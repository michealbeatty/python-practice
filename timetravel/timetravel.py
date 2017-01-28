#!/usr/bin/env python3

import math

SPEED_OF_LIGHT = 299792458 # meters/second
SHIPS_WEIGHT = 70000

velocity = SPEED_OF_LIGHT * (50/100) # percentage of speed of light

factor = 1 / math.sqrt(1 - (velocity ** 2 / SPEED_OF_LIGHT ** 2))

print(factor)
print("Weight is ", SHIPS_WEIGHT * factor)
print("Time to Alpha Centauri: ", 4.3 / factor)
