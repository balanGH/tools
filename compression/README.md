# Media Tools

A collection of tools for media compression, including:

- **Image Compression** using C++ and libjpeg
- **Video Compression** using Python and FFmpeg (or OpenCV)

## 📁 Project Structure

- `image_compression/`: Contains C++ code for JPEG image compression.
- `video_compression/`: Contains Python code for compressing videos.

## 🛠️ Requirements

For image compression:
- `libjpeg` development libraries (e.g., `libjpeg-dev` or `libjpeg-turbo-devel`)

For video compression:
- `Python 3.x`
- `ffmpeg` (must be installed and added to PATH)
- Python packages: `opencv-python`, `ffmpeg-python` *(optional)*

## 📸 Image Compression

Compile with:

```bash
g++ image_compression.cpp -o image_compression -ljpeg
./image_compression input.jpg output.jpg 75
