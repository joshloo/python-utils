import os
import os.path
import shutil

def mkdir(location):
    folder = os.path.exists(location)
    if not folder:
        os.mkdir(location)
        print("mkdir "+location+" ——success")
    else:
        print("location folder exists!!")

new_folder = "./ExtractedJpg"
mkdir(new_folder)

for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if (f.endswith(".jpg") or f.endswith(".JPG") or f.endswith(".jpeg"))]:
        print(os.path.join(dirpath, filename))
        # Move from source to destination
        shutil.move(os.path.join(dirpath, filename), os.path.join(new_folder, filename))