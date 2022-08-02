import os
extensions = []
for root, directories, filenames in os.walk(os.getcwd()):
    for file in filenames:
        firstpart, ext = os.path.splitext(file)
        if ext not in extensions:
            extensions.append(ext)


print(extensions)
