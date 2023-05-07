import os
import random
from PIL import Image

def generate_colored_noise_frames(num_frames, resolution, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in range(num_frames):
        img = Image.new("RGB", resolution)
        pixels = img.load()

        for x in range(resolution[0]):
            for y in range(resolution[1]):
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                pixels[x, y] = (r, g, b)

        img.save(os.path.join(output_folder, f"frame_{i:04d}.png"))

if __name__ == "__main__":
    num_frames = 300  # Number of frames to generate
    resolution = (645, 445)  # Frame resolution (width, height)
    output_folder = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\StaticFrames\\output"  # Output folder for the frames

    generate_colored_noise_frames(num_frames, resolution, output_folder)
