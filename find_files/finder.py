import os
to_find = input('Enter file or directory to find: ')
path = input('Enter path to search in like c:\windows\system32: ')

findings = []
for currentdir,direnames,filenames in os.walk(fr'{path}'):
    if to_find in filenames or to_find in direnames:
        findings.append(currentdir)
for finding in findings:
    print(f'what you want in {finding}')
