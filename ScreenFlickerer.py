import os
import random
from PIL import Image, ImageEnhance, ImageOps

def random_effect_intensity(min_intensity, max_intensity):
    return random.uniform(min_intensity, max_intensity)

def apply_crt_flicker_effect(input_folder, output_folder, relative_parameter):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        filepath = os.path.join(input_folder, file)

        if os.path.isfile(filepath) and file.lower().endswith(('png', 'jpg', 'jpeg')):
            img = Image.open(filepath)

            # Apply random color adjustment
            color_enhancer = ImageEnhance.Color(img)
            img = color_enhancer.enhance(random_effect_intensity(1 - relative_parameter, 1 + relative_parameter))

            # Apply random brightness adjustment
            brightness_enhancer = ImageEnhance.Brightness(img)
            img = brightness_enhancer.enhance(random_effect_intensity(1 - relative_parameter, 1 + relative_parameter))

            # Apply random contrast adjustment
            contrast_enhancer = ImageEnhance.Contrast(img)
            img = contrast_enhancer.enhance(random_effect_intensity(1 - relative_parameter, 1 + relative_parameter))

            # Save the modified image to the output folder
            img.save(os.path.join(output_folder, file))

if __name__ == '__main__':
    input_folder = 'C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\ScreenFlickerer\\input'
    output_folder = 'C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\ScreenFlickerer\\output'
    relative_parameter = 0.1  # Adjust this value to control the range of effect intensities
    apply_crt_flicker_effect(input_folder, output_folder, relative_parameter)
