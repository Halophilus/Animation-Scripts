import os
import shutil
import random
import tempfile
from tkinter import (Tk, StringVar, BooleanVar, Entry, Label, Button, Checkbutton,
                     messagebox, filedialog, Toplevel)
from tkinter.ttk import Separator
import time



def show_tooltip(event, tooltip_text):
    tooltip = Toplevel(root)
    tooltip.wm_overrideredirect(True)
    tooltip.wm_geometry(f"+{event.x_root + 20}+{event.y_root + 20}")
    label = Label(tooltip, text=tooltip_text, background="white")
    label.pack()
    event.widget.tooltip = tooltip


def hide_tooltip(event):
    if hasattr(event.widget, 'tooltip'):
        event.widget.tooltip.destroy()
        del event.widget.tooltip

def browse_folder():
    file_paths = filedialog.askopenfilenames(filetypes=[("PNG Files", "*.png")])
    selected_files.set(", ".join(file_paths))

def browse_folder_path():
    folder_path = filedialog.askdirectory()
    folder_path_var.set(folder_path)

def duplicate_frames():
    files = selected_files.get().split(", ")
    duplicates = int(duplicates_var.get()) - 1
    jumble = jumble_var.get()

    if duplicates > 0:
        start_frame = min(files, key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))
        end_frame = max(files, key=lambda x: int(os.path.splitext(os.path.basename(x))[0]))

        folder_path = os.path.dirname(start_frame)
        os.chdir(folder_path)

        start_frame_number = int(os.path.splitext(os.path.basename(start_frame))[0])
        end_frame_number = int(os.path.splitext(os.path.basename(end_frame))[0])

        # Shift frames after the duplicated sequence
        all_frames = [f for f in os.listdir(folder_path) if f.endswith('.png')]
        all_frames.sort(key=lambda f: int(os.path.splitext(f)[0]), reverse=True)
        for frame in all_frames:
            frame_number = int(os.path.splitext(frame)[0])
            if frame_number > end_frame_number:
                new_frame_number = frame_number + (end_frame_number - start_frame_number + 1) * duplicates
                os.rename(frame, f"{new_frame_number}.png")

        # Duplicate the frames
        for i in range(end_frame_number, start_frame_number - 1, -1):
            for _ in range(1, duplicates + 1):
                if f"{i}.png" in all_frames:
                    src = f"{i}.png"
                    dst = f"{i + (end_frame_number - start_frame_number + 1) * _}.png"
                    shutil.copy2(src, dst)

    if jumble:
        all_frames = [f for f in os.listdir(folder_path) if f.endswith('.png')]
        random.shuffle(all_frames)
        for idx, frame in enumerate(all_frames, start=1):
            src = frame
            dst = f"{idx}.png"
            shutil.move(src, dst)

