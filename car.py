from microbit import *
import radio

"""
This code is flashed on to the micro:bit embedded in the car

pin 1 = left motor
pin 2 = right motor

signals from the remote must be received 
"""

radio.on()
radio.config(power=7)
radio.config(channel=19)

speed_left = 0      # Speed of the right motor from 0 (off) to 100 (max)
speed_right = 0     # Speed of the right motor from 0 (off) to 100 (max)

delay_ms = 0

while True:
    acceleration_status = 0
    message_string_received = str(radio.receive())
    if message_string_received != "None":
        acceleration_status = float(message_string_received[3:])

        if acceleration_status > 0.5: acceleration_status = 0.5

        speed_left = (acceleration_status*200) * int(message_string_received[1])
        speed_right = (acceleration_status*200) * int(message_string_received[0])

        analogue_out_left = (speed_left * 1023)/100
        analogue_out_right = (speed_right * 1023)/100
        
        pin1.write_analog(analogue_out_left)
        pin2.write_analog(analogue_out_right)

    sleep(delay_ms)