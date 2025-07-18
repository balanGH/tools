import yt_dlp
import os
import sys

# ANSI escape codes for colors
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

def print_logo():
    logo = f"""
{CYAN}
__     ___   _____    _____  
\\ \\   / _|  |_   _|  |  __ \\ 
 \\ \\_/ /      | |    | |  | |
  \\   /       | |    | |  | |
   | |        | |    | |__| |
   |_|        |_|    |_____/

 Y   T   D – YouTube Terminal Downloader 💾🎵
{RESET}
    """
    print(logo)

def hook_progress(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes', 0)
        if total:
            progress = int(downloaded / total * 30)
            bar = '█' * progress + '-' * (30 - progress)
            percent = downloaded / total * 100
            sys.stdout.write(f"\r{YELLOW}🔄 Downloading: [{bar}] {percent:.2f}%{RESET}")
            sys.stdout.flush()
    elif d['status'] == 'finished':
        print(f"\n{GREEN}✅ Download complete. Converting to MP3...{RESET}")

def download_youtube_audio(video_url, output_path='./'):
    try:
        os.makedirs(output_path, exist_ok=True)
        print_logo()
        print(YELLOW + "🔗 Fetching video data..." + RESET)

        ydl_opts = {
            'format': 'bestaudio/best',
            'progress_hooks': [hook_progress],
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info_dict)
            base, ext = os.path.splitext(filename)
            mp3_file = base + '.mp3'

            print(GREEN + f"\n🎉 Audio saved as: {mp3_file}" + RESET)
            return mp3_file

    except Exception as e:
        print(RED + f"\n❌ Error: {str(e)}" + RESET)
        return None

if __name__ == "__main__":
    video_url = input(BLUE + "🔗 Enter YouTube video URL: " + RESET).strip()
    download_youtube_audio(video_url)