def reverse_frames():
    folder_path = folder_path_var.get()
    all_frames = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    all_frames.sort(key=lambda f: int(os.path.splitext(f)[0]))

    # Calculate the total number of frames
    num_frames = len(all_frames)

    # Iterate through half of the frames and swap the frame names
    for i in range(num_frames // 2):
        frame_a = all_frames[i]
        frame_b = all_frames[num_frames - i - 1]

        # Temporary file name for swapping
        tmp_name = f"tmp_{i}.png"

        # Swap frames using a temporary file
        frame_a_path = os.path.join(folder_path, frame_a)
        frame_b_path = os.path.join(folder_path, frame_b)
        tmp_path = os.path.join(folder_path, tmp_name)

        os.rename(frame_a_path, tmp_path)
        os.rename(frame_b_path, frame_a_path)
        os.rename(tmp_path, frame_b_path)


def adjust_frames():
    folder_path = folder_path_var.get()
    desired_frames = int(desired_frames_var.get())

    all_frames = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    all_frames.sort(key=lambda f: int(os.path.splitext(f)[0]))

    if desired_frames > len(all_frames):
        while len(all_frames) < desired_frames:
            src = random.choice(all_frames)
            src_path = os.path.join(folder_path, src)
            frame_number = int(os.path.splitext(src)[0])

            # Find the index to insert the duplicate frame
            insert_idx = all_frames.index(src) + 1

            # Rename frames in reverse order to make space for the duplicate frame
            for i in range(len(all_frames), insert_idx, -1):
                old_frame_path = os.path.join(folder_path, all_frames[i - 1])
                new_frame_number = int(os.path.splitext(all_frames[i - 1])[0]) + 1
                new_frame_path = os.path.join(folder_path, f"{new_frame_number}.png")
                os.rename(old_frame_path, new_frame_path)

            # Duplicate the frame
            dst_path = os.path.join(folder_path, f"{frame_number + 1}.png")
            shutil.copy2(src_path, dst_path)

            # Update the all_frames list after duplication
            all_frames = [f for f in os.listdir(folder_path) if f.endswith('.png')]
            all_frames.sort(key=lambda f: int(os.path.splitext(f)[0]))

    elif desired_frames < len(all_frames):
        while len(all_frames) > desired_frames:
            if not all_frames:  # Check if the all_frames list is empty
                break
            src = random.choice(all_frames)
            src_path = os.path.join(folder_path, src)
            os.remove(src_path)
            all_frames.remove(src)

        # Rename the remaining frames
        for idx, frame in enumerate(all_frames, start=1):
            old_frame_path = os.path.join(folder_path, frame)
            new_frame_path = os.path.join(folder_path, f"{idx}.png")
            os.rename(old_frame_path, new_frame_path)

def insert_images():
    selected_image_paths = selected_files.get().split(", ")
    destination_folder_path = destination_folder_var.get()
    insert_index = int(insert_index_var.get())

    os.chdir(destination_folder_path)

    # Shift the frames after the insertion index
    all_frames = [f for f in os.listdir(destination_folder_path) if f.endswith('.png')]
    all_frames.sort(key=lambda f: int(os.path.splitext(f)[0]), reverse=True)
    for frame in all_frames:
        frame_number = int(os.path.splitext(frame)[0])
        if frame_number >= insert_index:
            new_frame_number = frame_number + len(selected_image_paths)
            os.rename(frame, f"{new_frame_number}.png")

    # Insert the selected images
    for idx, image_path in enumerate(selected_image_paths, start=insert_index):
        src = image_path
        dst = f"{idx}.png"
        shutil.copy2(src, dst)


def delete_frames():
    if messagebox.askyesno("Delete frames", "Are you sure you want to delete the selected frames? This action cannot be undone."):
        folder_path = os.path.dirname(selected_files.get().split(",")[0].strip())
        os.chdir(folder_path)

        frames_to_delete = [f.strip() for f in selected_files.get().split(",")]

        # Delete selected frames
        for frame in frames_to_delete:
            os.remove(frame)

        # Renumber remaining frames
        all_frames = [f for f in os.listdir(folder_path) if f.endswith('.png')]
        all_frames.sort(key=lambda f: int(os.path.splitext(f)[0]))

        for idx, frame in enumerate(all_frames, start=1):
            src = frame
            dst = f"{idx}.png"
            if src != dst:
                shutil.move(src, dst)


def sort_and_rename_by_date():
    folder_path = folder_path_var.get()
    os.chdir(folder_path)

    # Get all the image files and sort them by modification date
    all_frames = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    all_frames.sort(key=lambda f: os.path.getmtime(os.path.join(folder_path, f)))

    # Rename the image files according to the sorted order
    for idx, frame in enumerate(all_frames, start=1):
        new_frame_name = f"{idx}.png"
        os.rename(frame, new_frame_name)


def duplicate_frames_random():
    folder_path = folder_path_var.get()
    min_dup, max_dup = eval(random_duplicates_range_var.get())
    os.chdir(folder_path)

    all_frames = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    all_frames.sort(key=lambda f: int(os.path.splitext(f)[0]))

    with tempfile.TemporaryDirectory() as temp_dir:
        new_frames = []
        for frame in all_frames:
            num_duplicates = random.randint(min_dup, max_dup)
            new_frames.extend([frame] * num_duplicates)

        for idx, frame in enumerate(new_frames, start=1):
            src = os.path.join(folder_path, frame)
            dst = os.path.join(temp_dir, f"{idx}.png")
            shutil.copy2(src, dst)

        for frame in all_frames:
            os.remove(frame)

        for frame in os.listdir(temp_dir):
            src = os.path.join(temp_dir, frame)
            dst = os.path.join(folder_path, frame)
            shutil.move(src, dst)

root = Tk()
root.title("Frame Manipulator")

selected_files = StringVar()
duplicates_var = StringVar()
jumble_var = BooleanVar()
destination_folder_var = StringVar()
insert_index_var = StringVar()
folder_path_var = StringVar()
random_duplicates_range_var = StringVar()
desired_frames_var = StringVar()


def browse_destination_folder():
    folder = filedialog.askdirectory()
    if folder:
        destination_folder_var.set(folder)

Label(root, text="Selected frames:").grid(row=0, column=0, sticky="e")
Entry(root, textvariable=selected_files, width=50).grid(row=0, column=1)
browse_button = Button(root, text="Browse", command=browse_folder)
browse_button.grid(row=0, column=2)
browse_button.bind('<Enter>', lambda event: show_tooltip(event, "Select frames to be manipulated"))
browse_button.bind('<Leave>', hide_tooltip)

# Duplicate frames
Label(root, text="Duplicate frames").grid(row=1, column=0, columnspan=3)
Label(root, text="Number of duplicates:").grid(row=2, column=0, sticky="e")
Entry(root, textvariable=duplicates_var).grid(row=2, column=1)
Checkbutton(root, text="Jumble frames", variable=jumble_var).grid(row=2, column=2, sticky="w")
duplicate_button = Button(root, text="Duplicate", command=duplicate_frames)
duplicate_button.grid(row=3, column=2)
duplicate_button.bind('<Enter>', lambda event: show_tooltip(event, "Duplicate selected frames"))
duplicate_button.bind('<Leave>', hide_tooltip)

Separator(root, orient="horizontal").grid(row=4, column=0, columnspan=3, sticky="ew", pady=10)

# Insert images
Label(root, text="Insert images").grid(row=5, column=0, columnspan=3)
Label(root, text="Destination folder:").grid(row=6, column=0, sticky="e")
Entry(root, textvariable=destination_folder_var, width=50).grid(row=6, column=1)
Button(root, text="Browse", command=browse_destination_folder).grid(row=6, column=2)
Label(root, text="Insert index:").grid(row=7, column=0, sticky="e")
Entry(root, textvariable=insert_index_var).grid(row=7, column=1)
insert_button = Button(root, text="Insert", command=insert_images)
insert_button.grid(row=7, column=2)
insert_button.bind('<Enter>', lambda event: show_tooltip(event, "Insert selected images at the specified index"))
insert_button.bind('<Leave>', hide_tooltip)

Separator(root, orient="horizontal").grid(row=8, column=0, columnspan=3, sticky="ew", pady=10)

# Delete frames
Label(root, text="Delete frames").grid(row=9, column=0, columnspan=3)
delete_button = Button(root, text="Delete", command=delete_frames)
delete_button.grid(row=10, column=1)
delete_button.bind('<Enter>', lambda event: show_tooltip(event, "Delete selected frames"))
delete_button.bind('<Leave>', hide_tooltip)

Separator(root, orient="horizontal").grid(row=11, column=0, columnspan=3, sticky="ew", pady=10)

# Randomize duplicates
Label(root, text="Randomize duplicates").grid(row=12, column=0, columnspan=3)
Label(root, text="Folder path for random duplicates:").grid(row=13, column=0, sticky="e")
Entry(root, textvariable=folder_path_var, width=50).grid(row=13, column=1)
Button(root, text="Browse", command=browse_folder_path).grid(row=13, column=2)
Label(root, text="Random duplicate range (e.g., (1,5)):").grid(row=14, column=0, sticky="e")
Entry(root, textvariable=random_duplicates_range_var).grid(row=14, column=1)
randomize_button = Button(root, text="Randomize", command=duplicate_frames_random)
randomize_button.grid(row=14, column=2)
randomize_button.bind('<Enter>', lambda event: show_tooltip(event, "Create random duplicates of frames in the specified range"))
randomize_button.bind('<Leave>', hide_tooltip)

Separator(root, orient="horizontal").grid(row=15, column=0, columnspan=3, sticky="ew", pady=10)

# Sort and rename by date
Label(root, text="Sort and rename by date").grid(row=16, column=0, columnspan=3)
sort_button = Button(root, text="Sort", command=sort_and_rename_by_date)
sort_button.grid(row=17, column=1)
sort_button.bind('<Enter>', lambda event: show_tooltip(event, "Sort and rename frames by date"))
sort_button.bind('<Leave>', hide_tooltip)

# Adjust frames
Label(root, text="Adjust frames").grid(row=18, column=0, columnspan=3)
Label(root, text="Folder path:").grid(row=19, column=0, sticky="e")
Entry(root, textvariable=folder_path_var, width=50).grid(row=19, column=1)
Button(root, text="Browse", command=browse_folder_path).grid(row=19, column=2)
Label(root, text="Desired number of frames:").grid(row=20, column=0, sticky="e")
Entry(root, textvariable=desired_frames_var).grid(row=20, column=1)
adjust_button = Button(root, text="Adjust", command=adjust_frames)
adjust_button.grid(row=20, column=2)
adjust_button.bind('<Enter>', lambda event: show_tooltip(event, "Adjust the number of frames to the desired value"))
adjust_button.bind('<Leave>', hide_tooltip)

# Add a separator

# Reverse frames
Label(root, text="Reverse frames").grid(row=21, column=0, columnspan=3)
Label(root, text="Folder path for reversing frames:").grid(row=22, column=0, sticky="e")
Entry(root, textvariable=folder_path_var, width=50).grid(row=22, column=1)
Button(root, text="Browse", command=browse_folder_path).grid(row=22, column=2)
reverse_button = Button(root, text="Reverse", command=reverse_frames)
reverse_button.grid(row=22, column=2)
reverse_button.bind('<Enter>', lambda event: show_tooltip(event, "Reverse the order of frames in the folder"))
reverse_button.bind('<Leave>', hide_tooltip)

root.mainloop()
