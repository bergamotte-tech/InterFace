#----------IMPORTS----------

import os
import time
from threading import Thread, Lock
from sense_hat import SenseHat
mySenseHat = SenseHat()


#----------GLOBAL VARIABLES----------
Blank = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
DefaultFace = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[81,72,249],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[81,72,249],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[81,72,249],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[81,72,249],[0,0,0],[0,0,0],[0,0,0],[81,72,249],[81,72,249],[81,72,249],[81,72,249],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
TemperatureFace = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[255,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[255,0,0],[0,0,0],[255,0,0],[255,0,0],[0,0,0],[255,0,0],[255,0,0],[0,0,0],[0,0,0],[255,0,0],[255,0,0],[255,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[255,0,0],[255,0,0],[255,255,0],[255,0,0],[255,0,0],[0,0,0],[0,0,0],[255,0,0],[255,0,0],[255,128,0],[255,255,0],[255,0,0],[255,0,0],[0,0,0],[0,0,0],[255,0,0],[255,128,0],[255,255,255],[255,255,255],[255,0,0],[255,0,0],[0,0,0],[0,0,0],[255,0,0],[255,255,0],[255,255,255],[255,128,0],[255,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[255,0,0],[255,255,0],[255,0,0],[0,0,0],[0,0,0],[0,0,0]]
HumidityFace = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,0,0],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,255,255],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,255,255],[0,0,0],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,0,0],[0,255,255],[0,0,0],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,0,0]]
ShakingFace1 = [[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,128,0],[0,128,0],[0,0,0],[0,0,0],[0,128,0],[0,128,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
ShakingFace2 = [[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,128,0],[0,128,0],[0,0,0],[0,0,0],[0,128,0],[0,128,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
PlugFace = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,160],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,160],[0,0,0],[0,0,160],[0,0,0],[0,0,160],[0,0,0],[0,0,0],[0,0,160],[0,0,0],[0,0,160],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,160],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,160],[0,0,0],[0,0,160],[0,0,160],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,160],[0,0,160],[0,0,0],[0,0,0],[0,0,160],[0,0,160],[0,0,160],[0,0,160],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

AllDrawings = [DefaultFace, TemperatureFace, HumidityFace, ShakingFace1, ShakingFace2, PlugFace]

DEBUGGING_temperature, DEBUGGING_humidity, DEBUGGING_shaking = False, False, False
temperature = 0
humidity = 0
shaking = 0

temperatureTriggered, humidityTriggered, shakingTriggered = False, False, False
oldLength = -1

levels = 4
depth = 2 # basic priority=0 (default) | low=1 (temperature, humidity) | medium=2 (shaking) | high=3 (plug)
switcher1 = {
    "temperature": 1,
    "humidity": 1,
    "shaking": 2,
    "plug": 3,
}

main = None
UserCanDraw = False

lock = Lock()


#----------MAIN CLASS----------

