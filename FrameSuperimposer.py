import os
import re
from PIL import Image

def extract_frame_number(filename):
    return int(re.search(r'\d+', filename).group())

def superimpose_frames(paste_point, input_folder_1, input_folder_2, output_folder):
    files_1 = sorted([f for f in os.listdir(input_folder_1) if f.lower().endswith(('.png', '.jpg', '.jpeg'))], key=extract_frame_number)
    files_2 = sorted([f for f in os.listdir(input_folder_2) if f.lower().endswith(('.png', '.jpg', '.jpeg'))], key=extract_frame_number)

    num_files_1 = len(files_1)
    num_files_2 = len(files_2)

    if num_files_1 == 0 or num_files_2 == 0:
        print("Error: One or both input folders are empty or do not contain valid image files.")
        return

    max_files = max(num_files_1, num_files_2)

    for i in range(max_files):
        file_1 = files_1[i % num_files_1]
        file_2 = files_2[i % num_files_2]

        img1 = Image.open(os.path.join(input_folder_1, file_1)).convert("RGBA")
        img2 = Image.open(os.path.join(input_folder_2, file_2)).convert("RGBA")

        img2.paste(img1, paste_point, img1)
        img2.save(os.path.join(output_folder, f"{i+1}.png"))

if __name__ == "__main__":
    # Replace these values with your desired values
    paste_x = 260
    paste_y = 0
    input_folder_1 = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\FrameSuperimposer\\input_folder_1"
    input_folder_2 = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\FrameSuperimposer\\input_folder_2"
    output_folder = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\FrameSuperimposer\\output_folder"

    paste_point = (paste_x, paste_y)
    superimpose_frames(paste_point, input_folder_1, input_folder_2, output_folder)
