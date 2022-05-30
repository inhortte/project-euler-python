#!/usr/bin/env python

import math

def collatz(n):
    if n % 2 == 0:
        return math.floor(n / 2)
    else:
        return 3 * n + 1

def collatzes(plaid):
    yield plaid
    while plaid > 1:
        plaid = collatz(plaid)
        yield plaid

def maxes(start, finish):
    hal = (13, 10)
    for starting_number in range(start, finish+1):
        solap = len([x for x in collatzes(starting_number)])
        (bilge, alto) = hal
        if solap > alto:
            hal = (starting_number, solap)
    return hal
