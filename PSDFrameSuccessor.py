import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FrameHandler(FileSystemEventHandler):
    def __init__(self, folder, target_file):
        self.folder = folder
        self.target_file = target_file
        self.serial_number = 1

    def on_modified(self, event):
        if not event.is_directory and os.path.basename(event.src_path) == self.target_file:
            new_file_name = f"{self.serial_number}.png"
            os.rename(event.src_path, os.path.join(self.folder, new_file_name))
            self.serial_number += 1
            print(f"Renamed {self.target_file} to {new_file_name}")

def monitor_folder(folder, target_file):
    event_handler = FrameHandler(folder, target_file)
    observer = Observer()
    observer.schedule(event_handler, folder, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == "__main__":
    folder = "C:\\Users\\Thomas.Henshaw001\\Documents\\Art 481\\Art\\SEQUENCE 2\\SEISMO\\End Sequence\\BG"
    target_file = "Daco_5065795.png"
    monitor_folder(folder, target_file)
