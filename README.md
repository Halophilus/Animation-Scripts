**Bootsequencer**

**Description:**
The "Bootsequencer" script is designed to generate a series of frames, each containing a portion of text, to create an animated "typing out" effect. It takes a text file as input and outputs a series of PNG image files, each containing a frame of the animation.

**Usage:**
To use the script, simply provide it with the necessary input parameters, such as the path to the input text file, the desired dimensions of the output frames, and the path to the output folder. Additional customization options are available, such as the font style, text color, background color, and typing indicator symbol.

Once the script is run, it will process the input text file, generating a series of frames that simulate the effect of text being typed out on a screen. The resulting image frames can be combined to create an animated sequence, either through a video editing program or another script.

**Key Features:**
- Generates animated "typing out" sequences from text files.
- Customizable font style, text color, background color, and typing indicator.
- Outputs individual PNG frames for easy integration into video projects.

**How to Use:**
1. Modify the script to specify the following parameters:
   - Path to the input text file.
   - Desired dimensions of the output frames.
   - Path to the output folder where frames will be saved.
   - Customization options such as font style, text color, and background color.

2. Run the script using a Python interpreter.

3. The script will process the input text file and generate a series of PNG frames in the output folder.

4. Combine the frames to create an animated "typing out" effect using video editing software or other tools.

**REMAINING SCRIPTS**
**FRAMEDUPLICATOR**
    Duplicate frames: Duplicates the selected frames a specified number of times and optionally jumbles them randomly.
    Insert images: Inserts images from the selected folder into a destination folder at a specified index.
    Delete frames: Deletes the selected frames from the folder.
    Randomize duplicates: Creates random duplicates of frames within a specified range.
    Sort and rename by date: Sorts and renames frames based on their creation date.
    Adjust frames: Adjusts the total number of frames in a folder by either randomly deleting or duplicating frames to match the specified count.
    Reverse frames: Reverses the order of frames within a folder based on their naming convention.

To use the script, run it, and the GUI will provide you with the necessary options and buttons to perform each function. Select the appropriate folder or files, specify the required parameters, and then click the corresponding button to execute the desired action.

**LoadingTiles**
This script generates a series of images that emulate the loading of input images one set of tiles at a time, creating a loading animation effect. Each frame of the output images progressively adds tiles to the canvas, either sequentially (left-to-right, top-to-bottom) or randomly, depending on the given parameters. You can also control whether the tiles persist in the subsequent frames or only appear in the current frame.

To use the script, call the split_images_in_folder function with the following parameters:

    input_folder: Path to the folder containing the input images.
    x: Number of tiles that fit in the image horizontally.
    y: Number of tiles that fit in the image vertically.
    output_dir: Path to the output directory (optional, default: "output").
    background_color: RGB color for the background canvas, or None for a transparent background (optional, default: None).
    sequential: If True, tiles are added sequentially (left-to-right, top-to-bottom); if False, tiles are added randomly (optional, default: True).
    random_tiles_range: Tuple (min, max) indicating the range of tiles to be added per frame (optional, default: None).
    persist_tiles: If True, tiles carry over to the next frame; if False, each frame shows only the tiles loaded in that frame (optional, default: True).

The script processes all images in the input folder and saves the resulting tile loading animation frames in subdirectories within the output folder, named after the original image files.

**TimelineMerger**

This function combines multiple folders containing image sequences into a single master timeline with smooth transitions between each sequence. The function takes an input directory containing folders with single-digit serial number naming conventions and an output directory for saving the merged images. It also takes an overlap_range parameter to define the number of overlapping frames between consecutive image sequences. The script ensures that there are no duplicate images in the output, and each frame occurs only once.

**FrameSuperimposer**
This script is designed to superimpose frames from two sets of input directories containing animation frames organized in subfolders. The purpose of the script is to combine frames from corresponding subfolders in the input directories, allowing users to overlay animations and create a new set of combined animation frames. The script maintains the order of the frames and considers transparency, so the output frames will show the corresponding sections from the background images after superimposition.

To use the script, you need to provide four arguments:

    paste_point: A tuple of two numbers (x, y) representing the coordinates of the upper-left corner where the frames from the first input directory will be pasted onto the frames from the second input directory.

    input_folder_1: The path to the first input directory, containing the images to be pasted onto the frames from the second input directory. The directory should have subfolders with sequentially numbered frame files (e.g., 1.png, 2.png, 3.png).

    input_folder_2: The path to the second input directory, containing the background images on which the images from the first input directory will be pasted. The directory should have subfolders with sequentially numbered frame files, similar to the first input directory.

    output_folder: The path to the output directory, where the combined frames will be saved in subfolders corresponding to the input subfolders. The output frames will be named sequentially, e.g., 1.png, 2.png, 3.png.

