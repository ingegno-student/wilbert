from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(0)

sense.show_message("halo",text_colour=(0,0,255), back_colour=(4, 34, 180))
sense.set_pixel(3,3, (116,255,231))
