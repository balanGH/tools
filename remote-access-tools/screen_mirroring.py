from flask import Flask, Response, send_file, request, jsonify
import pyautogui
import cv2
import numpy as np
import threading
import time
import io
# pip install Flask pyautogui numpy opencv-python pillow

app = Flask(__name__)

latest_frame_lock = threading.Lock()
latest_frame_jpeg = None

recording_lock = threading.Lock()
recording = False
video_writer = None
record_start_time = None
frame_count = 0

TARGET_FPS = 15

def capture_frames():
    global latest_frame_jpeg, video_writer, recording, frame_count
    screen_size = pyautogui.size()
    frame_interval = 1.0 / TARGET_FPS

    while True:
        start_time = time.time()
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        ret, jpeg = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
        if ret:
            with latest_frame_lock:
                latest_frame_jpeg = jpeg.tobytes()

        with recording_lock:
            if recording and video_writer is not None:
                video_writer.write(frame)
                frame_count += 1

        elapsed = time.time() - start_time
        sleep_time = max(0, frame_interval - elapsed)
        time.sleep(sleep_time)

def generate_frames():
    while True:
        with latest_frame_lock:
            if latest_frame_jpeg is None:
                continue
            frame = latest_frame_jpeg

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(1.0 / TARGET_FPS)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return '''
    <html>
      <head>
        <title>Screen Sharing with Screenshot & Recording</title>
      </head>
      <body>
        <h1>Live Screen Sharing</h1>
        <img src="/video_feed" width="80%" />
        <br/><br/>
        <button onclick="window.location.href='/download'">Download Screenshot</button>
        <button id="recBtn" onclick="toggleRecording()">Start Recording</button>

        <script>
        async function toggleRecording() {
            const btn = document.getElementById('recBtn');
            let action = btn.innerText.includes("Start") ? "start" : "stop";
            const resp = await fetch('/record', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({action: action})
            });
            const data = await resp.json();
            if (data.status === 'ok') {
                btn.innerText = action === "start" ? "Stop Recording" : "Start Recording";
                if (action === "stop") {
                    // After stopping, prompt user to download video
                    window.location.href = '/download_video';
                }
            } else {
                alert('Error: ' + data.message);
            }
        }
        </script>
      </body>
    </html>
    '''

@app.route('/download')
def download():
    with latest_frame_lock:
        if latest_frame_jpeg is None:
            return "No screenshot available yet.", 404
        data = latest_frame_jpeg

    return send_file(
        io.BytesIO(data),
        mimetype='image/jpeg',
        as_attachment=True,
        download_name='screenshot.jpg'
    )

@app.route('/record', methods=['POST'])
def record():
    global recording, video_writer, record_start_time, frame_count

    data = request.get_json()
    if not data or 'action' not in data:
        return jsonify(status='error', message='Invalid request')

    action = data['action']

    with recording_lock:
        if action == 'start':
            if recording:
                return jsonify(status='error', message='Already recording')
            screen_size = pyautogui.size()
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            video_writer = cv2.VideoWriter('recording.avi', fourcc, TARGET_FPS, (screen_size.width, screen_size.height))
            recording = True
            record_start_time = time.time()
            frame_count = 0
            print("Recording started")
            return jsonify(status='ok')

        elif action == 'stop':
            if not recording:
                return jsonify(status='error', message='Not recording')
            
            # Optional: Check minimum recording duration
            duration = time.time() - record_start_time if record_start_time else 0
            if duration < 2:
                # If too short, you might want to reject or just warn
                print(f"Recording too short: {duration:.2f}s")
            
            recording = False
            if video_writer:
                video_writer.release()
                video_writer = None
            
            print(f"Recording stopped. Duration: {duration:.2f}s, Frames: {frame_count}")
            return jsonify(status='ok')

        else:
            return jsonify(status='error', message='Unknown action')

@app.route('/download_video')
def download_video():
    try:
        return send_file('recording.avi', as_attachment=True)
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == '__main__':
    threading.Thread(target=capture_frames, daemon=True).start()
    app.run(host='0.0.0.0', port=8000, threaded=True)
