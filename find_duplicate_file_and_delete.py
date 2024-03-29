import sys
import os
import hashlib

def chunk_reader(fobj, chunk_size=1024):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

def check_for_duplicates(paths, hash=hashlib.sha1):
    hashes = {}
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                hashobj = hash()
                print("hashobj: ", hashobj)
                for chunk in chunk_reader(open(full_path, 'rb')):
                    hashobj.update(chunk)
                file_id = (hashobj.digest(), os.path.getsize(full_path))
                print("file_id: ", file_id)
                duplicate = hashes.get(file_id, None)
                print("duplicate: ", duplicate)
                if duplicate:
                    print("Duplicate found: %s and %s" % (full_path, duplicate))
                    try:
                        os.remove(duplicate)
                    except OSError as e:
                        print("Already deleted\n\n")
                        continue
                else:
                    hashes[file_id] = full_path

def remove_duplicates(dir):
    unique = []
    for filename in os.listdir(dir):
        if os.path.isfile(filename):
            filehash = md5.md5(file(filename).read()).hexdigest()
        if filehash not in unique: 
            unique.append(filehash)
        else: 
            os.remove(filename)

if sys.argv[1:]:
    check_for_duplicates(sys.argv[1:])
else:
    print("Please pass the paths to check as parameters to the script")