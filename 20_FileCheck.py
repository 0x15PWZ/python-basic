import os
count = 0
check = ''
while check != 'notes.txt': 
    filename = input('Enter file name:')
    count+=1
    if os.path.exists(filename):
        print(f"{filename} exists.")
        break
    else:
        print(f"{filename} does not exist.")
