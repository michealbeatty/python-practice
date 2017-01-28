#!/usr/bin/env python3
"""windchill takes a temperature and a windspeed and returns the windchill"""
# pylint: disable=C0103


def calculate_windchill(temp, wind):
    """calculate_windchill returns the wind chill for the given temperaturea
    and wind speed"""
    wc = 35.74 + 0.6215 * temp - (35.75 * (wind**0.16)) + 0.4275 * (temp * (wind**0.16))
    return wc


def main():
    wind_chill = calculate_windchill(temperature, wind_speed)
    print("Wind chill is {:.1f}".format(wind_chill))

    temp_str = input("Please enter the temperature: ")
    temp_float = float(temp_str)

    speed_str = input("Please enter the wind speed: ")
    speed_float = float(speed_str)

    wind_chill = calculate_windchill(temp_float, speed_float)
    print("Wind chill is {:.1f}".format(wind_chill))

if __name__ == '__main__':
    temperature = 26.0
    wind_speed = 9
    main()
