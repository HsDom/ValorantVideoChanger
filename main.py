import hashlib,os,shutil,psutil
from time import sleep


def hash_file(filename):
   h = hashlib.sha1()
   with open(filename,'rb') as file:
       chunk = 0
       while chunk != b'':
           chunk = file.read(1024)
           h.update(chunk)

   return h.hexdigest()


#Find which drive valorant is installed on
def find_valorant_drive():
    drives = psutil.disk_partitions()
    for drive in drives:
        if os.path.exists(drive.mountpoint + "\\Riot Games\\VALORANT\\live\\VALORANT.exe"):
            return drive.mountpoint
    return None


File_Names=['Battle Pass Glitches.webm','Contract Glitches.webm','HomeScreen.mp4','VTC_Valorant_Game_Changers_Homepage.mp4']

VALORANT_Win64_Shipping_Running = False
while True:

    # Check if VALORANT is running
    if VALORANT_Win64_Shipping_Running == False:
        for proc in psutil.process_iter():
            if proc.name() == "VALORANT-Win64-Shipping.exe":
                VALORANT_Win64_Shipping_Running = True

        #Change the video of the wallpaper
        if VALORANT_Win64_Shipping_Running:
            for file in File_Names:
                #checking if file exisits in valorant folder
                if os.path.exists(find_valorant_drive() + "\\Riot Games\\VALORANT\\live\\ShooterGame\Content\\Movies\\Menu\\" + file) and os.path.exists(file):
                    valorant_File = hash_file(f"C:\Riot Games\VALORANT\live\ShooterGame\Content\Movies\Menu\{file}")
                    File_To_Change = hash_file(file)
                    if valorant_File != File_To_Change:
                        shutil.copy(file, f"C:\Riot Games\VALORANT\live\ShooterGame\Content\Movies\Menu\{file}")

    else:
        #check if VALORANT-Win64-Shipping.exe is not running anymore
        IsRunnnig = False
        for proc in psutil.process_iter():
            if proc.name() == "VALORANT-Win64-Shipping.exe":
                IsRunnnig = True

        if IsRunnnig == False:
            VALORANT_Win64_Shipping_Running = False
