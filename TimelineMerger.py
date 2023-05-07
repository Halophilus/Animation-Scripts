import os
from PIL import Image

def merge_images(input_dir, output_dir, overlap_range):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    folder_list = sorted(os.listdir(input_dir), key=lambda x: int(x))
    current_frame = 0

    for i in range(len(folder_list)):
        current_folder = os.path.join(input_dir, folder_list[i])
        current_images = sorted(os.listdir(current_folder), key=lambda x: int(x.split('.')[0]))

        if i == 0:
            # Save all images from the first folder
            for img_name in current_images:
                img_path = os.path.join(current_folder, img_name)
                output_path = os.path.join(output_dir, f"{current_frame}.png")
                img = Image.open(img_path)
                img.save(output_path)
                current_frame += 1
        else:
            # Merge overlapping images
            for j in range(overlap_range):
                img1_path = os.path.join(output_dir, f"{current_frame - overlap_range + j}.png")
                img2_path = os.path.join(current_folder, current_images[j])

                img1 = Image.open(img1_path)
                img2 = Image.open(img2_path)

                img1.paste(img2, (0, 0), img2)
                output_path = os.path.join(output_dir, f"{current_frame - overlap_range + j}.png")
                img1.save(output_path)

            # Save non-overlapping images
            for img_name in current_images[overlap_range:]:
                img_path = os.path.join(current_folder, img_name)
                output_path = os.path.join(output_dir, f"{current_frame}.png")
                img = Image.open(img_path)
                img.save(output_path)
                current_frame += 1

input_dir = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\TimelineMerger\\input"  # Replace this with the path to your directory containing timeline folders
overlap_range = 8
output_dir = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\TimelineMerger\\output"

merge_images(input_dir, output_dir, overlap_range)

