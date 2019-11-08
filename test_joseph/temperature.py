from sense_hat import SenseHat

def tempa(color) :
	global hat
	pixels = hat.get_pixels()
	pixels[9] = color
	pixels[14] = color
	pixels[16] = color
	pixels[18] = color
	pixels[21] = color
	pixels[23] = color
	pixels[33] = color
	pixels[38] = color
	pixels[40] = color
	pixels[41] = color
	pixels[46] = color
	pixels[47] = color
	pixels[50] = color
	pixels[51] = color
	pixels[52] = color
	pixels[53] = color
	hat.set_pixels(pixels)
	
hat = SenseHat()
hat.clear()
hat.low_light = True
pixels = hat.get_pixels()

temp = hat.get_temperature()
color=[0,0,0]
if (temp>20) :
  color=[255,0,0]
  tempa(color)
else :
  color=[0,0,205]
  tempa(color)
print(temp)


