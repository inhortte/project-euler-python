#!/usr/bin/env python

import math

def test(primes, victim):
    for prime in primes:
        if victim % prime == 0:
            return False
    return True

def factors(n):
    primes = []
    current = 2
    while n > 1:
        if test(primes, current):
            primes.append(current)
            while n % current == 0:
                n = math.floor(n / current)
                yield current
        current += 1
