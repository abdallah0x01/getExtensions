import os
import shutil
# path = input('Enter path you want organize files in: ').strip()
extensions = ['txt','jpg','jpeg','png','mp4','mp3','html','css','iso','pdf','docx','exe','py','sh','c']
path = 'c:\\users\\abdallah\\desktop'
os.chdir(path)
path2copy2 = 'c:\\users\\abdallah\\desktop\\dir'

for root, dirnames,filenames in os.walk(path):
    for filename in filenames:
        firstpart, ext = os.path.splitext(filename)
        ext = ext.strip('.')
        if ext in extensions:
            if not os.path.exists(f'{path2copy2}\\{ext}'):
                os.makedirs(f'{path2copy2}\\{ext}')
                try:
                    shutil.copy(f'{root}\\{filename}',f'{path2copy2}\\{ext}')
                except:
                    continue

            else:
                try:
                    shutil.copy(f'{root}\\{filename}',f'{path2copy2}\\{ext}')
                except:
                    continue
