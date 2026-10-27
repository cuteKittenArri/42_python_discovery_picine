#!/usr/bin/env python3
number = float(input("Give me a number: "))
if number % 1 == 0:
    print(round(number))
else:
    print(round(number) + 1)
