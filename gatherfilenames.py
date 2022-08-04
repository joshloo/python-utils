#makefile creator for the content with huge library
import os

files = os.listdir('.')
print(files)

a = open("files.txt", "w")

# first, extract h file, then extract c file.
for file in files:
  if (file.endswith(".h")):
    a.write(file + "\n")

for file in files:
  if (file.endswith(".c")):
    a.write(file + "\n")