**VideoDithering**
This script processes a folder containing MP4 video files, applying a lower fidelity appearance to each frame with increased noise and a reduced color palette. The script extracts the frames from the input videos, modifies them using the specified dithering method (Floyd-Steinberg dithering), and saves the resulting frames as PNG images in an output folder named after the input video file.

To use this script:

    Replace the input_folder variable with the path to the folder containing your MP4 video files.
    Run the script, and it will process all the MP4 files in the specified folder.
    The output frames will be saved as PNG images in subfolders named after the input video files, located within the input folder.

You can adjust the fidelity and noise of the output frames by modifying the color_palette_size and noise_intensity parameters in the apply_random_dithering function. Lower values for color_palette_size will result in fewer colors in the output frames, while higher values for noise_intensity will increase the noise level in the output frames.

**VideoCropper**
This script, VideoCropper.py, is a Python utility for cropping and trimming MP4 video files. It uses FFmpeg to perform the video processing and allows users to specify the crop dimensions, the position of the cropped area (center, left, right, top, or bottom), and the start and end times for trimming the video. The output video will be saved with the specified crop and trimmed duration.

Usage:

    Make sure FFmpeg is installed on your system and added to the system's PATH variable.
    Modify the input_file and output_file variables in the script with the paths to the input and output video files.
    Set the crop_width and crop_height variables to the desired dimensions of the cropped area.
    Set the position variable to one of the following strings: 'center', 'left', 'right', 'top', or 'bottom'.
    Set the start_time variable to the desired start time in the format "HH:MM:SS".
    Set the end_time variable to the desired duration in the format "HH:MM:SS".
    Run the script with Python. The output video will be saved to the specified location with the cropped and trimmed settings applied.

**VideoGenerator**
This script provides a simple GUI to generate video files from a series of PNG images and concatenate multiple video files in a specified order. The images and videos should be named using a single-digit serial number naming convention (e.g., "1.png", "2.png", "1.mp4", "2.mp4", etc.) and will be processed in that order.
Features

    Generate a video from a folder containing PNG images, ordered by their single-digit serial number naming convention.
    Convert PNG images to a common format (RGB) to avoid codec issues.
    Save the generated video to the same folder containing the source images.
    Concatenate multiple videos located in a single folder, ordered by their single-digit serial number naming convention.
    Save the concatenated video to the same folder containing the source videos.

How to use

    Use the "Browse" button to select the folder containing the PNG images or video files you wish to process.
    Enter the desired name for the output file in the "Output file" field (default is "CLIP").
    Click the "Generate" button to generate a video from the PNG images in the selected folder.
    Click the "Concatenate" button to concatenate the video files in the selected folder.


**Bootsequencer**
This script is designed to generate a series of frames, each containing a portion of text, to create an animated "typing out" effect. It takes a text file as input, and outputs a series of PNG image files, each containing a frame of the animation.

To use the script, simply provide it with the necessary input parameters, such as the path to the input text file, the desired dimensions of the output frames, and the path to the output folder. Additional customization options are available, such as the font style, text color, background color, and typing indicator symbol.

Once the script is run, it will process the input text file, generating a series of frames that simulate the effect of text being typed out on a screen. The resulting image frames can be combined to create an animated sequence, either through a video editing program or another script.

**LossEventMaker**
The purpose of this script is to emulate the effect of video resampling that occurs while a video is buffering, followed by a gradual return to the original quality. The script processes a sequence of images (frames), applying random quality loss (downsampling) at specified or random indices (loss events), and then gradually restoring the quality in subsequent images.

How to use it:

    Run the script in a Python environment (e.g., via the command line or an IDE).
    When prompted, enter the following information:
        The path to the folder containing the input images in sequential order (e.g., 0.png, 1.png, 2.png, ...).
        The path to the output folder, where the processed images will be saved.
        The minimum loss factor (a float between 0 and 1) representing the smallest amount of quality loss applied to the images during a loss event.
        The maximum loss factor (a float between 0 and 1) representing the largest amount of quality loss applied to the images during a loss event. The max_loss should be greater than or equal to min_loss.
        The transition speed (a positive float) controlling the rate at which the image quality transitions back to the original quality after a loss event. Higher values result in a faster transition, while lower values result in a slower transition.
        Whether to use random loss events (by typing 'yes' or 'no'). If you choose 'no', you'll be prompted to enter a list of indices for the loss events, separated by spaces.
    The script will process the images and save the results in the specified output folder.

