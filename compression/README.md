---

````markdown
# 🎥 Media Compression Tools

A collection of tools for compressing **images** and **videos** using different technologies:

- **Image Compression** using C++ and `libjpeg`
- **Video Compression** using Python and FFmpeg (or OpenCV)

---

## 📁 Project Structure

```plaintext
compression/
├── image_compression/            # Contains C++ code for JPEG image compression.
├── image_compression.cpp         # The C++ source file for image compression.
├── video_compression.py          # Python script to compress video files using FFmpeg/OpenCV.
├── VideoCompressing.py           # A secondary Python script for video compression (optional, if needed).
└── README.md                     # This documentation
````

---

## 🚀 Getting Started

### Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/balanGH/media-tools.git
cd media-tools/compression
```

### Install Dependencies

For **Image Compression**:

* **libjpeg** development libraries (for JPEG image compression):

  On Ubuntu/Debian:

  ```bash
  sudo apt-get install libjpeg-dev
  ```

  On Fedora/RHEL:

  ```bash
  sudo dnf install libjpeg-turbo-devel
  ```

For **Video Compression**:

* **Python 3.x**

* **FFmpeg** (must be installed and added to PATH):

  [Download FFmpeg](https://ffmpeg.org/download.html)

* **Python packages**:
  Install the required Python libraries for video compression:

  ```bash
  pip install moviepy opencv-python ffmpeg-python
  ```

---

## 📸 Image Compression

This tool uses **C++** and **libjpeg** to compress JPEG images.

### How to Use

1. **Compile the C++ code**:

   Compile the `image_compression.cpp` file:

   ```bash
   g++ image_compression.cpp -o image_compression -ljpeg
   ```

2. **Run the compression tool**:

   Compress an image by providing the input file, output file, and the quality percentage (0-100):

   ```bash
   ./image_compression input.jpg output.jpg 75
   ```

   * `input.jpg`: The image you want to compress.
   * `output.jpg`: The output compressed image.
   * `75`: The quality percentage (adjust for more/less compression).

---

## 🎞 Video Compression

This tool uses **Python** and **FFmpeg** or **OpenCV** to compress video files.

### How to Use

1. **Run the video compression script**:

   Run the `video_compression.py` Python script to compress a video:

   ```bash
   python3 video_compression.py
   ```

2. **Follow the prompts**:

   * Enter the path to your video file.
   * Choose the output filename (default will append `_compressed`).
   * Choose the compression option (low, medium, high, or custom bitrate).
   * Select the encoding preset (optional).
   * Set the number of CPU threads to use (optional).

3. **Example terminal session**:

   ```bash
   $ python3 video_compression.py
   Enter path to your video file: video.mp4
   Enter output path for compressed video [video_compressed.mp4]: 
   Original video bitrate: 1230 kbps

   Choose compression option:
   1. Low quality (480p, ~500k bitrate)
   2. Medium quality (720p, ~1500k bitrate)
   3. High quality (1080p, ~3000k bitrate)
   4. Custom: percentage of original bitrate (e.g. 50 for 50%)
   Enter option (1-4): 2
   Enter encoding preset (ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow) [default medium]: fast
   Enter number of CPU threads to use [default 4]: 

   Compressed video saved as: video_compressed.mp4
   ```

---

## ✨ Author

Created with ❤️ by **balanGH**

```

---

### Key Details:
1. **Getting Started**:
   - Instructions on how to **clone** the repo and **install dependencies** for both **image** and **video compression**.
  
2. **Image Compression**:
   - Provides the steps to **compile** and **run** the image compression tool.
  
3. **Video Compression**:
   - Explains how to **use** the video compression script and includes example terminal output for user guidance.

This **`README.md`** now provides only the essential details for **compressing images and videos**.

Let me know if you need any more modifications!
```
