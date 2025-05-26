"""Imports"""
import os
import mimetypes
import shutil
import watchdog



print("Organizing download folder")
download_path = "/home/nicholas/Downloads"
downloaded_files = (file for file in os.listdir(download_path) #Ensures no folders selected
                    if os.path.isfile(os.path.join(download_path,file))) 



successes = 0
total = 0
for file_name in downloaded_files:
    total+=1
    try:
        file_path = os.path.join(download_path,file_name)
        mime_type, encoding = mimetypes.guess_type(file_path)
        try:
            folder_name =  mime_type.split('/')[0].capitalize()+"s"
        except AttributeError as e:
            print(f"Unrecognised file type for {file_name}, moved into Misc")
            folder_name = "Misc" #Handles Unrecognised File Type
        folder_path = os.path.join(download_path,folder_name)
        os.makedirs(folder_path,exist_ok=True)
        shutil.move(file_path,os.path.join(folder_path,file_name))
        successes +=1

    except Exception as e:
        print(f"Error moving file {file_name}: {e}")

print(f"{successes}/{total} files successfuly moved")
    
