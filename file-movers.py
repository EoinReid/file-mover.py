# File Mover script
import shutil
import glob
import os
from pathlib import Path
import sys

def move_files(source, destination, file_ext):
    mv_files = glob.glob(os.path.join(source, f'*{file_ext}'), recursive=True)
    for file in mv_files:
            dst_path = os.path.join(destination, os.path.basename(file))
            shutil.move(file, dst_path)
            print(f"Moved {file} -> {dst_path}")
try:
    print(str(len(sys.argv)))
    if len(sys.argv) < 4:
        print("Usage: python3 file-movers.py [source] [destination] [file extension]" )
        sys.exit()
    elif len(sys.argv) == 4:
        source = sys.argv[1]
        destination = Path(sys.argv[2])
        file_ext = sys.argv[3]
    if os.path.exists(destination):
       move_files(source,destination,file_ext)
    else:
           os.mkdir(destination)
           move_files(source,destination)
except FileNotFoundError:
    print("file or directory not found.")