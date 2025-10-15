from flask import Flask, Response, request, jsonify
import pyautogui
import cv2
import numpy as np
import threading
import time
# pip install Flask pyautogui numpy opencv-python pillow

app = Flask(__name__)

latest_frame_lock = threading.Lock()
latest_frame_jpeg = None

def capture_frames():
    global latest_frame_jpeg
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        ret, jpeg = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
        if ret:
            with latest_frame_lock:
                latest_frame_jpeg = jpeg.tobytes()
        time.sleep(0.1)

def generate_frames():
    while True:
        with latest_frame_lock:
            if latest_frame_jpeg is None:
                continue
            frame = latest_frame_jpeg
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(0.1)

@app.route('/')
def index():
    return '''
    <html>
      <head><title>Remote Control</title></head>
      <body>
        <h1>Live Screen + Remote Mouse & Keyboard Control</h1>
        <p>Move mouse or click inside the image to control mouse.<br>
           Focus this page and type to send keyboard input.</p>
        <img id="screen" src="/video_feed" width="auto" style="border:1px solid black;"/>
        <script>
          const img = document.getElementById('screen');

          img.onload = () => {
            img.naturalWidth_ = img.naturalWidth;
            img.naturalHeight_ = img.naturalHeight;
          }

          function sendMouseEvent(type, x, y, button=0) {
            fetch('/mouse', {
              method: 'POST',
              headers: {'Content-Type': 'application/json'},
              body: JSON.stringify({type: type, x: x, y: y, button: button})
            });
          }

          function scaleCoords(clientX, clientY) {
            const rect = img.getBoundingClientRect();
            const scaleX = img.naturalWidth_ / rect.width;
            const scaleY = img.naturalHeight_ / rect.height;
            const x = Math.round((clientX - rect.left) * scaleX);
            const y = Math.round((clientY - rect.top) * scaleY);
            return [x, y];
          }

          img.addEventListener('mousemove', e => {
            const [x, y] = scaleCoords(e.clientX, e.clientY);
            sendMouseEvent('move', x, y);
          });

          img.addEventListener('mousedown', e => {
            const [x, y] = scaleCoords(e.clientX, e.clientY);
            sendMouseEvent('down', x, y, e.button);
          });

          img.addEventListener('mouseup', e => {
            const [x, y] = scaleCoords(e.clientX, e.clientY);
            sendMouseEvent('up', x, y, e.button);
          });

          // Keyboard input handler
          document.addEventListener('keydown', e => {
            // Prevent default to avoid interfering with browser shortcuts sometimes
            e.preventDefault();
            fetch('/keyboard', {
              method: 'POST',
              headers: {'Content-Type': 'application/json'},
              body: JSON.stringify({type: 'keydown', key: e.key, code: e.code})
            });
          });

          document.addEventListener('keyup', e => {
            e.preventDefault();
            fetch('/keyboard', {
              method: 'POST',
              headers: {'Content-Type': 'application/json'},
              body: JSON.stringify({type: 'keyup', key: e.key, code: e.code})
            });
          });
        </script>
      </body>
    </html>
    '''

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/mouse', methods=['POST'])
def mouse():
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'No data'})

    x = data.get('x')
    y = data.get('y')
    event_type = data.get('type')
    button = data.get('button', 0)  # 0-left,1-middle,2-right

    try:
        if event_type == 'move':
            pyautogui.moveTo(x, y)
        elif event_type == 'down':
            if button == 0:
                pyautogui.mouseDown(x, y, button='left')
            elif button == 1:
                pyautogui.mouseDown(x, y, button='middle')
            elif button == 2:
                pyautogui.mouseDown(x, y, button='right')
        elif event_type == 'up':
            if button == 0:
                pyautogui.mouseUp(x, y, button='left')
            elif button == 1:
                pyautogui.mouseUp(x, y, button='middle')
            elif button == 2:
                pyautogui.mouseUp(x, y, button='right')
        else:
            return jsonify({'status': 'error', 'message': 'Unknown event type'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

    return jsonify({'status': 'ok'})

@app.route('/keyboard', methods=['POST'])
def keyboard():
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'No data'})
    
    event_type = data.get('type')  # 'keydown' or 'keyup'
    key = data.get('key')
    code = data.get('code')

    # Map some keys for pyautogui (basic)
    # pyautogui uses names like 'enter', 'shift', 'left', 'right', 'up', 'down', etc.
    # We'll just send key for now, but you can expand this map if needed.
    try:
        if event_type == 'keydown':
            pyautogui.keyDown(key)
        elif event_type == 'keyup':
            pyautogui.keyUp(key)
        else:
            return jsonify({'status': 'error', 'message': 'Unknown keyboard event'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    threading.Thread(target=capture_frames, daemon=True).start()
    app.run(host='0.0.0.0', port=5000, threaded=True)
