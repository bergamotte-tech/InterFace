#----------IMPORTS----------
		# TODO: /!\ TO MINIMZE /!\
import os
import time
from sense_hat import SenseHat

global sense = SenseHat()
DefaultFace = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[81,72,249],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[81,72,249],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[81,72,249],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[81,72,249],[0,0,0],[0,0,0],[0,0,0],[81,72,249],[81,72,249],[81,72,249],[81,72,249],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
HeatFace = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[255,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[255,0,0],[0,0,0],[255,0,0],[255,0,0],[0,0,0],[255,0,0],[255,0,0],[0,0,0],[0,0,0],[255,0,0],[255,0,0],[255,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[255,0,0],[255,0,0],[255,255,0],[255,0,0],[255,0,0],[0,0,0],[0,0,0],[255,0,0],[255,0,0],[255,128,0],[255,255,0],[255,0,0],[255,0,0],[0,0,0],[0,0,0],[255,0,0],[255,128,0],[255,255,255],[255,255,255],[255,0,0],[255,0,0],[0,0,0],[0,0,0],[255,0,0],[255,255,0],[255,255,255],[255,128,0],[255,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[255,0,0],[255,255,0],[255,0,0],[0,0,0],[0,0,0],[0,0,0]]
HumidityFace = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,0,0],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,255,255],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,255,255],[0,0,0],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,0,0],[0,255,255],[0,0,0],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,255,255],[0,255,255],[0,0,0],[0,0,0],[0,0,0]]
SickFace1 = [[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,128,0],[0,128,0],[0,0,0],[0,0,0],[0,128,0],[0,128,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
SickFace2 = [[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,128,0],[0,128,0],[0,0,0],[0,0,0],[0,128,0],[0,128,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,128,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
PlugFace = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,160],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,160],[0,0,0],[0,0,160],[0,0,0],[0,0,160],[0,0,0],[0,0,0],[0,0,160],[0,0,0],[0,0,160],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,160],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,160],[0,0,0],[0,0,160],[0,0,160],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,160],[0,0,160],[0,0,0],[0,0,0],[0,0,160],[0,0,160],[0,0,160],[0,0,160],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]


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

	def add(self, animation): # adds the animation designated by its precise String to its right level
		animationLevel = switcher1.get(animation)
		if (self._array[animationLevel][0] == None):
			self._array[animationLevel][0] = animation
		else:
			self._array[animationLevel][1] = animation

	def remove(self, animation):
		animationLevel = switcher1.get(animation)
		if (self._array[animationLevel][0] == animation):
			self._array[animationLevel][0] = self._array[animationLevel][1]
			self._array[animationLevel][1] = None
		else:
			self._array[animationLevel][1] = None

animationList = animationList()


#----------DETECTORS----------
temperatureTriggered, humidityTriggered, shakingTriggered = False
oldLength = -1


def check_temperature():
    temperature = sense.get_temperature()
	if (temperature >= 60 and temperatureTriggered == False): # corresponds to a new detection (some events can be detected and added but not instantly treated, because a higher priority event was added on top)
		animationList.add("temperature")
		temperatureTriggered = True

	elif (temperatureTriggered == True and temperature <= 55): # to avoid multiple consecutive triggers when temperature is switching around 60°C
			animationList.remove("temperature")
			temperatureTriggered = False

def checkShake()
  raw = sense.get_gyroscope_raw()
  rew = sense.get_accelerometer_raw()
  x = (raw['x'])
  y = (raw['y'])
  z = (raw['z'])
  a = (rew['x'])
  b = (rew['y'])
  c = (rew['z'])
  print(x)
  print(y)
  print(z)
  print(a)
  print(b)
  print(c)
  if (abs(x)>5 or abs(y)>5 or abs(z)>5) or (abs(a)>2 or abs(b)>2 or abs(c)>2):
  	return True
  else
    return False
  
def check_humidity():
	humidity = sense.get_humidity()
	if (humidity >= 100 and humidityTriggered == False): # arbitrary value of humidity for now
		animationList.add("humidity")
		humidityTriggered = True

	elif (humidityTriggered == True and humidity <= 95):
			animationList.remove("humidity")
			humidityTriggered = False


def check_shaking():
	shaking = checkShake()
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

def draw(content[]):
	currentTime = round(time.time()*10)
	alternator = currentTime - round(currentTime//10)*10 # gets tenth of a second

	if len(content[])==2:
		if (alternator < 5):
			singleAnimation = content[0]
		else:
			singleAnimation = content[1]
	else:
		singleAnimation = content[0]

	switcher2.get(singleAnimation)

def standFace(L1,S_hat): #This function change the Face to the L1, then light down ([0,0,0])
    pixels = S_hat.get_pixels()
    S_hat.set_pixels(L1)

    
    
def draw_default():
	standFace(DefaultFace,sense)


# def draw_inactive(): OPTIONNAL
# 	pass


def draw_reaction():
	standFace(PlugFace,sense)
	sleep(0.4)
	animationList.remove("plug")


def draw_temperature_warning():
	standFace(HeatFace)


def draw_humidity_warning():
	standFace(HumidityFace,sense)


def draw_shaking_warning():
	if (alternator < 5):
		standFace(SickFace1,sense)
	else:
		standFace(SickFace2,sense)


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