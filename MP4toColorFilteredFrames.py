import os
from PIL import Image

def convert_color_to_transparency(folder_path, target_color, tolerance=0):
    for file_name in os.listdir(folder_path):
        try:
            if file_name.endswith(".png"):
                file_path = os.path.join(folder_path, file_name)
                image = Image.open(file_path)

                if image.mode in ("RGBA", "P"):
                    image = image.convert("RGBA")
                else:
                    print(f"Skipped '{file_name}' due to unsupported mode: {image.mode}")
                    continue

                data = image.getdata()
                new_data = []

                for item in data:
                    if (abs(item[0] - target_color[0]) <= tolerance and
                        abs(item[1] - target_color[1]) <= tolerance and
                        abs(item[2] - target_color[2]) <= tolerance):
                        new_data.append((255, 255, 255, 0))
                    else:
                        new_data.append(item)

                image.putdata(new_data)
                image.save(file_path, "PNG")
                print(f"Converted '{file_name}'")
            else:
                print(f"Skipped '{file_name}' due to unsupported file type")
        except Exception as e:
            print(f"Error processing '{file_name}': {e}")

# Assign the variables here
folder_path = "C:\\Users\\Thomas.Henshaw001\\Documents\\Art 481\\Art\\SEQUENCE 2\\Nuclear Attack Animation\\Fallout Map"
target_color = (0, 0, 0)  # Replace with your target RGB color
tolerance = 3  # Replace with your desired tolerance value

convert_color_to_transparency(folder_path, target_color, tolerance)
print("Color conversion completed!")
