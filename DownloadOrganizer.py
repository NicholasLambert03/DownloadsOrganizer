"""Imports"""
import os
import mimetypes
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:

    def __init__(self,watch_directory):
        self.watch_directory = watch_directory
        self.observer = Observer()
    
    def run(self):
        print("Sorting all currently unorganized files")
        FileSorter.sort_files_in_dir(self.watch_directory)
        print("Beginning Real Time Sorter")
        event_handler = EventHandler()
        self.observer.schedule(event_handler,self.watch_directory)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("File Sorting Stopped")
            self.observer.join()

class EventHandler(FileSystemEventHandler):

    @staticmethod
    def on_created(event):
        if event.is_directory:
            return None
        else:
            FileSorter.sort_file_in_dir(event.src_path)

class FileSorter():
    
    @staticmethod
    def sort_file_in_dir(file_path):
        file_name = os.path.basename(file_path)
        dir_path = os.path.dirname(file_path)
        try:
            mime_type,_= mimetypes.guess_type(file_path)
            try:
                folder_name =  mime_type.split('/')[0].capitalize()+"s"
            except AttributeError as e:
                print(f"Unrecognised file type for {file_name}, moving into Misc")
                folder_name = "Misc" #Handles Unrecognised File Type
            folder_path = os.path.join(dir_path,folder_name)
            os.makedirs(folder_path,exist_ok=True)
            destination = os.path.join(folder_path,file_name)
            num=0 #Prevents overwriting of files with same name
            while(os.path.exists(destination)):
                num+=1
                destination = os.path.join(folder_path,file_name+f"[{num}]")
            shutil.move(file_path,destination)
            if num ==0:
                print(f"{file_name} successfully moved to /{folder_name}")
            else:
                print(f"{file_name} (renamed to {file_name}[{num}] due to pre-existing file in directory) successfully moved to /{folder_name}")

        except Exception as e:
            print(f"Error moving file {file_name}: {e}")
        
    @staticmethod
    def sort_files_in_dir(dir_path):
        files = (os.path.join(dir_path,file) for file in os.listdir(dir_path) #Ensures no folders selected
                    if os.path.isfile(os.path.join(dir_path,file))) 
        for file in files:
            FileSorter.sort_file_in_dir(file)


if __name__ == '__main__':
    watch = Watcher("/home/nicholas/Downloads")
    watch.run()

