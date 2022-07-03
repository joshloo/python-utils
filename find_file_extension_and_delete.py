import os
import os.path
import shutil

for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if (f.endswith(".html") or f.endswith(".HTML") or f.endswith(".txt") or f.endswith(".url") or f.endswith(".URL"))]:
        print(os.path.join(dirpath, filename))
        os.remove(os.path.join(dirpath, filename))