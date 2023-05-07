import os
from PIL import Image

def generate_zoom_frames(input_image, coord, num_frames, dimensions):
    # Load the image
    img = Image.open(input_image)

    # Get the original image dimensions
    img_width, img_height = img.size
    center_x, center_y = img_width // 2, img_height // 2

    # Calculate the size of the final zoomed section
    final_zoom_width, final_zoom_height = dimensions

    # Define the zoom section in the original image
    x, y = coord
    section = img.crop((x, y, x + final_zoom_width, y + final_zoom_height))

    # Generate zoom frames
    frames = []
    for i in range(num_frames + 1):
        # Calculate scaling factor for the current frame
        scale_factor = i / num_frames

        # Resize the zoom section for the current frame
        current_width = int((1 - scale_factor) * final_zoom_width + scale_factor * img_width)
        current_height = int((1 - scale_factor) * final_zoom_height + scale_factor * img_height)
        current_section = section.resize((current_width, current_height), Image.ANTIALIAS)

        # Calculate the current position of the zoomed section
        current_x = int((1 - scale_factor) * x + scale_factor * (center_x - current_width // 2))
        current_y = int((1 - scale_factor) * y + scale_factor * (center_y - current_height // 2))

        # Paste the current section onto the original image background
        frame = img.copy()
        frame.paste(current_section, (current_x, current_y, current_x + current_width, current_y + current_height))
        frames.append(frame)

    return frames


input_image = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\ZoomTiles\\1.png"
coord = (175, 115)
num_frames = 5
dimensions = (283, 169)
output_folder = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\ZoomTiles\\output"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

frames = generate_zoom_frames(input_image, coord, num_frames, dimensions)

# Save generated frames
for i, frame in enumerate(frames):
    frame.save(os.path.join(output_folder, f"{i}.png"))
