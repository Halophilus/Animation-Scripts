import os
import textwrap
from PIL import Image, ImageDraw, ImageFont


def generate_frames(text_file, dimensions, font_path, lines_per_frame, output_folder,
                    typing_indicator='>', indent='    ',
                    bg_color=(0, 0, 0), font_color=(255, 255, 255), highlight_color=None):

    with open(text_file, 'r') as file:
        lines = file.readlines()

    font_size = dimensions[1] // lines_per_frame ##Switch this to dimension[1] // lines_per_frame for automatic scaling
    font = ImageFont.truetype(font_path, font_size)

    cursor_width = ImageDraw.Draw(Image.new('RGBA', (1, 1), color=(0, 0, 0, 0))).textsize('A', font=font)[0]

    chars_per_line = dimensions[0] // cursor_width

    frame_count = 1
    displayed_lines = []

    typed_frame_ranges = []  # Added to keep track of the ranges where text is being typed out
    current_typing_range = None

    def draw_frame(lines_to_draw, cursor_position=None):
        nonlocal frame_count
        img = Image.new('RGBA', dimensions, color=bg_color if bg_color else (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        y = 0
        for line_to_draw in lines_to_draw:
            if highlight_color:
                line_width, line_height = draw.textsize(line_to_draw, font=font)
                draw.rectangle([0, y, line_width, y + line_height], fill=highlight_color)
            draw.text((0, y), line_to_draw, font=font, fill=font_color)
            y += font_size

        if cursor_position and highlight_color:
            x_cursor = draw.textsize(cursor_position[0], font=font)[0]
            y_cursor = cursor_position[1] * font_size
            draw.rectangle([x_cursor, y_cursor, x_cursor + cursor_width, y_cursor + font_size], fill=(255,255,255))

        img.save(os.path.join(output_folder, f'{frame_count}.png'))
        frame_count += 1

    for line in lines:
        if line.strip() == "":
            displayed_lines.append("")
            if len(displayed_lines) > lines_per_frame:
                displayed_lines.pop(0)
            draw_frame(displayed_lines)
            continue

        wrapped_lines = textwrap.wrap(line.strip(), width=chars_per_line)
        wrapped_lines = [wrapped_lines[0]] + [indent + l for l in wrapped_lines[1:]]

        if typing_indicator in line:
                if current_typing_range:
                    typed_frame_ranges.append((current_typing_range, frame_count - 1))
                    current_typing_range = None
                for wrapped_line in wrapped_lines:
                    typed_line = ''
                    for char in wrapped_line:
                        typed_line += char
                        if len(typed_line.strip()) == 1:
                            displayed_lines.append(typed_line)
                        else:
                            displayed_lines[-1] = typed_line
                            if len(typed_line) >= chars_per_line:
                                displayed_lines.append('')
                        if len(displayed_lines) > lines_per_frame:
                            displayed_lines.pop(0)
                        draw_frame(displayed_lines, cursor_position=(typed_line, len(displayed_lines) - 1))
                    for _ in range(3):  # Blink the cursor three times
                        draw_frame(displayed_lines)
                        draw_frame(displayed_lines, cursor_position=(typed_line, len(displayed_lines) - 1))
        else:
                if not current_typing_range:
                    current_typing_range = frame_count
                for wrapped_line in wrapped_lines:
                    displayed_lines.append(wrapped_line)
                    if len(displayed_lines) > lines_per_frame:
                        displayed_lines.pop(0)
                    draw_frame(displayed_lines)

    if current_typing_range:
        typed_frame_ranges.append((current_typing_range, frame_count - 1))

    for _ in range(lines_per_frame):
        displayed_lines.pop(0)
        draw_frame(displayed_lines)

    print(typed_frame_ranges)


if __name__ == '__main__':
    text_file = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\BootSequencer\\SEQ 3\\A.txt"
    dimensions = (640, 480)
    font_path = "C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\BootSequencer\\PrintChar21.ttf"
    lines_per_frame = 30
    typing_indicator = 'O'
    output_folder = 'C:\\Users\\Thomas.Henshaw001\\Development\\ImageVideoManipulator\\Animation Scripts\\BootSequencer\\frames'

    bg_color = (0,0,0)  # Example background color
    font_color = (255, 255, 255)  # Example font color
    highlight_color = (0, 0, 0)  # Example highlight color

    generate_frames(text_file, dimensions, font_path, lines_per_frame, output_folder,
                    typing_indicator='LOADING SHUTDOWN SEQUENCE...', indent='',
                    bg_color=bg_color, font_color=font_color, highlight_color=highlight_color)
