import os
from PIL import Image

def superimpose_frames(paste_point, input_folder_1, input_folder_2, output_folder):
    for subfolder in os.listdir(input_folder_1):
        subfolder_path_1 = os.path.join(input_folder_1, subfolder)
        subfolder_path_2 = os.path.join(input_folder_2, subfolder)
        
        if not os.path.isdir(subfolder_path_1) or not os.path.isdir(subfolder_path_2):
            continue
        
        files_1 = sorted(os.listdir(subfolder_path_1), key=lambda x: int(x.split('.')[0]))
        files_2 = sorted(os.listdir(subfolder_path_2), key=lambda x: int(x.split('.')[0]))
        
        num_files_1 = len(files_1)
        num_files_2 = len(files_2)

        output_subfolder = os.path.join(output_folder, subfolder)
        if not os.path.exists(output_subfolder):
            os.makedirs(output_subfolder)

        for i in range(max(num_files_1, num_files_2)):
            file_1 = files_1[i % num_files_1]
            file_2 = files_2[i % num_files_2]

            img1 = Image.open(os.path.join(subfolder_path_1, file_1)).convert("RGBA")
            img2 = Image.open(os.path.join(subfolder_path_2, file_2)).convert("RGBA")

            img2.paste(img1, paste_point, img1)
            img2.save(os.path.join(output_subfolder, f"{i+1}.png"))

if __name__ == "__main__":
    paste_point = (0, 0)
    input_folder_1 = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\FrameSuperimposer\\input_folder_1"
    input_folder_2 = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\FrameSuperimposer\\input_folder_2"
    output_folder = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\FrameSuperimposer\\output_folder"

    superimpose_frames(paste_point, input_folder_1, input_folder_2, output_folder)
