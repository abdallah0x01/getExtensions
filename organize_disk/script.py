import os
import shutil
# path = input('Enter path you want organize files in: ').strip()
path = 'c:\\users\\abdallah\\desktop'
os.chdir(path)
path2copy2 = 'c:\\users\\abdallah\\desktop\\dir'

for root, dirnames,filenames in os.walk(path):
    for filename in filenames:
        firstpart, ext = os.path.splitext(filename)
        if not os.path.exists(f'{path2copy2}\\{ext}'):
            os.makedirs(f'{path2copy2}\\{ext}')
            try:
                shutil.copy(filename,f'{path2copy2}\\{ext}')
            except:
                continue

        else:
            try:
                shutil.copy(filename,f'{path2copy2}\\{ext}')
            except:
                continue
