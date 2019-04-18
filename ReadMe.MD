# DEPA SideShow 

### Manual Setup
Create a syncable folder on your Google Drive:
* ```rclone config```
* Name the remote "remote"
* Clone this repo to the root of your pi
### The Shortcut 
* Install gdrive 
* Run the provided setup script 
### Pipeline 
* Use rclone to read all files in folder 
* * if file is in disallowed format convert it to jpg
* Use feh to start a slideshow of the converte files 

[Syncing while google drive *rclone*](https://unix.stackexchange.com/questions/136371/how-to-download-a-folder-from-google-drive-using-terminal/332277)

[RClone Instructions](https://www.techrepublic.com/article/how-to-sync-from-linux-to-google-drive-with-rclone/)

[RClone Instructions Video](https://www.youtube.com/watch?v=vPs9K_VC-lg)

[Displaying local slideshow using *feh*](https://www.instructables.com/id/Easy-Raspberry-Pi-Based-ScreensaverSlideshow-for-E/)

[Scheduling Jobs with Crontab]()

[Convert PPT to JPG](https://github.com/hadwinzhy/convert-ppt-to-jpg)

### Old Docs 
[Syncing while google drive *gdrive* **Promising Alternative**]()
 
[Displaying local slideshow using *slide* ](https://opensource.com/article/19/2/wifi-picture-frame-raspberry-pi)




## FAQ
* How do I install gdrive?
* * fsfeg
* How do I create syncable directories