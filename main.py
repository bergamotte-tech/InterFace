
#----------IMPORTS----------
		# /!\ TO MINIMZE /!\
import os
import time

#----------DETECTORS----------
temperatureTriggered, humidityTriggered, shakingTriggered = False
oldUsbList = []
oldLength = -1


def check_temperature():
	# temperature = get temperature
	if (temperature >= 60 temperatureTriggered == False): # corresponds to a new detection (some events can be detected and added but not instantly treated, because a higher priority event was added on top)
		animationList.add("temperature")
		temperatureTriggered = True

	elif (temperatureTriggered == True and temperature <= 55): # to avoid multiple consecutive triggers when temperature is switching around 60°C
			animationList.remove("temperature")
			temperatureTriggered = False


def check_humidity():
	# humidity = get humidity
	if (humidity >= 100 and humidityTriggered == False): # arbitrary value of humidity for now
		animationList.add("humidity")
		humidityTriggered = True

	elif (humidityTriggered == True and humidity <= 95):
			animationList.remove("humidity")
			humidityTriggered = False


def check_shaking():
	# shaking = get shaking value --> we can create it gathering different indicators if needed
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
			self._array[animationLevel][0] = None
		else:
			self._array[animationLevel][1] = None



#----------DRAW----------
alternator = 0
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


def draw_default():
	# draw face


# def draw_inactive(): OPTIONNAL
# 	pass


def draw_reaction():
	# draw face for .4s
	animationList.remove("plug")


def draw_temperature_warning():
	# draw face


def draw_humidity_warning():
	# draw face


def draw_shaking_warning():
	if (alternator < 5):
		# draw face 1
	else:
		# draw face 2


#----------ON/OFF----------
started = False

def start():
	if not(started):
		# create a new thread
		# create a new animationList
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
		#kill the threads and reset the changes (leds...)
		started = False
	else:
		print("Program not started yet")