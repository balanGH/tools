from moviepy import VideoFileClip
import subprocess
import re

def get_video_bitrate(input_path):
    """Get bitrate of the input video in kbps using ffprobe"""
    try:
        # Run ffprobe command to get bitrate in bits/s
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
        print("Error getting bitrate:", e)
        return None

def compress_video(input_path, output_path, target_bitrate, target_height, preset='medium', threads=4):
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
    print(f"\nCompressed video saved as: {output_path}")

if __name__ == "__main__":
    input_path = input("Enter path to your video file: ").strip().strip("'\"")
    default_output = input_path.rsplit('.', 1)[0] + "_compressed.mp4"
    output_path = input(f"Enter output path for compressed video [{default_output}]: ").strip().strip("'\"")
    if not output_path:
        output_path = default_output

    orig_bitrate = get_video_bitrate(input_path)
    if orig_bitrate:
        print(f"Original video bitrate: {orig_bitrate} kbps")
    else:
        print("Could not determine original bitrate, defaulting to manual input.")

    print("\nChoose compression option:")
    print("1. Low quality (480p, ~500k bitrate)")
    print("2. Medium quality (720p, ~1500k bitrate)")
    print("3. High quality (1080p, ~3000k bitrate)")
    print("4. Custom: percentage of original bitrate (e.g. 50 for 50%)")

    choice = input("Enter option (1-4): ").strip()

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
            print("Original bitrate unknown. Please enter target bitrate manually (e.g., 1500k):")
            target_bitrate = input("Target bitrate: ").strip()
            target_height_str = input("Target height in pixels (e.g. 480, 720, 1080) [default 720]: ").strip()
            target_height = int(target_height_str) if target_height_str else 720
        else:
            percent_str = input("Enter compression percentage (e.g. 50 for 50% of original bitrate): ").strip()
            try:
                percent = float(percent_str)
                target_bitrate_value = int(orig_bitrate * (percent / 100))
                target_bitrate = f"{target_bitrate_value}k"
                target_height_str = input("Target height in pixels (e.g. 480, 720, 1080) [default 720]: ").strip()
                target_height = int(target_height_str) if target_height_str else 720
            except Exception:
                print("Invalid percentage entered, defaulting to 50% and 720p")
                target_bitrate = f"{orig_bitrate // 2}k"
                target_height = 720
    else:
        print("Invalid option, defaulting to Medium quality")
        target_height = 720
        target_bitrate = "1500k"

    preset = input("Enter encoding preset (ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow) [default medium]: ").strip()
    if not preset:
        preset = "medium"

    threads_str = input("Enter number of CPU threads to use [default 4]: ").strip()
    threads = int(threads_str) if threads_str.isdigit() else 4

    compress_video(input_path, output_path, target_bitrate, target_height, preset, threads)
