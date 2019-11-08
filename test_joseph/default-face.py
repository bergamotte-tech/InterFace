from sense_hat import SenseHat

hat  = SenseHat()
hat.low_light = True
pixels = hat.get_pixels()
pixels[17] = [0,0,205]
pixels[18] = [0,0,205]
pixels[21] = [0,0,205]
pixels[22] = [0,0,205]
pixels[42] = [0,0,205]
pixels[43] = [0,0,205]
pixels[44] = [0,0,205]
pixels[45] = [0,0,205]
hat.set_pixels(pixels)