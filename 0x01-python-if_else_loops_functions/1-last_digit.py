#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rdr = number - (10 * int(number / 10))
if (number > 5):
    print(f"Last digit of {number} is {rdr} and is greater than 5")
if (number == 0):
    print(f"Last digit of {number} is {rdr} and is 0")
if (number < 6 and not number == 0):
    print(f"Last digit of {number} is {rdr} and is less than 6 and not 0")
