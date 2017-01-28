#!/usr/bin/env python3


def calc(richter_value):
    tnt_ton = 4.184e9
    energy = 10 ** ((1.5 * richter_value) + 4.8)
    tons = energy / tnt_ton
    return energy, tons


def main():
    print("Richter\t\tJoules\t\tTons")

    for r_value in richter_values:
        energy, tons = calc(r_value)
        joules_string = "{:.6e}".format(energy)
        tons_string = "{:.6e}".format(tons)
        full_string = "{}\t\t\t{}\t{}".format(r_value, joules_string, tons_string)
        print(full_string)

    num_str = input("Please enter a Richter scale value: ")
    float_str = float(num_str)
    energy, tons = calc(float_str)
    print("Richter scale value: ", float_str)
    print("Equivalence in joules: {:6e}".format(energy))
    print("Equivalence in tons of TNT: {:6e}".format(tons))

if __name__ == '__main__':
    richter_values = [1.0, 5.0, 9.1, 9.2, 9.5]
    main()
