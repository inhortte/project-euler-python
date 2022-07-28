#!/usr/bin/env python

import math

power = str(2 ** 1000)
sum = 0
while len(power) > 0:
    digit = int(power[0:1])
    sum = sum + digit
    power = power[1:]

print("the sum: " + str(sum))
