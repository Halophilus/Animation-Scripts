from PIL import Image

def generate_zoom_frames(input_image, coord, num_frames, dimensions):
    # Load the image
    img = Image.open(input_image)

    # Get the original image dimensions
    img_width, img_height = img.size

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

        # Paste the current section onto the original image background
        frame = img.copy()
        frame.paste(current_section, (x, y, x + current_width, y + current_height))
        frames.append(frame)

    return frames

input_image = "input_image.jpg"
coord = (100, 100)
num_frames = 3
dimensions = (200, 200)

frames = generate_zoom_frames(input_image, coord, num_frames, dimensions)

# Save generated frames
for i, frame in enumerate(frames):
    frame.save(f"frame_{i}.jpg")
