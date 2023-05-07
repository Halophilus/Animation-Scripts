import os
import random
from PIL import Image, ImageChops

def glitch_images(input_folder, output_folder, num_output_images):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.png', '.gif'))]
    num_images = len(image_files)

    for i in range(num_output_images):
        image1_path = os.path.join(input_folder, random.choice(image_files))
        image2_path = os.path.join(input_folder, random.choice(image_files))

        image1 = Image.open(image1_path).convert("RGB")
        image2 = Image.open(image2_path).convert("RGB")


        glitched_image = ImageChops.add(image1, image2, scale=random.uniform(0.5, 1.5), offset=random.randint(-100, 100))

        # Randomly apply additional glitch effects
        if random.random() > 0.5:
            glitched_image = ImageChops.offset(glitched_image, xoffset=random.randint(-5, 5), yoffset=random.randint(-5, 5))

        if random.random() > 0.5:
            glitched_image = ImageChops.screen(glitched_image, image1)

        if random.random() > 0.5:
            glitched_image = ImageChops.subtract(glitched_image, image2, scale=random.uniform(0.5, 1.5), offset=random.randint(-100, 100))

        output_path = os.path.join(output_folder, f'glitched_{i}.png')
        glitched_image.save(output_path)

input_folder = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\GlitchGenerator\\input"
output_folder = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\GlitchGenerator\\output"
num_output_images = 90
glitch_images(input_folder, output_folder, num_output_images)
