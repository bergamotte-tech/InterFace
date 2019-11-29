
#----------IMPORTS----------
import os
import time
from sense_hat import SenseHat

global sense = SenseHat()


#----------DATA STRUCTURE----------
class animationList:
    levels, depth = (4, 2) # basic priority=0 (default) | low=1 (temperature, humidity) | medium=2 (shaking) | high=3 (plug)
        switcher1 = {
        "temperature": 1,
        "humidity": 1,
        "shaking": 2,
        "plug": 3,
    }

    def __init__(self):
        self._array = [[None for i in range(depth)] for j in range(levels)]
        self._array[0][0] = "default"

    def getTop(self): # returns an array / the content of a level
        i = levels-1
        while (self._array[i][0] == None):
            i -= 1
        return self._array[i]

    def addAnimation(self, animation): # adds the animation designated by its precise String to its corresponding level
        animationLevel = switcher1.get(animation)
        if (self._array[animationLevel][0] == None):
            self._array[animationLevel][0] = animation
        else:
            self._array[animationLevel][1] = animation

    def removeAnimation(self, animation):
        animationLevel = switcher1.get(animation)
        if (self._array[animationLevel][0] == animation):
            self._array[animationLevel][0] = self._array[animationLevel][1]
            self._array[animationLevel][1] = None
        else:
            self._array[animationLevel][1] = None

myAnimationList = animationList()


#----------DETECTORS----------
temperatureTriggered, humidityTriggered, shakingTriggered = False
oldLength = -1
    

def check_temperature(animationList):
    # TODO: temperature = get temperature
    if (temperature >= 60 and temperatureTriggered == False): # corresponds to a new detection (some events can be detected and added but not instantly treated, because a higher priority event was added on top)
        animationList.addAnimation("temperature")
        temperatureTriggered = True

    elif (temperatureTriggered == True and temperature <= 55): # to avoid multiple consecutive triggers when temperature is switching around 60°C
            animationList.removeAnimation("temperature")
            temperatureTriggered = False


def check_humidity(animationList):
    # TODO: humidity = get humidity
    if (humidity >= 100 and humidityTriggered == False): # arbitrary value of humidity for now
        animationList.addAnimation("humidity")
        humidityTriggered = True

    elif (humidityTriggered == True and humidity <= 95):
            animationList.removeAnimation("humidity")
            humidityTriggered = False


def check_shaking():
    # TODO: shaking = get shaking value --> we can create it gathering different indicators if needed
    if (shaking >= 20 and shakingTriggered == False): # arbitrary value of shaking for now
        animationList.add("shaking")
        shakingTriggered = True

    elif (shakingTriggered == True and shaking <= 15):
            animationList.remove("shaking")
            shakingTriggered = False


def check_plug():
    newUsbList = os.popen("lsusb | awk '{print $6}'").read().split("\n")[:-1] # list of USB IDs stored in an array
    newLength = len(newUsbList)
    
    if (oldLength != -1):
        if (newLength != oldLength):
            animationList.add("plug") # this animation is guaranteed to be instantly processed, thus does not need a plugTriggered variable. It is removed from the list after it has been drawn

            if (newLength > oldLength):
                os.popen("sound_added.mp3")
            elif (newLength < oldLength):
                os.popen("sound_removed.mp3")
    
    oldUsbList = newUsbList
    oldLength = len(oldUsbList)


#----------DRAW----------
switcher2 = {
    "default": draw_default(),
    "reaction": draw_reaction(),
    "temperature": draw_temperature_warning(),
    "humidity": draw_humidity_warning(),
    "shaking": draw_shaking_warning(),
}

def draw(content):
    currentTime = round(time.time()*10)
    alternator = currentTime - round(currentTime//10)*10 # gets tenth of a second

    if len(content)==2:
        if (alternator < 5):
            singleAnimation = content[0]
        else:
            singleAnimation = content[1]
    else:
        singleAnimation = content[0]

    switcher2.get(singleAnimation)


def draw_default():
    # TODO: draw face
    pass

# def draw_inactive(): OPTIONNAL
#   pass


def draw_reaction():
    # TODO: draw face for .4s
    animationList.remove("plug")


def draw_temperature_warning():
    # TODO: draw face
    pass


def draw_humidity_warning():
    # TODO: draw face
    pass


def draw_shaking_warning():
    if (alternator < 5):
        # TODO: draw face 1
        pass
    else:
        # TODO: draw face 2
        pass


#----------ON/OFF----------
started = False

def start():
    if not(started):
        # TODO: create a new thread
        started = True
        while started:
            check_temperature()
            check_humidity()
            check_shaking()
            check_plug()

            draw(animationList.getTop())
    else:
        print("Program already started")


def stop():
    if started:
        # TODO: kill thread and reset the changes (leds...)
        started = False
    else:
        print("Program not started yet")