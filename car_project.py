#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor
from ev3dev2.sound import Sound
from time import sleep

from direction import Direction, LineSensor
from speed import getSpeed
from leds import LED

def line_detected(direction): 
    return direction > 10 or direction < -10

MAX_SPEED = 400

# DECLARACIONES

car_direction = Direction(LargeMotor(OUTPUT_D))
line_sensor = LineSensor(ColorSensor(INPUT_4), ColorSensor(INPUT_1))
leds = LED()
speed_motor = LargeMotor(OUTPUT_A)
us = UltrasonicSensor(INPUT_3)
us.mode='US-DIST-CM'
units=us.units
speed_reduction = 1
steering_block = 0
direction = 0
while True:
    provisional_direction = line_sensor.getMovement()
    direction = provisional_direction if steering_block < 3.5 else direction
    speed = getSpeed(us.value()/10)
    
    if line_detected(provisional_direction): # Detecta Línea
        steering_block = steering_block + 0.5 if steering_block + 0.5 <= 5 and (provisional_direction < -40 or provisional_direction > 40)  else steering_block
    elif not line_detected(provisional_direction): # No detecta línea
        steering_block = steering_block - 0.1 if steering_block  - 0.1 >= 0 else steering_block
    
    if line_detected(direction): # Detecta Línea
        speed_reduction = speed_reduction + 0.5 if speed_reduction + 0.5 <= 5 else speed_reduction
    elif not line_detected(direction): # No detecta línea
        speed_reduction = speed_reduction - 0.3 if speed_reduction - 0.3 >= 1 else speed_reduction
    
    speed = speed / speed_reduction
    speed_motor.run_forever(speed_sp = -MAX_SPEED*speed)
    car_direction.steerToDeg(direction)
    leds.updateLeds()
    