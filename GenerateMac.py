import random
import time,threading,datetime
import subprocess
import platform as ptf

now = datetime.datetime.now()
def getValidLetter(stringLength=2) :
    try:
        letters ='a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9'
        temp = random.choices(letters)
        validLetter=''.join(random.choice(letters) for i in range(stringLength))
    except(KeyboardInterrupt, SystemExit, SyntaxError):
         print("Stopped in getValidLetter()")
    return validLetter
def getMac():
    try:
        now=datetime.datetime.now()
        if(now.second%2==0):
            mac= "00:" + getValidLetter() + ":" + getValidLetter() + ":" + getValidLetter() + ":" + getValidLetter() + ":" + getValidLetter()
        else:
            mac= "06:" + getValidLetter() + ":" + getValidLetter() + ":" + getValidLetter() + ":" + getValidLetter() + ":" + getValidLetter()
    except(KeyboardInterrupt, SystemExit, SyntaxError):
        print("Stopped in getMac()")
    return mac
def getIpAddress():
    try:

        if (now.second % 2 == 0):
            ipAddress = ""
        elif(now.second%2==1):
            ipAddress = ""
        else:
            ipAddress=""
    except(KeyboardInterrupt, SystemExit, SyntaxError):
        print("Stopped in getMac()")
    return ipAddress

def setMac():
    #here to improve check any connected card or software system
    #sudo to remember
    #call("ip link set dev eno1 address "+getMac())
    #getmac /v /fo list
    if(ptf.system()=="Linux"):
        cmd='ip link set dev eno1 address '
        subprocess.call(cmd + getMac(),shell=True)
    elif(ptf.system()=="Windows"):
        print("Windows")
def setIpAddress():
    cmdIP='ifconfig eno1 '+getIpAddress()+' netmask 255.255.255.0'
    print(cmdIP)
   # subprocess.call(cmdIP,shell=True)
def setMode(mode):
    if(mode=='critical'):
        #to do now.second
        print(now.second)
    elif(mode=='normal'):
        #to do now hour for ip
        print(now.minute)
    else:
        print(now.hour)

def repeatEvery():
    try:
        print(getMac())
        print(time.ctime())
        print(getIpAddress())
        setMode('critical')
        setIpAddress()
        #setMac()
        #repeat every second
        threading.Timer(3,repeatEvery).start()
      #  while True: time.sleep(100)
    except (KeyboardInterrupt, SystemExit, SyntaxError):
        print("Stopped in repeatEvery()")
repeatEvery()

