import yt_dlp
import os

def download_youtube_audio(video_url, output_path='./'):
    """
    Downloads audio from a YouTube video and saves it as an MP3 file using yt-dlp.
    
    Args:
        video_url (str): URL of the YouTube video
        output_path (str): Directory where the audio file will be saved
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'quiet': False,
            'no_warnings': False,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info_dict)
            base, ext = os.path.splitext(filename)
            mp3_file = base + '.mp3'
            
            print(f"\nDownload completed! Audio saved as: {mp3_file}")
            return mp3_file
            
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage
    video_url = input("Enter YouTube video URL: ").strip()
    download_youtube_audio(video_url)