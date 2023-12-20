**Bootsequencer**

**Description:**
The "Bootsequencer" script is designed to generate a series of frames, each containing a portion of text, to create an animated boot sequence. It takes a text file as input and outputs a series of PNG image files, each containing a frame of the animation.

**Usage:**
To use the script, simply provide it with the necessary input parameters, such as the path to the input text file, the desired dimensions of the output frames, and the path to the output folder. Additional customization options are available, such as the font style, text color, background color, and typing indicator symbol.

Once the script is run, it will process the input text file, generating a series of frames that simulate the effect of text being typed out on a screen. The resulting image frames can be combined to create an animated sequence, either through a video editing program or another script.

**Key Features:**
- Generates animated "typing out" sequences from text files in the style of text-based boot sequences.
- Lines can appear all at once or one character at a time depending on if they contain an indicator character.
- Animation starts to marquee upwards once all available lines on the screen are occupied, creating room for subsequent lines.
- Customizable font style, text color, background color, and typing cursor.
- Outputs individual PNG frames for easy integration into video projects.

**How to Use:**
1. Modify the script to specify the following parameters:
   - Path to the input text file.
   - Desired dimensions of the output frames.
   - Path to the output folder where frames will be saved.
   - Customization options such as font style, text color, and background color.
2. Run the script using a Python interpreter.
3. The script will process the input text file and generate a series of PNG frames in the output folder.
4. Combine the frames to create an animated "typing out" effect.

---

**FRAMEDUPLICATOR**

**Description:**  
The "FRAMEDUPLICATOR" script offers a range of functions to manipulate image frames in a folder. These functions include duplicating, inserting, deleting, and randomizing frames. It also provides options to sort and rename frames by date and to adjust the total number of frames in a folder.

**Usage:**  
To utilize this script, run it, and a GUI will appear presenting various options and buttons. Select the appropriate folder or files, specify the parameters, and then execute the desired action by clicking the corresponding button.

**Key Features:**  
- Duplicate selected frames a specified number of times.
- Insert images from a folder into a destination folder at a specified index.
- Delete selected frames.
- Randomize duplicates within a specified range.
- Sort and rename frames by creation date.
- Adjust the total number of frames by deleting or duplicating to match a specified count.
- Reverse the order of frames within a folder.

**How to Use:**  
1. Run the script to open the GUI.
2. Select the folder or files for frame manipulation.
3. Specify the necessary parameters for the chosen function.
4. Click the corresponding button to execute the action.

---

**LoadingTiles**

**Description:**  
"LoadingTiles" generates a series of images that simulate the loading of input images, one set of tiles at a time. This creates an animated loading effect. The script offers control over tile progression, background color, and tile persistence.

**Usage:**  
To use this script, call `split_images_in_folder` with parameters for input and output folders, tile numbers, background color, sequence type, random tile range, and tile persistence.

**Key Features:**  
- Emulate loading animation for input images.
- Control over tile number, background color, and progression sequence.
- Options for sequential or random tile addition.
- Adjustable tile persistence across frames.

**How to Use:**  
1. Set the input and output folder paths.
2. Configure tile numbers (horizontal and vertical), background color, and sequence type. Leave None for transparent.
3. Run the script to process images in the input folder.
4. The output will be saved in the output folder, with subdirectories named after the original image files.

---

**TimelineMerger**

**Description:**  
"TimelineMerger" combines multiple folders of image sequences into a single master timeline, ensuring smooth transitions and no duplicate images. It requires a specific folder structure and naming convention for input images. The overlap transitions superimpose the advancing sequence of the last frames of the preceding sequence. The allows for the use of transparency to make transition animations between screens.

**Usage:**  
The script takes an input directory with single-digit serial numbered folders and an output directory. It also requires an `overlap_range` parameter to define transitions.

**Key Features:**  
- Merge multiple image sequences into a single timeline.
- Smooth transitions between sequences.
- Overlap range indicates number of transition frames that are superimposed from one sequence to the next
- No duplicate images in the output.

**How to Use:**  
1. Ensure input folders follow the required naming convention.
2. Specify the input directory, output directory, and overlap range.
3. Run the script to create the master timeline of merged images.

---
**FrameSuperimposer**

**Description:**  
"FrameSuperimposer" is designed for overlaying frames from two different sets of input directories. It allows for the combination of animations from corresponding subfolders, maintaining order and transparency.

**Usage:**  
This script requires four arguments: paste point, paths to two input directories, and an output directory.

**Key Features:**  
- Superimpose frames from two input directories.
- Maintain frame order and consider transparency.
- Create combined animation frames.

**How to Use:**  
1. Set the paste point coordinates.
2. Define the paths for the two input directories and the output directory representing the top and bottom layers in that order.
3. Run the script to combine frames and save them in the output directory.

