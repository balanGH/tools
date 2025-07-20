---

````markdown
# 🎧 YTD – YouTube Terminal Downloader

Download **YouTube videos** and **audio** or just **MP3 audio** from the terminal with a colorful progress bar and slick ASCII flair.

---

## 🔧 Requirements

### 1. Python 3.6+

Ensure that Python 3.6 or higher is installed on your system.

You can check the Python version with:
```bash
python --version
````

### 2. Install Dependencies

Install the required Python library **yt-dlp** (an improved version of youtube-dl):

```bash
pip install yt-dlp
```

---

## 🚀 Getting Started

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/balanGH/media-tools.git
cd media-tools/downloader
```

### 2. Run the Downloader

You can use the downloader by running the Python script. It will allow you to download **YouTube videos** or **audio files** from YouTube.

```bash
python3 yt_download_video+audio.py
```

### 3. Follow the Prompts

* **Enter the YouTube video URL**: The script will ask you for the URL of the YouTube video.
* **Choose the format**: You'll be prompted to choose the format for both the video and the audio.

Example session:

```bash
$ python3 yt_download_video+audio.py
🔗 Enter YouTube video URL: https://www.youtube.com/watch?v=video_id
Available video formats:
1. 720p - mp4 - 1500 kbps
2. 1080p - mp4 - 3000 kbps

Choose video format number: 2
Available audio formats:
1. 128kbps - mp3
2. 320kbps - mp3

Choose audio format number: 2

⬇️ Downloading and merging...
✅ Download & merge complete!
```

### 4. File Output

* The downloaded and merged video/audio will be saved in the same directory with the title of the video as the filename.
* Example output: `video_title.mp4`.

---

## 🛠️ Customization

* You can modify the script to change the output format or the way the video/audio is processed by editing the `yt_download_video+audio.py` file.

---

## ✨ Author

Created with ❤️ by **balanGH**

```

---

### Key Features:
1. **Requirements**: A section explaining the required dependencies (`yt-dlp` and Python 3.6+).
2. **Getting Started**: Details on how to clone the repository, install dependencies, and run the script.
3. **Interactive Prompts**: Provides a guide to follow the prompts for downloading video and audio.
4. **File Output**: Specifies how the downloaded content will be saved.

This updated **`README.md`** is now complete for your **YouTube Terminal Downloader (YTD)** tool!

Let me know if you'd like to add more information or tweak anything else.
```
