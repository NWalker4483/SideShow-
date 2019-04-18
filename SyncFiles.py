import os 
import time 
import subprocess as sp
import commands
#rclone -v --drive-impersonate foo@example.com lsf gdrive:backup

Slide_Folder_Path = "slides/"
#### Helper/f
def Pass(a):
    pass  
def PPT2JPG(filename):
    # Convert PPT to PDF
    commands.getoutput("soffice --headless --convert-to pdf {} --outdir .".format(filename))
    PDF2JPG(os.path.splitext(filename)[0] + ".pdf")
    pass
def PDF2JPG(filename):
     commands.getoutput("convert -verbose -density 150 {} -quality 100 {}{}'.jpg'".format(filename,Slide_Folder_Path,filename))
    pass
Converters = {"png":Pass,
              "ppt":PPT2JPG,
              "pptx":PPT2JPG,
              "pdf":PDF2JPG
              }
#### Check Dir

if not (os.getcwd() == '/home/pi/SideShow-'){
    print("Wrong Directory")
    exit()
    }
#### Download new files 
while True:
    print()
    resp = commands.getoutput("rclone copy remote:{} /home/pi/SideShow-/slides".format(Slide_Folder_Path))
    if "403" not in resp:
        break 
    time.sleep(.5)
#### Convert new files
for phile in os.listdir("."): 
    try: 
        extension = os.path.splitext(phile)[1]
        Converters[extension](phile)
    except:
        print("Invalid File Type present")
#### Launch SlideShow 
sp.Popen(['feh', '-Y', '-x', '-q', '-D', '5', '-B', 'black', '-F', '-Z', '-z', '-r', "/home/pi/SideShow-/slides"])
time.sleep(100)
#### Restart the process