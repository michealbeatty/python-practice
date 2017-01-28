#!/usr/bin/env python3

import math

SPEED_OF_LIGHT = 299792458 # meters/second
SHIPS_WEIGHT = 70000

ALPHA_CENTAURI = 4.3
BARNARDS_STAR = 6.0
BETELGEUSE = 309
ANDROMEDA_GALAXY = 2000000


def calculate_factor(vel):
    if vel < 100:
        velocity = SPEED_OF_LIGHT * (vel/100)
    else:
        velocity = 1
    factor = 1 / math.sqrt(1 - (velocity ** 2 / SPEED_OF_LIGHT ** 2))
    return factor

def calculate_weight(fact):
    return SHIPS_WEIGHT * fact


def calculate_travel(fact, light_years):
    return light_years / fact

def main():

    velocity_str = input("Please enter velocity (percentage of speed of light): ")
    velocity_float = float(velocity_str)
    factor = calculate_factor(velocity_float)

    print("Weight is ", calculate_weight(factor))
    print("Perceived travel time to Alpha Centauri: ", calculate_travel(factor, ALPHA_CENTAURI))
    print("Perceived travel time to Barnard's Star: ", calculate_travel(factor, BARNARDS_STAR))
    print("Perceived travel time to Betelgeuse: ", calculate_travel(factor, BETELGEUSE))
    print("Perceived time to travel to Andromeda Galaxy", calculate_travel(factor, ANDROMEDA_GALAXY))


if __name__ == '__main__':
    main()
