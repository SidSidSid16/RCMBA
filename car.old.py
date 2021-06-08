from microbit import *

"""
This code is flashed on to the micro:bit embedded in the car

pin 0 = left motor
pin 1 = right motor

signals from the remote must be recieved by the car and must be decoded by the
car.
steering signal = -100 (full left) and +100 (full right)
throttle signal = 0 (no throttle) and 100 (full throttle)
"""

throttle = 0        # Speed which the remote is outputting from 0 (off) to 100 (max)
speed_left = 0      # Speed of the right motor from 0 (off) to 100 (max)
speed_right = 0     # Speed of the right motor from 0 (off) to 100 (max)
steering = 0        # Steering from -100 (left) to 100 (right)

def set_turning_speed_bias():
    """
    This function uses the steering value to offset the left and right motor
    speeds.
    
    When steering is set to 1, the car will turn slightly right. The right 
    motor will be 1% higher than the inteded speeds (value from the remote)
    and the left motor will be 1% lower than the intended speed (value from the
    remote)
    
    When a motor speed is calculated to be above 100 (1023) then that motor
    will be set to 100 and the other will be set to 0.
    """
    
    if steering > 0:    # car will turn right for positive steering values
        new_speed_right = speed_right - ((speed_right/100)*steering)
        new_speed_left = speed_left + ((speed_left/100)*steering)
        
    if steering < 0:    # car will turn left for negative steering values
        new_speed_right = speed_right + ((speed_right/100)*steering)
        new_speed_left = speed_left - ((speed_left/100)*steering)
        
    if new_speed_right > 100:  # if the new calculated speed is more than 100%
        new_speed_right = 100  # then the motor will be set 100% and the other 
        new_speed_left = 0     # motor is set to 0%    
        
    if new_speed_left > 100:   # if the new calculated speed is more than 100%
        new_speed_right = 0    # then the motor will be set 100% and the other 
        new_speed_left = 100   # motor is set to 0%    

    if new_speed_right < 0:    # if the new calculated speed is more than 100%
        new_speed_right = 0    # then the motor will be set 100% and the other 
        new_speed_left = 100   # motor is set to 0%    
        
    if new_speed_left < 0:     # if the new calculated speed is more than 100%
        new_speed_right = 100  # then the motor will be set 100% and the other 
        new_speed_left = 0     # motor is set to 0%  
        
    speed_left = new_speed_left
    speed_right = new_speed_right

while True:
    analogue_out_left = (speed_left * 1023)/100
    analogue_out_right = (speed_right * 1023)/100
    pin0.write_analog(analogue_out_left)
    pin1.write_analog(analogue_out_right)

