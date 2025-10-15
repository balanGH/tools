import sys
from moviepy import VideoFileClip
import tkinter as tk
from tkinter import filedialog

def compress_video(input_path, output_path, target_bitrate="2500k", target_height=480):
    clip = VideoFileClip(input_path)
    
    # Resize video while maintaining aspect ratio
    clip_resized = clip.resized(height=target_height)
    
    # Export with higher bitrate and medium preset for better quality
    clip_resized.write_videofile(
        output_path,
        bitrate=target_bitrate,
        codec='libx264',
        audio_codec='aac',
        preset='medium',    # medium encoding preset for balanced quality/speed
        threads=4           # adjust threads based on your CPU cores
    )
    
    clip.close()
    print(f"Compressed video saved as: {output_path}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    print("Please select your input video file...")
    input_path = filedialog.askopenfilename(
        title="Select video file",
        filetypes=[("Video files", "*.mp4 *.mov *.avi *.mkv *.flv"), ("All files", "*.*")]
    )
    
    if not input_path:
        print("No input file selected, exiting.")
        sys.exit(1)

    default_output = input_path.rsplit('.', 1)[0] + "_compressed.mp4"
    print(f"Select output location for compressed video (default: {default_output})")
    output_path = filedialog.asksaveasfilename(
        title="Save compressed video as",
        defaultextension=".mp4",
        initialfile=default_output,
        filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")]
    )
    
    if not output_path:
        print("No output path selected, exiting.")
        sys.exit(1)

    compress_video(input_path, output_path)
