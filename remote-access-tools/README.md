---

# 🖥️ Remote Access Tools

A collection of **Python-based remote desktop tools** built with Flask, allowing remote screen sharing, mouse and keyboard control, screenshot capture, and screen recording — all through a web browser.

---

## ⚙️ Features

* **Live Screen Mirroring**: View the host's screen in real-time via browser.
* **Mouse Control**: Remotely move and click the mouse.
* **Keyboard Input**: Type and send key presses from the browser.
* **Screenshot Capture**: Take and download current screen snapshots.
* **Screen Recording**: Record and download screen activity as video.

---

## 📁 Project Structure

```plaintext
remote_access_tools/
├── remote-access (mouse+keyboard).py   # Full remote control (screen + mouse + keyboard)
├── remote-mouse_control.py             # Screen mirroring + mouse control
├── screen_mirroring.py                 # Screen mirroring + screenshot + recording
└── README.md                           # This documentation
````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/balanGH/media-tools.git
cd remote-access-tools
```

### 2. Install Dependencies

Ensure Python 3.x is installed. Then install the required packages:

```bash
pip install Flask pyautogui numpy opencv-python pillow
```

> ⚠️ On Linux, `pyautogui` may require additional dependencies:

```bash
sudo apt-get install scrot python3-tk python3-dev python3-xlib
```

---

## 🧪 Tools & Usage

### 1. `remote-access (mouse+keyboard).py`

**Full remote control with screen, mouse, and keyboard functionality.**

* **Port**: `5000`

* **Usage**:

  ```bash
  python "remote-access (mouse+keyboard).py"
  ```

* **Access in browser**: [http://localhost:5000](http://localhost:5000)

* **Access in browser**: [http://\<your-ip>:5000](http://<your-ip>:5000)

---

### 2. `remote-mouse_control.py`

**Screen sharing + remote mouse control.**

* **Port**: `5000`

* **Usage**:

  ```bash
  python remote-mouse_control.py
  ```

* **Access in browser**: [http://localhost:5000](http://localhost:5000)

* **Access in browser**: [http://\<your-ip>:5000](http://<your-ip>:5000)

---

### 3. `screen_mirroring.py`

**Screen sharing with screenshot and video recording features.**

* **Port**: `8000`

* **Features**:

  * Live feed at 15 FPS
  * Screenshot download
  * Start/Stop recording (saved as `recording.avi`)
  * Download recorded video

* **Usage**:

  ```bash
  python screen_mirroring.py
  ```

* **Access in browser**: [http://localhost:8000](http://localhost:8000)

* **Access in browser**: [http://\<your-ip>:8000](http://<your-ip>:8000)

---

## 🔐 Security Notes

* These tools bind to `0.0.0.0`, making them accessible from other devices on the same network.
* **No authentication** is implemented by default.
* For **safe use**, especially on shared or public networks:

  * Use firewalls or VPNs
  * Add password protection or IP filtering
  * Avoid exposing these services to the open internet

---

## 🛠 Requirements

* Python 3.x
* Flask
* pyautogui
* OpenCV (`cv2`)
* NumPy
* Pillow

---

## ❓ Troubleshooting

* **Mouse/Keyboard not working?**

  * Make sure browser window is in focus.
  * Some platforms restrict automation permissions — check system settings.

* **Black screen or frame errors?**

  * On macOS/Linux, allow screen recording or screenshot access.
  * Ensure your system supports screen capture and `pyautogui`.

* **Recording not saving?**

  * Ensure you have write permissions in the current directory.
  * File is saved as `recording.avi` upon stopping.

---

## 📄 License

This project is for **educational and personal use**. You are free to modify and distribute it, but use responsibly and ethically.

---

## 👨‍💻 Author

Created with ❤️ by **balanGH**

---

### ✅ Key Details:

1. **Getting Started**:

   * Step-by-step guide to **clone the repository** and **install required packages**.

2. **Script Breakdown**:

   * Descriptions and usage instructions for:

     * Full remote control (`remote-access (mouse+keyboard).py`)
     * Mouse-only control (`remote-mouse_control.py`)
     * Screen mirroring with recording (`screen_mirroring.py`)

3. **Security Advice**:

   * Highlights the risks of running on `0.0.0.0` and offers best practices.

4. **Troubleshooting**:

   * Covers common issues like screen permission errors or feature inaccessibility.
    
