from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)

sense.show_message("halo",
                   text_colour=(0,0,255), 
                   back_colour=(4, 34, 0),
                   scroll_speed = 0.05
                   )
sense.set_pixel(3,3, (116,255,231))

temp=sense.get_temperature()
pressure=sense.get_pressure()
humidity=sense.get_humidity()

sense.show_message("Temp",text_colour=(0,0,255), back_colour=(4, 34, 0),
                   scroll_speed = 0.05)
sense.show_message(str(round(temp, 1)),
                   text_colour=(0,0,255), 
                   back_colour=(4, 34, 0))

sense.show_message(str(round(pressure, 0)),
                   text_colour=(0,0,255), 
                   back_colour=(4, 34, 0))

sense.show_message(str(round(humidity, 0)),
                   text_colour=(0,0,255), 
                   back_colour=(4, 34, 0))
