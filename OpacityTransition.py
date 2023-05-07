from PIL import Image
import os

def create_transition(input_folder1, input_folder2, output_folder):
    # Get the list of frames from both input folders
    frames1 = sorted(os.listdir(input_folder1))
    frames2 = sorted(os.listdir(input_folder2))

    # Determine the total number of output frames
    total_output_frames = max(len(frames1), len(frames2))

    # Calculate the opacity increment based on the total number of output frames
    opacity_increment = 255 / total_output_frames

    for i in range(total_output_frames):
        # Load images from input folders, handling cases where one folder has more frames than the other
        frame1 = frames1[min(i, len(frames1) - 1)]
        frame2 = frames2[min(i, len(frames2) - 1)]

        img1 = Image.open(os.path.join(input_folder1, frame1)).convert('RGBA')
        img2 = Image.open(os.path.join(input_folder2, frame2)).convert('RGBA')

        # Calculate the current opacity for img1
        current_opacity = int(255 - (i * opacity_increment))

        # Apply the current opacity to img1
        img1.putalpha(current_opacity)

        # Overlay img1 onto img2
        img2.paste(img1, (0, 0), img1)

        # Save the resulting image to the output folder
        img2.save(os.path.join(output_folder, f'{i:03d}.png'))

# Example usage
input_folder1 = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\OpacityTransition\\input_1"
input_folder2 = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\OpacityTransition\\input_2"
output_folder = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\OpacityTransition\\output"
create_transition(input_folder1, input_folder2, output_folder)
