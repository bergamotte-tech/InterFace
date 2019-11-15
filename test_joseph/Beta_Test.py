from sense_hat import SenseHat
import time

def checkTemperature() :
	temp = hat.get_temperature()
	temp = round(temp, 1)
	return temp

hat  = SenseHat()
hat.low_light = True
defaut=[[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[0,255,0],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[0,255,0],[255,255,255],[255,255,255],[0,255,0],[0,255,0],[255,255,255],[255,255,255],[0,255,0],[0,255,0],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[0,255,0],[0,255,0],[0,255,0],[0,255,0],[0,255,0],[0,255,0],[255,255,255],[255,255,255],[0,255,0],[255,255,255],[0,255,0],[255,255,255],[0,255,0],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255]]
hot = [[255,255,255],[255,255,255],[255,0,0],[255,128,0],[255,255,255],[255,255,255],[255,128,0],[255,255,255],[255,255,255],[255,255,255],[255,0,0],[255,255,255],[255,255,255],[255,0,0],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,0,0],[255,128,0],[255,128,0],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,0,0],[255,128,0],[255,255,0],[255,128,0],[255,0,0],[255,255,255],[255,255,255],[255,255,255],[255,0,0],[255,255,0],[255,255,0],[255,255,0],[255,128,0],[255,0,0],[255,255,255],[255,255,255],[255,0,0],[255,128,0],[255,255,0],[255,255,0],[255,128,0],[255,0,0],[255,255,255],[255,0,0],[255,128,0],[255,128,0],[255,255,0],[255,128,0],[255,128,0],[255,0,0],[255,255,255],[255,255,255],[255,0,0],[255,128,0],[255,128,0],[255,0,0],[255,0,0],[255,255,255],[255,255,255]]
happy = [[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[24,13,242],[24,13,242],[255,255,255],[255,255,255],[24,13,242],[24,13,242],[255,255,255],[255,255,255],[24,13,242],[24,13,242],[255,255,255],[255,255,255],[24,13,242],[24,13,242],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[24,13,242],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[24,13,242],[255,255,255],[255,255,255],[255,255,255],[24,13,242],[24,13,242],[24,13,242],[24,13,242],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[255,255,255]]
cold = [[255,255,255],[255,255,255],[255,255,255],[255,255,255],[97,224,218],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[97,224,218],[255,255,255],[97,224,218],[97,224,218],[255,255,255],[255,255,255],[97,224,218],[255,255,255],[255,255,255],[255,255,255],[97,224,218],[97,224,218],[97,224,218],[255,255,255],[255,255,255],[97,224,218],[255,255,255],[97,224,218],[97,224,218],[97,224,218],[97,224,218],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[97,224,218],[97,224,218],[97,224,218],[97,224,218],[97,224,218],[255,255,255],[255,255,255],[255,255,255],[97,224,218],[97,224,218],[97,224,218],[97,224,218],[97,224,218],[255,255,255],[97,224,218],[255,255,255],[97,224,218],[97,224,218],[97,224,218],[97,224,218],[97,224,218],[255,255,255],[255,255,255],[255,255,255],[255,255,255],[97,224,218],[97,224,218],[255,255,255],[255,255,255],[255,255,255]]
tempHot = False
tempCold = False
aChange = False
hat.set_pixels(defaut)
while True :
	temperature = checkTemperature()
	if (temperature>30 and aChange == False) :
		tempHot = True
		tempCold = False
	elif(temperature<10 and aChange == False) :
		tempHot = False
		tempCold = True
	else :
		tempHot = False
		tempCold = False
	print(temperature)
	timeout = time.time()+5
	time.sleep(5)

	if (tempHot == True) :
		hat.clear()
		hat.set_pixels(hot)
		aChange = True
	elif(tempCold == True) :
		hat.clear()
		hat.set_pixels(cold)
		aChange = True
	else:
		hat.clear()
		hat.set_pixels(defaut)
		aChange = False
