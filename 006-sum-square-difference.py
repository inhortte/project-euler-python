#!/usr/bin/env python

import math

def square_of_sum():
    return math.floor(math.pow(sum(range(1, 101)), 2))

def add_the_squares():
    inception = square_of_sum()
    for x in range(1, 101):
        inception -= math.pow(x, 2)
    print("yup: " + str(inception))
