# this script get the extensions of files 
import os
path = input('Enter the path: ').strip()
extensions = []
for root, directories, filenames in os.walk(path):
    for file in filenames:
        firstpart, ext = os.path.splitext(file)
        if ext not in extensions:
            extensions.append(ext)


print(extensions)