class MainThread(Thread):
    
    class animationList:

        def __init__(self):
            global depth, levels
            self._array = [[None for i in range(depth)] for j in range(levels)]
            self._array[0][0] = "default"

        def getTop(self): # returns an array / the content of a level
            global levels
            i = levels-1
            while (self._array[i][0] == None):
                i -= 1
            return self._array[i]

        def add(self, animation): # adds the animation designated by its precise String to its right level
            global switcher1
            animationLevel = switcher1.get(animation)
            if (self._array[animationLevel][0] == None):
                self._array[animationLevel][0] = animation
            else:
                self._array[animationLevel][1] = animation

        def remove(self, animation):
            global switcher1
            animationLevel = switcher1.get(animation)
            if (self._array[animationLevel][0] == animation):
                self._array[animationLevel][0] = self._array[animationLevel][1]
                self._array[animationLevel][1] = None
            else:
                self._array[animationLevel][1] = None

    def __init__(self):
        Thread.__init__(self)
        self.animation = MainThread.animationList()
        self.alternator = 0

    def run(self):
        self.clearAll()
        global started,UserCanDraw
        started = True
        while started:
            lock.acquire()
            if(not UserCanDraw):
                MainThread.check_temperature(self)
                MainThread.check_humidity(self)
                MainThread.check_shaking(self)
                MainThread.check_plug(self)
                MainThread.draw(self, self.animation.getTop())
                # print(self.alternator, " ", self.animation.getTop())
            lock.release()
            time.sleep(0.03)
        self.clearAll()
        
    def clearAll(self):
        global mySenseHat
        mySenseHat.set_pixels(Blank)


    def check_temperature(self):
        global temperatureTriggered, temperature
        if (DEBUGGING_temperature):
            temperature = 500
        else:
            temperature = mySenseHat.get_temperature()
        
        if (temperature >= 60 and temperatureTriggered == False): # corresponds to a new detection (some events can be detected and added but not instantly treated, because a higher priority event was added on top)
            self.animation.add("temperature")
            temperatureTriggered = True

        elif (temperatureTriggered == True and temperature <= 55): # to avoid multiple consecutive triggers when temperature is switching around 60°C
                self.animation.remove("temperature")
                temperatureTriggered = False


    def check_humidity(self):
        global humidityTriggered, humidity
        if (DEBUGGING_humidity):
            humidity = 500
        else:
            humidity = mySenseHat.get_humidity()
        
        if (humidity >= 100 and humidityTriggered == False): # arbitrary value of humidity for now
            self.animation.add("humidity")
            humidityTriggered = True

        elif (humidityTriggered == True and humidity <= 95):
                self.animation.remove("humidity")
                humidityTriggered = False


    def get_shaking(self):
        raw = mySenseHat.get_gyroscope_raw()
        rew = mySenseHat.get_accelerometer_raw()
        x = (raw['x'])
        y = (raw['y'])
        z = (raw['z'])
        a = (rew['x'])
        b = (rew['y'])
        c = (rew['z'])
        acceleration = abs(x)+abs(y)+abs(z)
        rotation = (abs(a)+abs(b)+abs(c))*2.5 # trying to have an equivalent "critical case" value between acceleration and rotation
        return max(acceleration*10, rotation*10)


    def check_shaking(self):
        global shakingTriggered, shaking
        if (DEBUGGING_shaking):
            shaking = 500
        else:
            shaking = self.get_shaking()
        
        if (shaking >= 50 and shakingTriggered == False):
            self.animation.add("shaking")
            shakingTriggered = True

        elif (shakingTriggered == True and shaking <= 25):
            self.animation.remove("shaking")
            shakingTriggered = False


    def check_plug(self):
        global oldLength
        newUsbList = os.popen("lsusb | awk '{print $6}'").read().split("\n")[:-1] # list of USB IDs stored in an array
        newLength = len(newUsbList)
        
        if (oldLength != -1):
            if (newLength != oldLength):
                self.animation.add("plug") # this animation is guaranteed to be instantly processed, thus does not need a plugTriggered variable. It is removed from the list after it has been drawn
                if (newLength > oldLength):
                    os.popen("aplay plug.wav &")
                elif (newLength < oldLength):
                    os.popen("aplay unplug.wav &")
                
        oldUsbList = newUsbList
        oldLength = len(oldUsbList)


    #----------DRAW----------
    def draw(self, content): # calls the right draw_something function
        currentTime = round(time.time()*10)
        self.alternator = currentTime - round(currentTime//10)*10 # gets tenth of a second

        if content[1]!=None:
            if (self.alternator < 5):
                singleAnimation = content[0]
            else:
                singleAnimation = content[1]
        else:
            singleAnimation = content[0]

        if(singleAnimation == "default"):
            MainThread.draw_default(self)
        elif(singleAnimation == "plug"):
            MainThread.draw_plug(self)
        elif(singleAnimation == "temperature"):
            MainThread.draw_temperature_warning(self)
        elif(singleAnimation == "humidity"):
            MainThread.draw_humidity_warning(self)
        elif(singleAnimation == "shaking"):
            MainThread.draw_shaking_warning(self)


    def draw_default(self):
        mySenseHat.set_pixels(DefaultFace)

    # def draw_inactive(): OPTIONNAL

    def draw_plug(self):
        mySenseHat.set_pixels(PlugFace)
        time.sleep(.4)
        self.animation.remove("plug")

    def draw_temperature_warning(self):
        mySenseHat.set_pixels(TemperatureFace)

    def draw_humidity_warning(self):
        mySenseHat.set_pixels(HumidityFace)

    def draw_shaking_warning(self):
        if (self.alternator < 5):
            mySenseHat.set_pixels(ShakingFace1)
        else:
            mySenseHat.set_pixels(ShakingFace2)

#--------------------------------------


#----------ON/OFF----------

started = False

def start():
    global main
    if main == None:
        main = MainThread()
        main.start() #TODO main.run() instead ?
        print("Program started with success")
    else:
        print("Program already started")

def stop():
    global main, started
    if main != None:
        started = False
        main.join()
        main = None
        print("Program ended with success")
    else:
        print("Program not started yet")
        
def switchPannelOwner(userCanDraw, clear):
    global UserCanDraw, mySenseHat, Blank
    lock.acquire()
    UserCanDraw = userCanDraw
    lock.release()
    if(clear and main != None):
        mySenseHat.set_pixels(Blank)
    
def symmetry():
    global AllDrawings
    for paint in AllDrawings:
        for i in range (0,32):
            temp = paint[i];
            paint[i] = paint[63-i]
            paint[63-i] = temp
            
def triggerTemperature():
    global DEBUGGING_temperature
    DEBUGGING_temperature = True
    
def triggerHumidity():
    global DEBUGGING_humidity
    DEBUGGING_humidity = True
    
def triggerShaking():
    global DEBUGGING_shaking
    DEBUGGING_shaking = True
    
def untriggerTemperature():
    global DEBUGGING_temperature
    DEBUGGING_temperature = False
    
def untriggerHumidity():
    global DEBUGGING_humidity
    DEBUGGING_humidity = False
    
def untriggerShaking():
    global DEBUGGING_shaking
    DEBUGGING_shaking = False

#----------TESTS----------

