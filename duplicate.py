from tkinter.filedialog import askdirectory
from tkinter import Tk
import os
import hashlib
from pathlib import Path
Tk().withdraw()
path = askdirectory(title="Select A Folder")

file_list = os.walk(path)

unique = dict()
for root, folders, files in file_list:
    for file in files:
        path = Path(os.path.join(root, file))
        fileHash = hashlib.md5(open(path, 'rb').read()).hexdigest()
        print(len(fileHash))
        if fileHash not in unique:
            unique[fileHash] = path

        else:
            os.walk(path)
            print(f"{path} is a duplicate")

# IF YOU WANT TO DELETE DUPLICATES, UNCOMMENT THE CODE BELOW AND REPLACE THE ONE ON TOP BECAUSE
# IT ONLY PRINTS OUT THE DUPLICATES AND DOES NOT DELETE
#
#        else:
#            os.remove(path)
#            print(f"{path} has been deleted")
