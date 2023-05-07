from PIL import Image, ImageDraw, ImageFont
from decimal import Decimal, getcontext

getcontext().prec = 4

def has_partially_transparent_pixels(image):
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.getpixel((x, y))
            if 0 < pixel[3] < 255:
                return True
    return False

def find_font_sizes_without_partial_transparency(font_path, char_set, min_size, max_size, increment):
    font_sizes_without_partial_transparency = []
    total_iterations = (max_size - min_size) / increment
    current_iteration = 1

    size = min_size
    try:
        while size <= max_size:
            print(f"Checking size {size} ({current_iteration}/{total_iterations})")
            font = ImageFont.truetype(font_path, int(round(size)))
            max_width = max([font.getbbox(c)[2] for c in char_set])
            max_height = max([font.getbbox(c)[3] for c in char_set])

            image = Image.new('RGBA', (max_width, max_height), (255, 255, 255, 0))
            draw = ImageDraw.Draw(image)

            for c in char_set:
                draw.text((0, 0), c, font=font, fill=(0, 0, 0, 255))

            if not has_partially_transparent_pixels(image):
                font_sizes_without_partial_transparency.append(float(size))
                print(f"Size {size} has no partially transparent pixels.")

            size += increment
            current_iteration += 1
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Printing font sizes tested so far...")

    return font_sizes_without_partial_transparency


font_path = "C:\\Users\\Thomas.Henshaw001\\Downloads\\oldschool_pc_font_pack_v2.2_FULL\\ttf - Px (pixel outline)\\PxPlus_IBM_XGA-AI_12x20.ttf"
char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
min_size, max_size = Decimal('30.00'), Decimal('80.00')
increment = Decimal('0.01')

result = find_font_sizes_without_partial_transparency(font_path, char_set, min_size, max_size, increment)
print(f"Font sizes without partially transparent pixels: {result}")
