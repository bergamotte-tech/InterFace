from sense_hat import SenseHat

hat  = SenseHat()
hat.low_light = True
pixels = hat.get_pixels()
pixels[9] = [0,0,205]
pixels[14] = [0,0,205]
pixels[16] = [0,0,205]
pixels[18] = [0,0,205]
pixels[21] = [0,0,205]
pixels[23] = [0,0,205]
pixels[33] = [0,0,205]
pixels[38] = [0,0,205]
pixels[40] = [0,0,205]
pixels[41] = [0,0,205]
pixels[46] = [0,0,205]
pixels[47] = [0,0,205]
pixels[50] = [0,0,205]
pixels[51] = [0,0,205]
pixels[52] = [0,0,205]
pixels[53] = [0,0,205]
hat.set_pixels(pixels)