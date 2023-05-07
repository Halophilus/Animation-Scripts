import os
import random
from PIL import Image

def reveal_video_frames(input_dir, x, y, background_color=None, sequential=True, random_tiles_range=None, persist_tiles=True):
    # Get the list of subdirectories
    subdirs = [d for d in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, d))]

    for subdir in subdirs:
        subdir_path = os.path.join(input_dir, subdir)
        
        # Sort frame files based on their numerical values
        frame_files = sorted(os.listdir(subdir_path), key=lambda x: int(os.path.splitext(x)[0]))

        # Generate a list of tiles
        tiles = [(i, j) for i in range(x) for j in range(y)]

        # If not sequential, shuffle the tile list
        if not sequential:
            random.shuffle(tiles)

        # Initialize the revealed_tiles
        revealed_tiles = set()

        for idx, frame_name in enumerate(frame_files):
            frame_path = os.path.join(subdir_path, frame_name)
            img = Image.open(frame_path).convert('RGBA')
            img_width, img_height = img.size
            tile_width = img_width // x
            tile_height = img_height // y

            if background_color is None:
                canvas = Image.new('RGBA', (img_width, img_height), (0, 0, 0, 0))
            else:
                canvas = Image.new('RGBA', (img_width, img_height), background_color)

            if idx < (x * y):
                if random_tiles_range:
                    tiles_to_add = random.randint(random_tiles_range[0], random_tiles_range[1])
                else:
                    tiles_to_add = 1

                for _ in range(tiles_to_add):
                    if len(revealed_tiles) < x * y:
                        tile = tiles.pop(0)
                        revealed_tiles.add(tile)

            for i, j in revealed_tiles:
                tile = (i * tile_width, j * tile_height, (i + 1) * tile_width, (j + 1) * tile_height)
                canvas.paste(img.crop(tile), (tile[0], tile[1]), img.crop(tile))

            canvas.save(frame_path, "PNG")

            if len(revealed_tiles) == x * y:
                break

if __name__ == '__main__':
    input_dir = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\Test Frames\\LoadingTilesVideo\\input"
    x = 40
    y = 30
    background_color = None
    sequential = False
    random_tiles_range = (0, 120)
    persist_tiles = True
    reveal_video_frames(input_dir, x, y, background_color, sequential, random_tiles_range, persist_tiles)

