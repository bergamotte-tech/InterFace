#----------IMPORTS----------

import os
import time
from threading import Thread
# from sense_hat import SenseHat
# sense = SenseHat()


#----------GLOBAL VARIABLES----------

DefaultFace = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[81,72,249],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[81,72,249],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[81,72,249],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[81,72,249],[0,0,0],[0,0,0],[0,0,0],[81,72,249],[81,72,249],[81,72,249],[81,72,249],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
HeatFace = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[255,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[255,0,0],[0,0,0],[255,0,0],[255,0,0],[0,0,0],[255,0,0],[255,0,0],[0,0,0],[0,0,0],[255,0,0],[255,0,0],[255,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[255,0,0],[255,0,0],[255,255,0],[255,0,0],[255,0,0],[0,0,0],[0,0,0],[255,0,0],[255,0,0],[255,128,0],[255,255,0],[255,0,0],[255,0,0],[0,0,0],[0,0,0],[255,0,0],[255,128,0],[255,255,255],[255,255,255],[255,0,0],[255,0,0],[0,0,0],[0,0,0],[255,0,0],[255,255,0],[255,255,255],[255,128,0],[255,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[255,0,0],[255,255,0],[255,0,0],[0,0,0],[0,0,0],[0,0,0]]
HumidityFace = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,0,0],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,255,255],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,255,255],[0,0,0],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,0,0],[0,255,255],[0,0,0],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,0,0]]
SickFace1 = [[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,128,0],[0,128,0],[0,0,0],[0,0,0],[0,128,0],[0,128,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
SickFace2 = [[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,128,0],[0,128,0],[0,0,0],[0,0,0],[0,128,0],[0,128,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
PlugFace = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,160],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,160],[0,0,0],[0,0,160],[0,0,0],[0,0,160],[0,0,0],[0,0,0],[0,0,160],[0,0,0],[0,0,160],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,160],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,160],[0,0,0],[0,0,160],[0,0,160],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,160],[0,0,160],[0,0,0],[0,0,0],[0,0,160],[0,0,160],[0,0,160],[0,0,160],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]


UserCanDraw = False
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
        self.animationList = MainThread.animationList()
        self.alternator = 0
        self.switcher2 = {
            "default": MainThread.draw_default(self),
            "reaction": MainThread.draw_reaction(self),
            "temperature": MainThread.draw_temperature_warning(self),
            "humidity": MainThread.draw_humidity_warning(self),
            "shaking": MainThread.draw_shaking_warning(self),
        }
        
    def run(self):
        # TODO: create a new thread
        started = True
        while started:
            MainThread.check_temperature(self)
            MainThread.check_humidity(self)
            MainThread.check_shaking(self)
            MainThread.check_plug(self)

            MainThread.draw(self, self.animation.getTop())
        
    def check_temperature(self):
        global temperatureTriggered
        # TODO: temperature = get temperature
        
        # delete
        temperature = 10
        
        if (temperature >= 60 and temperatureTriggered == False): # corresponds to a new detection (some events can be detected and added but not instantly treated, because a higher priority event was added on top)
            self.animation.add("temperature")
            temperatureTriggered = True

        elif (temperatureTriggered == True and temperature <= 55): # to avoid multiple consecutive triggers when temperature is switching around 60°C
                self.animation.remove("temperature")
                temperatureTriggered = False

    def check_humidity(self):
        global humidityTriggered
        # TODO: humidity = get humidity
        
        #delete
        humidity = 0
        
        
        if (humidity >= 100 and humidityTriggered == False): # arbitrary value of humidity for now
            self.animation.add("humidity")
            humidityTriggered = True

        elif (humidityTriggered == True and humidity <= 95):
                self.animation.remove("humidity")
                humidityTriggered = False

    def check_shaking(self):
        global shakingTriggered
        # TODO: shaking = get shaking value --> we can create it gathering different indicators if needed
        
        #delete
        shaking = 0
        
        if (shaking >= 20 and shakingTriggered == False): # arbitrary value of shaking for now
            self.animation.add("shaking")
            shakingTriggered = True

        elif (shakingTriggered == True and shaking <= 15):
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
                    os.popen("sound_added.mp3")
                elif (newLength < oldLength):
                    os.popen("sound_removed.mp3")
        
        oldUsbList = newUsbList
        oldLength = len(oldUsbList)


    #----------DRAW----------
    def draw(self, content):
        currentTime = round(time.time()*10)
        self.alternator = currentTime - round(currentTime//10)*10 # gets tenth of a second

        if len(content)==2:
            if (self.alternator < 5):
                singleAnimation = content[0]
            else:
                singleAnimation = content[1]
        else:
            singleAnimation = content[0]

        self.switcher2.get(singleAnimation)


    def draw_default(self):
        # TODO: draw face
        pass

    # def draw_inactive(): OPTIONNAL

    def draw_reaction(self):
        # TODO: draw face for .4s
        self.animation.remove("plug")


    def draw_temperature_warning(self):
        # TODO: draw face
        pass


    def draw_humidity_warning(self):
        # TODO: draw face
        pass

    def draw_shaking_warning(self):
        if (self.alternator < 5):
            # TODO: draw face 1
            pass
        else:
            # TODO: draw face 2
            pass

#--------------------------------------


#----------ON/OFF----------

started = False

def start():
    global main
    if main == None:
        main = MainThread()
    else:
        print("Program already started")


def stop():
    global main
    if main != None:
        main.join()
        started = None
    else:
        print("Program not started yet")


message1 = MainThread()

message1.start()
# message1.join()
