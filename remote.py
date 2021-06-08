from microbit import *
import radio

"""
This code is flashed on to the micro:bit embedded in the remote
"""

radio.on()
radio.config(channel=19)
radio.config(power=7)

delay_ms = 0

def checkTurnButton():
    turn_status = ""
    """
    Check if the left or right turn button is pressed

    A + B = 11
    A     = 10 (left button)
    B     = 01 (right button)
    """
    if button_a.is_pressed():   # turn left
        turn_status = turn_status + "1"
    else:
        turn_status = turn_status + "0"

    if button_b.is_pressed():   # turn right
        turn_status = turn_status + "1"
    else:
        turn_status = turn_status + "0"
        
    if turn_status == "00":
        turn_status = "11"
    
    return turn_status          # 2 bits

def retrieveAccelerometerValues():
    """
    Retrieves the accelerometer values for car's acceleration
    then normalises.

    Normalisation = Y_norm = (Y-Y_max)/(Y_max-Y_min)

    Full forward = Y_max = -1024
    Full back    = Y_min = 1024

    Range of normalised values:
        microbit full forward tilt      = 1
        microbit parallel to the ground = 0.5
        microbit full backwards tilt    = 0
    """
    Y = accelerometer.get_y()
    Y_norm = (Y - 1024)/(-2048)

    if Y_norm < 0.1: Y_norm = 0.0100

    return str(Y_norm)[:4]     # 4 characters x.xx

while True:
    """
    Main loop
        1 - see if the turn right/left button is pressed
        2 - retrieve the values from the accelerometer
        3 - scale down the accelerometer values
        4 - send to the car
    """
    message_string = ""     # [left/right][accelerometer]
    message_string = str(checkTurnButton()) + str(retrieveAccelerometerValues())
    radio.send(message_string)
    sleep(delay_ms)
