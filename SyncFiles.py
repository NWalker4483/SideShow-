import os 
import time 
import subprocesss

Photo_dir = ""
Slide_Folder_ID = ""
#### Helper

#### Check Dir
if not (os.getcwd() == '/home/pi'){
    print()
    exit()
}

#### Download new files 
os.system("gdrive sync download {} .".format(Slide_Folder_ID))
#### Convert new files
for phile in os.listdir("."): 
    try:
        pass
    except:
        print("Invalid File Type present")

#### Launch SlideShow 
    sp.Popen(['feh', '-Y', '-x', '-q', '-D', '5', '-B', 'black', '-F', '-Z', '-z', '-r', '/media/'])
    