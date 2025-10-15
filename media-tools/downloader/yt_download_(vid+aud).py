import yt_dlp
import os
import sys

# Colors
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

 Y   T   D – YouTube Terminal Downloader 🎬🎵
{RESET}
    """
    print(logo)

def get_available_formats(url):
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])

        video_formats = [f for f in formats if f.get('vcodec') != 'none' and f.get('acodec') == 'none']
        audio_formats = [f for f in formats if f.get('acodec') != 'none' and f.get('vcodec') == 'none']

        return video_formats, audio_formats, info_dict.get('title', 'video')

def choose_format(formats, media_type='video'):
    print(f"\nAvailable {media_type} formats:")
    for i, f in enumerate(formats):
        if media_type == 'video':
            print(f"{i + 1}. {f.get('format_id')} - {f.get('ext')} - {f.get('height', 'N/A')}p - {f.get('fps', 'N/A')}fps")
        else:
            print(f"{i + 1}. {f.get('format_id')} - {f.get('ext')} - {f.get('abr', 'N/A')}kbps")

    while True:
        try:
            choice = int(input(f"\nChoose {media_type} format number: "))
            if 1 <= choice <= len(formats):
                return formats[choice - 1]['format_id']
            else:
                print("❌ Invalid choice.")
        except ValueError:
            print("❌ Please enter a number.")

def download_and_merge(url, video_format_id, audio_format_id, output_path='./'):
    try:
        os.makedirs(output_path, exist_ok=True)

        print(YELLOW + "⬇️ Downloading and merging..." + RESET)

        ydl_opts = {
            'format': f'{video_format_id}+{audio_format_id}',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',  # output file will be MP4
            'progress_hooks': [hook_progress],
            'quiet': True,
            'no_warnings': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(GREEN + "\n✅ Download & merge complete!" + RESET)

    except Exception as e:
        print(RED + f"\n❌ Error: {str(e)}" + RESET)

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
        print(f"\n{GREEN}✅ Download complete. Merging with audio...{RESET}")

if __name__ == "__main__":
    print_logo()
    url = input(BLUE + "🔗 Enter YouTube video URL: " + RESET).strip()
    
    video_formats, audio_formats, title = get_available_formats(url)
    video_id = choose_format(video_formats, 'video')
    audio_id = choose_format(audio_formats, 'audio')

    download_and_merge(url, video_id, audio_id)
