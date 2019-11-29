from sense_hat import SenseHat
from time import sleep

import time

s = SenseHat()
test = True

while test:
  sense = SenseHat()
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
  if (abs(x)>8 or abs(y)>8 or abs(z)>8) and(abs(a)>3 or abs(b)>3 or abs(c)>3):
  	shakingTrigger = True
  print("")
  sleep(0.1)
  


