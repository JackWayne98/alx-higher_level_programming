#!/usr/bin/python3
def print_last_digit(number):
    print("{}".format(abs((number - (10 * int(number / 10))))), end="")
    return abs((number - (10 * int(number / 10))))
