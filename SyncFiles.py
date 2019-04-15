import os 
import time 
import subprocess as sp

#Photo_dir = ""
Slide_Folder_ID = ""
#### Helper
Converters = {}
#### Check Dir
if not (os.getcwd() == '/home/pi/SideShow-'){
    print("Wrong Directory")
    exit()
}
#### Download new files 
while true:
    os.system("gdrive sync download {} .".format(Slide_Folder_ID))
    time.sleep(.5)
#### Convert new files
for phile in os.listdir("."): 
    try:
        extension = os.path.splitext(phile)[1]
        
    except:
        print("Invalid File Type present")

#### Launch SlideShow 
    sp.Popen(['feh', '-Y', '-x', '-q', '-D', '5', '-B', 'black', '-F', '-Z', '-z', '-r', "/home/pi/SideShow-/slides"])
    