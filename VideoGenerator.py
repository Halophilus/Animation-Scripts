import os
import tkinter as tk
from tkinter import filedialog, messagebox

from moviepy.editor import ImageSequenceClip, concatenate_videoclips
from PIL import Image


class VideoGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Video Generator and Concatenator")
        self.geometry("300x200")

        self.create_widgets()

    def create_widgets(self):
        self.folder_label = tk.Label(self, text="Folder:")
        self.folder_label.grid(row=0, column=0, padx=(10, 0), pady=(10, 0))

        self.folder_entry = tk.Entry(self)
        self.folder_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 0))

        self.file_label = tk.Label(self, text="Output file:")
        self.file_label.grid(row=1, column=0, padx=(10, 0), pady=(10, 0))

        self.file_entry = tk.Entry(self)
        self.file_entry.grid(row=1, column=1, padx=(0, 10), pady=(10, 0))
        self.file_entry.insert(0, "CLIP")

        self.generate_button = tk.Button(self, text="Generate", command=self.generate_video)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=(10, 0))

        self.browse_button = tk.Button(self, text="Browse", command=self.browse_folder)
        self.browse_button.grid(row=0, column=2, padx=(0, 10), pady=(10, 0))

        self.concatenate_button = tk.Button(self, text="Concatenate", command=self.concatenate_videos)
        self.concatenate_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))

    def browse_folder(self):
        folder = filedialog.askdirectory()
        self.folder_entry.delete(0, tk.END)
        self.folder_entry.insert(0, folder)

    def generate_video(self):
            folder = self.folder_entry.get()
            output_file = os.path.join(folder, f"{self.file_entry.get()}.mp4")

            # Filter out directories and non-.png files
            all_files = os.listdir(folder)
            image_files = [f for f in all_files if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith('.png')]

            # Sort image files, moving non-numeric file names to the end
            image_files = sorted(image_files, key=lambda x: int(os.path.splitext(x)[0]) if os.path.splitext(x)[0].isdigit() else float('inf'))

            # Convert images to RGB color mode
            rgb_images = []
            for img_file in image_files:
                img_path = os.path.join(folder, img_file)
                img = Image.open(img_path).convert("RGB")
                rgb_images.append(img)

            # Save converted images to a temporary folder
            temp_folder = os.path.join(folder, "temp")
            os.makedirs(temp_folder, exist_ok=True)
            temp_image_paths = [os.path.join(temp_folder, f"{i}.png") for i in range(len(rgb_images))]
            for img, temp_path in zip(rgb_images, temp_image_paths):
                img.save(temp_path)

            # Generate video from the temporary image sequence
            with ImageSequenceClip(temp_image_paths, fps=24) as clip:
                clip.write_videofile(output_file, codec='libx264rgb', audio=False)

            # Clean up the temporary folder
            for temp_path in temp_image_paths:
                os.remove(temp_path)
            os.rmdir(temp_folder)

            messagebox.showinfo("Success", "Video generated successfully!")



    def concatenate_videos(self):
        folder = self.folder_entry.get()
        output_file = os.path.join(folder, f"{self.file_entry.get()}.mp4")

        # Filter out directories and non-.mp4 files
        all_files = os.listdir(folder)
        video_files = [f for f in all_files if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith('.mp4')]

        # Sort video files, moving non-numeric file names to the end
        video_files = sorted(video_files, key=lambda x: int(os.path.splitext(x)[0]) if os.path.splitext(x)[0].isdigit() else float('inf'))

        # Load video clips
        from moviepy.editor import VideoFileClip
        clips = [VideoFileClip(os.path.join(folder, vf)) for vf in video_files]

        # Concatenate video clips
        final_clip = concatenate_videoclips(clips)

        # Write the concatenated video to the output file
        final_clip.write_videofile(output_file, codec='libx264rgb', audio=False)

        messagebox.showinfo("Success", "Videos concatenated successfully!")

if __name__ == "__main__":
    app = VideoGeneratorApp()
    app.mainloop()
