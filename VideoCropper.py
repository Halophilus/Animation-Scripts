import cv2
import os
import sys
import subprocess


def crop_and_trim_video(input_path, output_path, width, height, position, start_time, end_time):
    if not os.path.isfile(input_path):
        print(f"Input file {input_path} not found.")
        sys.exit(1)

    input_directory, _ = os.path.split(input_path)

    # Get video dimensions
    cap = cv2.VideoCapture(input_path)
    video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()

    # Calculate crop positions based on the provided position parameter
    if position.lower() == 'center':
        x = (video_width - width) // 2
        y = (video_height - height) // 2
    elif position.lower() == 'left':
        x = 0
        y = (video_height - height) // 2
    elif position.lower() == 'right':
        x = video_width - width
        y = (video_height - height) // 2
    elif position.lower() == 'top':
        x = (video_width - width) // 2
        y = 0
    elif position.lower() == 'bottom':
        x = (video_width - width) // 2
        y = video_height - height
    else:
        print(f"Invalid position value: {position}")
        sys.exit(1)

    command = [
        "ffmpeg",
        "-ss", start_time,
        "-i", input_path,
        "-t", end_time,
        "-filter:v", f"crop={width}:{height}:{x}:{y}",
        "-c:a", "copy",
        output_path
    ]

    try:
        subprocess.run(command, cwd=input_directory, check=True)
        print(f"Video successfully cropped and trimmed, saved to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during cropping and trimming: {e}")
        sys.exit(1)


if __name__ == "__main__":
    input_file = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\VideoCropper\\input.mp4"
    output_file = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\VideoCropper\\output.mp4"
    crop_width, crop_height = 640, 480
    position = "center"  # 'center', 'left', 'right', 'top', or 'bottom'
    start_time = "00:00:00"  # start time in format "HH:MM:SS"
    end_time = "00:17:00"  # duration in format "HH:MM:SS"

    crop_and_trim_video(input_file, output_file, crop_width, crop_height, position, start_time, end_time)

