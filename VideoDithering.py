import os
import cv2
import random
import numpy as np
from PIL import Image, ImageOps

def floyd_steinberg_dithering(image):
    return image.convert('P', dither=Image.FLOYDSTEINBERG)

def apply_random_dithering(image, color_palette_size=32, noise_intensity=10):
    # Apply slight variations to the image by adding random noise
    h, w, _ = np.asarray(image).shape
    noise = np.random.randint(-noise_intensity, noise_intensity + 1, (h, w, 1), dtype='int8')
    noisy_image = np.asarray(image) + noise
    np.clip(noisy_image, 0, 255, out=noisy_image)
    image = Image.fromarray(noisy_image.astype(np.uint8))

    # Apply Floyd-Steinberg dithering with reduced color palette
    dithered_image = image.quantize(colors=color_palette_size).convert('RGB')
    dithered_image = dithered_image.convert('P', dither=Image.FLOYDSTEINBERG)

    return dithered_image

def process_video(input_video_path, output_folder):
    video_capture = cv2.VideoCapture(input_video_path)
    frame_number = 0

    while True:
        # Read a frame from the video
        ret, frame = video_capture.read()

        if not ret:
            break

        # Convert the frame to a PIL Image
        frame_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Apply random dithering
        dithered_frame_image = apply_random_dithering(frame_image)

        # Save the frame to the output folder
        output_frame_path = os.path.join(output_folder, f"{frame_number:01d}.png")
        dithered_frame_image.save(output_frame_path, format="PNG")

        frame_number += 1

    video_capture.release()

def process_video_folder(input_folder):
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Check if the file is an MP4 file
        if not os.path.isfile(file_path) or not filename.lower().endswith('.mp4'):
            continue

        # Create an output folder named after the file
        output_folder = os.path.join(input_folder, os.path.splitext(filename)[0])
        os.makedirs(output_folder, exist_ok=True)

        # Process the video and save the frames to the output folder
        process_video(file_path, output_folder)

input_folder = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\VideoDithering"
process_video_folder(input_folder)

