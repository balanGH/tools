from moviepy import VideoFileClip
import subprocess

# ANSI colors
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

def get_video_bitrate(input_path):
    """Get bitrate of the input video in kbps using ffprobe"""
    try:
        result = subprocess.run(
            ['ffprobe', '-v', 'error', '-select_streams', 'v:0',
             '-show_entries', 'format=bit_rate', '-of', 'default=noprint_wrappers=1:nokey=1',
             input_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        bitrate_bps = result.stdout.strip()
        if bitrate_bps.isdigit():
            return int(bitrate_bps) // 1000  # convert to kbps
        else:
            return None
    except Exception as e:
        print(f"{RED}Error getting bitrate:{RESET} {e}")
        return None

def compress_video(input_path, output_path, target_bitrate, target_height, preset='medium', threads=4):
    print(f"{CYAN}Starting compression...{RESET}")
    clip = VideoFileClip(input_path)
    clip_resized = clip.resized(height=target_height)
    clip_resized.write_videofile(
        output_path,
        bitrate=target_bitrate,
        codec='libx264',
        audio_codec='aac',
        preset=preset,
        threads=threads
    )
    clip.close()
    print(f"\n{GREEN}✅ Compressed video saved as: {output_path}{RESET}")

if __name__ == "__main__":
    input_path = input(f"{BLUE}Enter path to your video file:{RESET} ").strip().strip("'\"")
    default_output = input_path.rsplit('.', 1)[0] + "_compressed.mp4"
    output_path = input(f"{BLUE}Enter output path for compressed video [{default_output}]:{RESET} ").strip().strip("'\"")
    if not output_path:
        output_path = default_output

    orig_bitrate = get_video_bitrate(input_path)
    if orig_bitrate:
        print(f"{GREEN}Original video bitrate: {orig_bitrate} kbps{RESET}")
    else:
        print(f"{YELLOW}Could not determine original bitrate, defaulting to manual input.{RESET}")

    print(f"""
{MAGENTA}Choose compression option:{RESET}
1. Low quality (480p, ~500k bitrate)
2. Medium quality (720p, ~1500k bitrate)
3. High quality (1080p, ~3000k bitrate)
4. Custom: percentage of original bitrate (e.g. 50 for 50%)
""")

    choice = input(f"{BLUE}Enter option (1-4):{RESET} ").strip()

    if choice == "1":
        target_height = 480
        target_bitrate = "500k"
    elif choice == "2":
        target_height = 720
        target_bitrate = "1500k"
    elif choice == "3":
        target_height = 1080
        target_bitrate = "3000k"
    elif choice == "4":
        if orig_bitrate is None:
            print(f"{YELLOW}Original bitrate unknown. Please enter target bitrate manually (e.g., 1500k):{RESET}")
            target_bitrate = input(f"{BLUE}Target bitrate:{RESET} ").strip()
            target_height_str = input(f"{BLUE}Target height in pixels (e.g. 480, 720, 1080) [default 720]:{RESET} ").strip()
            target_height = int(target_height_str) if target_height_str else 720
        else:
            percent_str = input(f"{BLUE}Enter compression percentage (e.g. 50 for 50% of original bitrate):{RESET} ").strip()
            try:
                percent = float(percent_str)
                target_bitrate_value = int(orig_bitrate * (percent / 100))
                target_bitrate = f"{target_bitrate_value}k"
                target_height_str = input(f"{BLUE}Target height in pixels (e.g. 480, 720, 1080) [default 720]:{RESET} ").strip()
                target_height = int(target_height_str) if target_height_str else 720
            except Exception:
                print(f"{YELLOW}Invalid percentage entered, defaulting to 50% and 720p{RESET}")
                target_bitrate = f"{orig_bitrate // 2}k"
                target_height = 720
    else:
        print(f"{YELLOW}Invalid option, defaulting to Medium quality{RESET}")
        target_height = 720
        target_bitrate = "1500k"

    preset = input(f"{BLUE}Enter encoding preset (ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow) [default medium]:{RESET} ").strip()
    if not preset:
        preset = "medium"

    threads_str = input(f"{BLUE}Enter number of CPU threads to use [default 4]:{RESET} ").strip()
    threads = int(threads_str) if threads_str.isdigit() else 4

    compress_video(input_path, output_path, target_bitrate, target_height, preset, threads)
