#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
red = (100, 0, 255)
#sense.show_message("One small step for Pi!", text_colour=red)
sense.show_message("note!", text_colour=red)
