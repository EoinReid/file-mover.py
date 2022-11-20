# File Mover script
# just update the destination directory name and the file extension to move chosen files to chosen directory
# e.g. change mv_files escond paramter from *.txt to *.png for png files
# update destination from home/user/Text to home/user/Png
import shutil
import glob
import os
from pathlib import Path

def move_files(source, destination):
    mv_files = glob.glob(os.path.join(source, '*.py'), recursive=True)
    for file in mv_files:
            dst_path = os.path.join(destination, os.path.basename(file))
            shutil.move(file, dst_path)
            print(f"Moved {file} -> {dst_path}")

try:
    source = Path.home()
    destination = Path(Path.home() / "Python")
    if os.path.exists(destination):
       move_files(source,destination)
    else:
           os.mkdir(destination)
           move_files(source,destination)

except FileNotFoundError:
    print("file or directory not found.")