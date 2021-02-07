from microbit import *

degrees = input.compass_heading()
if (degrees < 45):
   basic.show_string("N")
elif (degrees >=45) and (degrees<135):
   basic.show_string("E")
elif (degrees >=135) and (degrees<225):
    basic.show_string("S")
elif (degrees > 225):
    basic.show_string("W")
else:
    basic.show_string("N")