This script is useful for simulating the effect of video buffering and quality degradation, as well as the subsequent restoration of quality, which can be helpful for testing video streaming algorithms, compression techniques, or for creating video effects in post-production.

**OpacityTransition**
This Python script creates a smooth transition between two sets of image frames by gradually reducing the opacity of the first set of frames and overlaying them onto the second set of frames. The resulting images show the second set of frames fading in from the first set, providing a visually appealing transition between the two sets. The script is designed to handle image sets with different numbers of frames by matching the output frames to the larger set.

How to Use:

    Prepare your input and output folders: Organize your image sets into two separate input folders (input_folder1 and input_folder2) and create an output folder where the transition frames will be saved.

    Configure the script: Replace 'path/to/your/input_folder1', 'path/to/your/input_folder2', and 'path/to/your/output_folder' in the script with the paths to your input and output folders.

    Run the script: Execute the script using your preferred Python environment. The script will read the images from the input folders, create a smooth transition by adjusting the opacity of the first set of frames, and save the resulting images in the output folder.

    Review the output: Check the output folder for the generated transition frames. The transition should appear smooth, with the second set of frames gradually revealed at a rate of (100 / number of output frames)% per frame.

**StaticFrames**
The purpose of this Python script is to generate a specified number of colored static noise frames with a defined resolution and save them to an output folder. The static noise is a random assortment of colors, rather than just black and white.

To use this script:

    Set the num_frames, resolution, and output_folder variables in the script according to your requirements:
        num_frames: The number of static noise frames you want to generate.
        resolution: A tuple (width, height) representing the desired frame resolution.
        output_folder: The folder where the generated frames will be saved.

    Run the script using a Python interpreter. The script will create the specified number of colored static noise frames with the defined resolution and save them as PNG files in the output folder.

The generated frames can be used in various applications such as testing image or video processing algorithms, creating visual effects, simulating sensor noise, or any other use case where random colored noise images are required.

**ZoomTiles**
The purpose of this script is to create a zooming animation effect on a given image by generating a series of frames that display the zooming process. The script takes an input image, a pixel coordinate representing the top-left corner of the section to be zoomed in, the number of frames to be generated for the zooming effect, and the dimensions of the rectangular section to be zoomed in.

The script first loads the input image and calculates the original dimensions of the image. It then crops the section to be zoomed in based on the provided coordinate and dimensions. It generates the zoom frames by resizing the section, moving it towards the center of the image, and pasting it onto the original image background for each frame.

To use the script, set the input_image variable to the path of the image you want to create the zooming animation for. Set the coord variable to the pixel coordinate of the top-left corner of the section to be zoomed in. Set the num_frames variable to the number of frames you want to generate for the zooming animation. Set the dimensions variable to the dimensions of the rectangular section to be zoomed in. Finally, set the output_folder variable to the path where you want to save the generated frames.

The script will create the output folder if it doesn't exist, generate the frames with the zooming effect, and save them in the output folder. The frames can be further processed to create a video or GIF using other tools or libraries.

**AddStatic**
The purpose of this script is to apply Gaussian noise with a random intensity to all images within a specified folder. Gaussian noise is a type of noise that follows a Gaussian distribution and is often used to simulate or model the presence of noise in real-world images.

To use the script:

    Copy the script into a new Python file, e.g., add_gaussian_noise.py.

    Replace the input_folder and output_folder paths in the script with the appropriate directories for your images. The input_folder should contain the images you want to apply noise to, and the output_folder is where the script will save the noisy images.

    Adjust the min_noise and max_noise values as needed. These values represent the acceptable range of standard deviation for the Gaussian noise applied to the images. A higher value will result in more noise.
The script will iterate through all image files (with '.png', '.jpg', or '.jpeg' extensions) in the input_folder, apply Gaussian noise with a random standard deviation within the specified range, and save the noisy images in the output_folder. The script will also print the standard deviation of noise applied to each image during processing.

**GlitchGenerator**
The purpose of this script is to create a series of glitchy images by combining frames from a set of input images. The script takes an input folder containing image frames, an output folder to save the generated glitched images, and a number specifying how many glitched images to create.

