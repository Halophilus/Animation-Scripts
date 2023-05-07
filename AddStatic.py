import os
import random
import cv2
import numpy as np

def apply_gaussian_noise(image, mean, std_dev):
    noise = np.zeros_like(image, dtype=np.uint8)
    cv2.randn(noise, mean, std_dev)
    noisy_image = cv2.add(image, noise)
    return noisy_image

def add_noise_to_images_in_folder(input_folder, output_folder, min_noise=10, max_noise=50):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            image = cv2.imread(file_path)
            if image is not None:
                random_noise_std_dev = random.randint(min_noise, max_noise)
                noisy_image = apply_gaussian_noise(image, mean=0, std_dev=random_noise_std_dev)
                output_file_path = os.path.join(output_folder, file_name)
                cv2.imwrite(output_file_path, noisy_image)
                print(f"Processed {file_path} with noise std dev {random_noise_std_dev}")

if __name__ == "__main__":
    input_folder = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\AddStatic\\input"
    output_folder = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\AddStatic\\output"
    min_noise = 60
    max_noise = 200

    add_noise_to_images_in_folder(input_folder, output_folder, min_noise, max_noise)
