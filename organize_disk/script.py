import os
import shutil
path2copy2 = 'c:\\users\\abdallah\\downloads'
os.chdir(path2copy2)

for root, dirnames,filenames in os.walk(path2copy2):
    for filename in filenames:
        firstpart, ext = os.path.splitext(filename)
        ext = ext.strip('.')
        if not os.path.exists(f'{path2copy2}\\{ext}'):
                os.makedirs(f'{path2copy2}\\{ext}')
                try:
                    shutil.move(f'{root}\\{filename}',f'{path2copy2}\\{ext}')
                except:
                    continue

        else:
                try:
                    shutil.move(f'{root}\\{filename}',f'{path2copy2}\\{ext}')
                except:
                    continue