The script works by randomly selecting pairs of images from the input folder, resizing them to the same dimensions, and converting them to the same mode (RGB). It then combines the images using different blending modes and offsets to create a glitchy appearance. The script also applies additional glitch-like effects such as shifting image content or using other blending modes to further enhance the glitchy look. The randomness in the selection of images and effect parameters ensures that the output images have an authentic, corrupted appearance.

To use the script:

    Replace the output_folder variable with the path to the folder where you want to save the generated glitched images. If the folder doesn't exist, the script will create it.
    Set the num_output_images variable to the desired number of glitched images you want to generate.
    Run the script. The generated glitched images will be saved in the specified output folder with names in the format glitched_{i}.png, where i is a unique index.

You can adjust the parameters within the script for different glitch effects, such as the scale, offset, or blending mode.

**MP4toColorFilteredFrames**
This script is designed to convert a specific color in a folder of PNG images to transparency. It processes each image in the folder, replaces the specified color with a transparent color, and overwrites the original images with the modified versions.

How to use:

    Save the script as a Python file, e.g., color_to_transparency.py.
    Modify the folder_path, target_color, and tolerance variables within the script according to your needs:
        folder_path: Replace path/to/your/folder with the actual folder path containing the PNG images.
        target_color: Replace with your target RGB color (e.g., (0, 0, 0) for black).
        tolerance: Replace with your desired tolerance value (e.g., 0 for an exact color match).
    Run the script using a terminal or command prompt. The script will process each image in the specified folder, replacing the target color with transparency, and print out information about the processed images.
    After the script completes, the original images in the folder will be replaced with the modified versions.

Note: Since the script overwrites the original images, it is recommended to create a backup of the images before running the script to avoid any loss of data.

**PSDFrameSuccessor**
The purpose of this script is to monitor a specified folder for the appearance of a specific file, named "FRAME.png". When a new instance of the "FRAME.png" file is detected in the folder, the script will rename it using a 1-digit serial number (e.g., "1.png", "2.png", etc.). The script will keep running and monitoring the folder until it is manually stopped by the user.

How to use it:

    Replace the "C:/path/to/your/folder" in the script with the actual path to the folder you want to monitor. Make sure to use forward slashes (/) as path separators instead of backslashes ().
    Ensure that the watchdog library is installed using pip: pip install watchdog.
    Run the script using a Python interpreter. You can run it using the command line by navigating to the folder containing the script and running python script_name.py (replace script_name.py with the actual name of the script file).
    The script will continuously monitor the specified folder. When a new instance of the "FRAME.png" file appears in the folder, the script will rename it using a 1-digit serial number.
    To stop the script, press Ctrl+C in the command prompt or terminal where the script is running.

**ScreenFlickerer**
This script applies a CRT flickering effect to a sequence of images by randomly altering the color, brightness, and contrast within a specified range of effect intensities. The script takes an input folder containing low-resolution frames, processes each frame, and saves the modified frames to an output folder.

Here's how to use the script:

    Modify the following variables in the script to suit your needs:
        input_folder: The path to the folder containing your input frames.
        output_folder: The path where you want the modified frames to be saved.
        relative_parameter: A float value between 0 and 1 (inclusive) that determines the range of effect intensities for color, brightness, and contrast adjustments. A higher value results in more intense effects.

    Run the script using the command python crt_flicker_effect.py. This will process the images in the input folder and save the modified frames to the output folder.

Please note that this script only processes and saves the modified frames. To compile the modified frames into an animation, you will need to use a separate tool or library like OpenCV or ImageMagick.

**FontSize**
This script is designed to find font sizes without partially transparent pixels for a given font and character set. It uses the Python Pillow library for image manipulation to render characters in different font sizes and checks whether there are any partially transparent pixels in the rendered images.

To use the script, follow these steps:

    Replace 'path/to/your/font_file.ttf' in the script with the actual path to the font file you want to use.
    Modify the char_set variable if you want to use a different set of characters for testing.
    Set the min_size and max_size variables to the desired range of font sizes you want to test.
    Run the script using a Python interpreter, for example: python your_script_name.py

The script will iterate through font sizes in the specified range with an increment of 0.01 (to the nearest hundredth place) and check whether there are any partially transparent pixels in the rendered images. When the script finishes or is interrupted using a keyboard interrupt (Ctrl+C), it will print the font sizes without partially transparent pixels found so far.
