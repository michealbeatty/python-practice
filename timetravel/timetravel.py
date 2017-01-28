#!/usr/bin/env python3

import math

SPEED_OF_LIGHT = 299792458 # meters/second
SHIPS_WEIGHT = 70000

ALPHA_CENTAURI = 4.3
BARNARDS_STAR = 6.0
BETELGEUSE = 309
ANDROMEDA_GALAXY = 2000000


def main():
    velocity_str = input("Please enter velocity (percentage of speed of light): ")
    velocity_float = float(velocity_str)

    velocity = SPEED_OF_LIGHT * (velocity_float/100)

    factor = 1 / math.sqrt(1 - (velocity ** 2 / SPEED_OF_LIGHT ** 2))

    print(factor)
    print("Weight is ", SHIPS_WEIGHT * factor)
    print("Perceived travel time to Alpha Centauri: ", ALPHA_CENTAURI / factor)
    print("Perceived travel time to Barnard's Star: ", BARNARDS_STAR / factor)
    print("Perceived travel time to Betelgeuse: ", BETELGEUSE/ factor)
    print("Perceived time to travel to Andromeda Galaxy", ANDROMEDA_GALAXY / factor)


if __name__ == '__main__':
    main()