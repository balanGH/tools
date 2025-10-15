# 🛠️ Tools

A collection of utilities for media compression, remote access, and media downloading built with Python and C++.

---

## 📁 Project Structure

```plaintext
tools/
├── compression/
│   ├── image_compression.cpp
│   ├── video_compression.py
│   ├── VideoCompressing.py
│   └── README.md
├── downloader/
│   ├── youtube_mp4_to_mp3.py
│   ├── yt_download_(vid+aud).py
│   └── README.md
└── remote-access/
    ├── remote-access (mouse+keyboard).py
    ├── remote-mouse_control.py
    ├── screen_mirroring.py
    └── README.md
```

---

## 🖼️ Compression Tools

### Image Compression (C++ with libjpeg)

* Compile with:

  ```bash
  g++ image_compression.cpp -o image_compression -ljpeg
  ```

* Run:

  ```bash
  ./image_compression input.jpg output.jpg 75
  ```

  Where `75` is quality (0-100).

---

### Video Compression (Python with FFmpeg/OpenCV)

* Run the Python script:

  ```bash
  python3 video_compression.py
  ```

* Follow prompts to compress video by selecting bitrate, resolution, etc.

---

## 📥 Downloader Tools

### 1. `youtube_mp4_to_mp3.py`

* Convert YouTube videos (mp4) to mp3 audio.

* Usage:

  ```bash
  python youtube_mp4_to_mp3.py
  ```

### 2. `yt_download_(vid+aud).py`

* Download YouTube video and audio streams separately.

* Usage:

  ```bash
  python yt_download_(vid+aud).py
  ```

---

## 🖥️ Remote Access Tools

### 1. `remote-access (mouse+keyboard).py`

* Full remote control: screen + mouse + keyboard.

* Run:

  ```bash
  python "remote-access (mouse+keyboard).py"
  ```

* Access via browser: `http://localhost:5000`

---

### 2. `remote-mouse_control.py`

* Remote mouse control with screen sharing.

* Run:

  ```bash
  python remote-mouse_control.py
  ```

* Access via browser: `http://localhost:5000`

---

### 3. `screen_mirroring.py`

* Screen sharing + screenshots + recording.

* Run:

  ```bash
  python screen_mirroring.py
  ```

* Access via browser: `http://localhost:8000`

---

## 🚀 Getting Started

### Clone Repo

```bash
git clone https://github.com/balanGH/tools.git
cd tools
```

### Install Dependencies

* For image compression:

  ```bash
  sudo apt-get install libjpeg-dev
  ```

* For video compression:

  ```bash
  pip install moviepy opencv-python ffmpeg-python
  ```

* For downloader tools:

  * Usually requires `pytube` or similar (check downloader scripts).

  ```bash
  pip install pytube
  ```

* For remote access tools:

  ```bash
  pip install Flask pyautogui numpy opencv-python pillow
  ```

* Additional Linux dependencies for pyautogui:

  ```bash
  sudo apt-get install scrot python3-tk python3-dev python3-xlib
  ```

---

## 🔐 Security Notes

* Services bind to `0.0.0.0` — accessible on local network.
* No authentication by default; **use caution** on untrusted networks.
* Consider firewalls, VPNs, or adding authentication for security.

---

## ❓ Troubleshooting

* Mouse/keyboard control requires browser focus.
* Screen capture may require system permissions.
* Recording saves to current directory as `recording.avi`.
* Downloader scripts may need updated libraries or API keys.

---

## 📄 License

For educational and personal use. Modify and distribute responsibly.

---

## 👨‍💻 Author

Created with ❤️ by **balanGH**