---

**VideoDithering**

**Description:**  
"VideoDithering" applies a low fidelity, noisy appearance to video frames, mimicking the effect of Floyd-Steinberg dithering. It extracts frames from MP4 files, modifies them, and saves them as PNG images.

**Usage:**  
Replace the `input_folder` variable with the folder containing MP4 files, and run the script.

**Key Features:**  
- Process MP4 files to apply dithering.
- Modify frames for a lower fidelity, noisy appearance.
- Save modified frames as PNG images.

**How to Use:**  
1. Set the path to the folder containing MP4 files.
2. Run the script to process and save modified frames.
3. Adjust fidelity and noise via `color_palette_size` and `noise_intensity` parameters.

---

**VideoCropper**

**Description:**  
"VideoCropper.py" is a utility for cropping and trimming MP4 video files using FFmpeg. It allows specifying crop dimensions, crop position, and video trimming times.

**Usage:**  
Ensure FFmpeg is installed, set the paths for input and output files, and configure crop and trim settings.

**Key Features:**  
- Crop and trim MP4 video files.
- Customizable crop dimensions and position.
- Specify start and end times for trimming.

**How to Use:**  
1. Install FFmpeg and set it in the system's PATH.
2. Configure input and output file paths, crop dimensions, position, and trim times.
3. Run the script to apply cropping and trimming.

---

**VideoGenerator**

**Description:**  
"VideoGenerator" offers a GUI to create videos from PNG images and concatenate multiple videos. It processes frame named using a single-digit serial number convention.

**Usage:**  
Use the GUI to select folders, specify output file names, and choose between generating a video or concatenating existing ones.

**Key Features:**  
- Generate videos from PNG images.
- Concatenate multiple video files.
- User-friendly GUI interface.

**How to Use:**  
1. Open the GUI and browse for the folder containing PNG images or video files.
2. Enter the output file name.
3. Click "Generate" for video creation or "Concatenate" for merging videos.

---

**AddStatic**

**Description:**  
"AddStatic" applies Gaussian noise to a sequence of images in a folder, simulating the presence of noise in real-world images. It offers control over noise intensity.

**Usage:**  
Replace the paths in the script for the input and output folders, and adjust noise values.

**Key Features:**  
- Apply Gaussian noise to images.
- Adjustable noise intensity.
- Overwrite original images with noisy versions.

**How to Use:**  
1. Set input folder containing a set of frames to be randomly noised within a given range.
2. Adjust minimum and maximum noise values.
3. Run the script to apply noise to images.

---

**GlitchGenerator**

**Description:**  
"GlitchGenerator" creates glitchy images by combining frames using blending modes and offsets. It offers a randomized approach to make unpredictable animations, randomly overlaying images from the source folder over each other at variable transparency and saving them to an output folder.

**Usage:**  
Replace the output folder path in the script and set the number of glitched images to generate.

**Key Features:**  
- Randomly combine images for a glitch effect.
- Use blending modes and offsets.
- Create authentic-looking glitchy images.

**How to Use:**  
1. Set an input folder containing all template images to be glitched
2. Set the output folder path and number of glitched images.
3. Run the script to generate and save glitched images.

---

**MP4toColorFilteredFrames**

**Description:**  
This script converts a specific color in PNG images to transparency. It processes each image, replacing a target color with transparency. This was used in the scene with the nuclear attack simulation during the second act, as the animation was based on an existing model for a Mutually Assured Destruction (MAD) scenario between two political hegemonies.

**Usage:**  
Modify the script with the folder path, target color, and tolerance, then run it.

**Key Features:**  
- Replace a specific color with transparency.
- Process each image in a folder.
- Overwrite original images with modified versions.

**How to Use:**  
1. Set the IO folder path, target color, and tolerance.
2. Run the script to process and replace images.
3. Check the output folder for modified images.

---

**PSDFrameSuccessor**

**Description:**  
"PSDFrameSuccessor" monitors a folder for a specific file (e.g., "FRAME.png") and automatically renames it using a serial number that increments for every additional copy made. This serial number depends on the highest serial number already present as a frame in the root folder. This was used so that photos could be edited and saved as additional frames without filling out the naming convention manually.

**Usage:**  
Set the folder path, install the `watchdog` library, and run the script.

**Key Features:**  
- Monitor a folder for a specific file.
- Rename detected files using a serial number.
- Continuous operation until manually stopped.

**How to Use:**  
1. Set the folder path.
2. Run the script and monitor the folder for file renaming.

---

**ScreenFlickerer**

**Description:**  
"ScreenFlickerer" applies a CRT flickering effect to image sequences, altering color, brightness, and contrast. It simulates the affectations of an old CRT displayed and is applied to a set of frames for an authentic glitching effect.

**Usage:**  
Modify input and output folder paths, and set the effect intensity parameter.

