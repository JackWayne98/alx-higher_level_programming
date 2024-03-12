#!/usr/bin/python3
for ltr in range(97, 123):
    if not chr(ltr) == 'q' and not chr(ltr) == 'e':
        print("{}".format(chr(ltr)), end="")
