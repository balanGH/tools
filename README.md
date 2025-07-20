---

````markdown
# 🎥 Media Tools

A collection of terminal-based tools for compressing and processing media files — including **image compression** in C++, **video compression** in Python, and **YouTube video/audio downloading** via the terminal.

---

## 📁 Project Structure

```plaintext
media-tools/
├── compression/
│   ├── image_compression/
│   │   └── image_compression.cpp      # JPEG compression using libjpeg
│   ├── video_compression/
│   │   └── video_compression.py       # Video compression using FFmpeg/OpenCV
│
├── downloader/
│   ├── yt_download_video+audio.py     # Download and merge YouTube video + audio (MP4)
│   ├── youtube_mp4_to_mp3.py          # Download YouTube audio as high-quality MP3
│   └── README.md                      # Instructions for downloader tools
│
└── README.md                         # This documentation
````

---

## 🛠 Features

* **🎧 YouTube Downloader**:
  Download **YouTube videos** and extract **audio** using `yt_dlp`, with a colorful terminal UI and progress bars.

* **🖼 Image Compression**:
  C++ tool to compress **JPEG images** using `libjpeg`.

* **🎞 Video Compression**:
  Python-based video compression using **FFmpeg** or **OpenCV** for efficient video size reduction.

---

## 📦 Requirements

### 1. General Requirements:

* Python 3.6+
* C++ compiler (`g++` for image compression)
* **FFmpeg** (for video/audio processing)

### 2. Python Dependencies:

* `yt_dlp` for downloading YouTube content:

  ```bash
  pip install yt-dlp
  ```

### 3. System Dependencies:

* **libjpeg** development libraries for image compression:

  * **On Ubuntu/Debian**:

    ```bash
    sudo apt-get install libjpeg-dev
    ```
  * **On Fedora/RHEL**:

    ```bash
    sudo dnf install libjpeg-turbo-devel
    ```

* **FFmpeg** (for video compression):
  Install via your system’s package manager:

  ```bash
  sudo apt-get install ffmpeg      # Ubuntu/Debian
  brew install ffmpeg              # macOS (with Homebrew)
  ```

---

## 🚀 Usage

### 1. **YouTube Downloader**

In the `downloader` directory, you have two scripts for downloading content:

#### Download Video + Audio:

```bash
cd downloader
python yt_download_video+audio.py       # Download and merge video + audio as MP4
```

#### Download Audio Only (MP3):

```bash
python youtube_mp4_to_mp3.py            # Download audio only as MP3
```

### 2. **Image Compression (C++)**

Navigate to the `compression/image_compression` directory and compile the C++ code to compress JPEG images:

```bash
cd compression/image_compression
g++ image_compression.cpp -o compress -ljpeg
./compress input.jpg output.jpg
```

### 3. **Video Compression (Python)**

Navigate to the `compression/video_compression` directory and run the Python script for video compression:

```bash
cd compression/video_compression
python video_compression.py input.mp4 output.mp4
```

---

## ✨ Author

Created with ❤️ by **balanGH**

```

---

### Key Updates:
1. **Organization**: The project structure is made clearer, detailing where each tool resides (image compression, video compression, downloader tools).
2. **Requirements**: A specific section for general, Python, and system dependencies.
3. **Usage**: Concise steps for running each tool, both for the downloader and the compression tools.
4. **Author**: Added a personalized "Author" section.

This version should now clearly reflect the overall structure and provide concise instructions for using each tool in the project.

Let me know if you'd like to modify or add anything!
```