**Key Features:**  
- Simulate CRT flickering effect.
- Adjustable color, brightness, and contrast.
- Process and save modified frames.

**How to Use:**  
1. Set input and output folder paths.
2. Adjust the effect intensity parameter.
3. Run the script to apply and save effects.

---

**FontSize**

**Description:**  
"FontSize" finds optimal font sizes without partially transparent pixels for a specified font and character set. This was used to determine what font sizes could be used on screen without looking blurry or resampled.

**Usage:**  
Set the font file path, character set, and font size range in the script.

**Key Features:**  
- Determine optimal font sizes.
- Avoid partially transparent pixels to emulate AMIGA-era raster graphics.
- Test across a range of font sizes.

**How to Use:**  
1. Set the font file path and character set.
2. Adjust font size range.
3. Run the script to find optimal sizes.

---

**LossEventMaker**

**Description:**  
"LossEventMaker" emulates the effect of video buffering by applying random quality loss to images and then gradually restoring quality. It's useful for simulating video streaming issues.

**Usage:**  
Run the script in a Python environment and input the necessary information when prompted, such as paths, loss factors, transition speed, and loss event indices.

**Key Features:**  
- Simulate video buffering and quality degradation.
- Random quality loss at specified or random indices.
- Gradual restoration of image quality.

**How to Use:**  
1. Run the script and input the required information.
2. Specify the path to the input and output folders, loss factors, transition speed, and loss event indices.
3. The script processes the images and saves the results in the output folder.

---

**OpacityTransition**

**Description:**  
"OpacityTransition" creates a smooth transition between two sets of image frames by adjusting the opacity. It matches the output frames to the larger set for a consistent transition.

**Usage:**  
Organize image sets into separate input folders and create an output folder. Configure the script with the paths to these folders and run it in a Python environment.

**Key Features:**  
- Smooth opacity transition between two image sets.
- Handle different numbers of frames in each set.
- Adjustable opacity for a visually appealing transition.

**How to Use:**  
1. Prepare input and output folders with image sets.
2. Configure the script with the folder paths.
3. Run the script to create the transition frames.

---

**StaticFrames**

**Description:**  
"StaticFrames" generates colored static noise frames with a defined resolution. It's useful for testing image or video processing algorithms and creating visual effects.

**Usage:**  
Set the number of frames, resolution, and output folder in the script, then run it using a Python interpreter.

**Key Features:**  
- Generate colored static noise frames.
- Customizable number of frames and resolution.
- Suitable for various applications like testing algorithms and creating effects.

**How to Use:**  
1. Configure the script with the desired number of frames, resolution, and output folder.
2. Run the script to generate and save the static noise frames.

---

**ZoomTiles**

**Description:**  
"ZoomTiles" creates a zooming animation effect on images. It generates frames showing the zooming process on a specific section of an image.

**Usage:**  
Set the input image, zoom coordinates, number of frames, dimensions of the zoom section, and output folder in the script.

**Key Features:**  
- Create a zooming animation effect.
- Customizable zoom coordinates, number of frames, and dimensions.
- Generate frames for video or GIF creation.

**How to Use:**  
1. Set the input image path, zoom coordinates, number of frames, zoom dimensions, and output folder.
2. Run the script to generate the zooming effect frames.
3. Use the frames for video or GIF creation.

---

**LoadingTilesVideo**

**Description:**  
"LoadingTilesVideo" is a Python script that progressively reveals video frames by showing them in small tiles. It supports both sequential and random tile revealing patterns, and can work with a range of settings like tile size, background color, and tile persistence. This script is ideal for creating scanline loading effects and retro animation/transition sequences.

**Usage:**  
To use this script, specify the input directory, tile dimensions, background color, sequential or random tile order, range of random tiles to reveal per frame, and tile persistence option. The script processes each frame in the input directory's subdirectories, revealing it tile by tile.

**Key Features:**  
- Progressively reveal video frames in tile format.
- Customizable tile size and background color.
- Option to reveal tiles sequentially or randomly.
- Control over the range of tiles revealed per frame.
- Ability to persist revealed tiles across frames.

**How to Use:**  
1. Modify the script to specify parameters:
   - Path to the input directory.
   - Tile dimensions (x for width, y for height).
   - Background color (optional, default: None for transparent).
   - Sequential or random tile revealing (default: True for sequential).
   - Range of random tiles to reveal per frame (optional, default: None).
   - Tile persistence across frames (default: True).
2. Run the script using a Python interpreter.
3. The script will process the frames in each subdirectory, saving the progressively revealed frames back to their original paths.

---

`Batch` versions of these script perform the task of the parent script for entire directories instead of just one output folder. For scripts such as FrameSuperimposeBatch will overlay all of the frames from several folders into a single set of output frames.
