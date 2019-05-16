#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import UltrasonicSensor, ColorSensor
from ev3dev2.sound import Sound
from time import sleep

from direction import Direction, LineSensor
from speed import getSpeed
from leds import LED

MAX_SPEED = 750

# DECLARACIONES

car_direction = Direction(LargeMotor(OUTPUT_D))
line_sensor = LineSensor(ColorSensor(INPUT_4), ColorSensor(INPUT_1))
leds = LED()
speed_motor = LargeMotor(OUTPUT_A)
us = UltrasonicSensor(INPUT_3)
us.mode='US-DIST-CM'
units=us.units
speed_reduction = 1
while True:
    direction = line_sensor.getMovement()
    print(direction)
    speed = getSpeed(us.value()/10)
    if (direction > 10 or direction < -10) and speed_reduction < 5:
        speed_reduction += 0.5
    elif direction < 10 and direction > -10 and speed_reduction > 1:
        speed_reduction -= 0.25
    speed = speed / speed_reduction
    #print(speed_reduction)
    speed_motor.run_forever(speed_sp = -(MAX_SPEED*speed)/ 2)
    car_direction.steerToDeg(direction)
    leds.updateLeds()
    