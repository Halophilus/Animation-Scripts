import os
import random
from PIL import Image

def split_image(image_path, x, y, output_dir="output", background_color=None, sequential=True, random_tiles_range=None, persist_tiles=True):
    # Load the image
    img = Image.open(image_path).convert('RGBA')
    img_width, img_height = img.size

    # Calculate the tile dimensions
    tile_width = img_width // x
    tile_height = img_height // y

    # Create a background canvas for the output images
    if background_color is None:
        black_canvas = Image.new('RGBA', (img_width, img_height), (0, 0, 0, 0))
    else:
        black_canvas = Image.new('RGBA', (img_width, img_height), background_color)

    # Generate a list of tiles
    tiles = [(i * tile_width, j * tile_height, (i + 1) * tile_width, (j + 1) * tile_height)
             for i in range(x) for j in range(y)]

    # If not sequential, shuffle the tile list
    if not sequential:
        random.shuffle(tiles)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    canvas = black_canvas.copy()
    remaining_tiles = tiles.copy()
    frame_count = 0

    while remaining_tiles:
        if random_tiles_range:
            tiles_to_add = random.randint(random_tiles_range[0], random_tiles_range[1])
        else:
            tiles_to_add = 1

        for _ in range(tiles_to_add):
            if remaining_tiles:
                tile = remaining_tiles.pop(0)
                canvas.paste(img.crop(tile), (tile[0], tile[1]), img.crop(tile))

        canvas.save(os.path.join(output_dir, f"{frame_count + 1}.png"), "PNG")
        frame_count += 1

        if not persist_tiles:
            canvas = black_canvas.copy()

def split_images_in_folder(input_folder, x, y, output_dir="output", background_color=None, sequential=True, random_tiles_range=None, persist_tiles=True):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_path = os.path.join(input_folder, filename)
            image_output_dir = os.path.join(output_dir, os.path.splitext(filename)[0])

            split_image(image_path, x, y, image_output_dir, background_color, sequential, random_tiles_range, persist_tiles)

if __name__ == '__main__':
    output_dir = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\LoadingTiles\\output"
    image_path = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\LoadingTiles\\50.png"
    input_folder = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\LoadingTiles\\input"
    x = 80
    y = 60
    background_color = None
    sequential = True
    random_tiles_range = (500, 600)
    persist_tiles = True

    #split_image(image_path, x, y, output_dir, background_color, sequential, random_tiles_range, persist_tiles)
    split_images_in_folder(input_folder, x, y, output_dir, background_color, sequential, random_tiles_range, persist_tiles)
