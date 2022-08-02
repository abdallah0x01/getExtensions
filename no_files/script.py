#this script retun the number of files in a path you enter
import os
path = input('Enter path: ').strip()
no_files = 0
for root, directories, filenames in os.walk(path):
    no_files += len(filenames)

print(no_files)
