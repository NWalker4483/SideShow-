import os 
import time 
import subprocess as sp
import commands
#rclone -v --drive-impersonate foo@example.com lsf gdrive:backup

Slide_Folder_Path = "slides/"
Temp_Slide_Folder_Path = "temp_slides/"
#### Helper/f
def Pass(a):
    pass  
def PPT2JPG(filename):
    pdf_filename = os.path.splitext(filename)[0] + ".pdf"
    print("Converting {} to pdf".format(filename))
    # Convert PPT to PDF
    commands.getoutput("soffice --headless --convert-to pdf {}{} --outdir .".format(Temp_Slide_Folder_Path,filename))
    #print("\tSplitting {}".format(pdf_filename))
    #commands.getoutput("pdfseparate {} {}".format(os.path.splitext(filename)[0] + ".pdf",os.path.splitext(filename)[0] + ".page%d"))
    #For Every Seperated File 
    PDF2JPG(pdf_filename)
    
def PDF2JPG(filename):
    commands.getoutput("convert -verbose -density 150 {} -quality 100 {}{}'.jpg'".format(filename,Slide_Folder_Path,filename))
    pass
Converters = {".png":Pass,
              ".jpg":Pass,
              ".jpeg":Pass,
              ".ppt":PPT2JPG,
              ".pptx":PPT2JPG,
              ".pdf":PDF2JPG
              }
#### Check Dir

if not (os.getcwd() == '/home/pi/SideShow-'):
    print("Wrong Directory")
    exit()
#### Download new files 
while True:
    print()
    resp = commands.getoutput("rclone copy remote:{} /home/pi/SideShow-/temp_slides".format(Slide_Folder_Path))
    if "403" not in resp:
        break 
    time.sleep(.5)
#### Convert new files
for phile in os.listdir(Temp_Slide_Folder_Path): 
    try: 
        extension = os.path.splitext(phile)[1]
        Converters[extension](phile)
    except:
        print("'{}' file conversion failed".format(phile))
#### Launch SlideShow 
sp.Popen(['feh', '-Y', '-x', '-q', '-D', '5', '-B', 'black', '-F', '-Z', '-z', '-r', "/home/pi/SideShow-/slides"])
#"feh -Y -x -q -D 5 -B black -F -Z -z -r /home/pi/SideShow-/slides"

time.sleep(10000)
#### Restart the process
