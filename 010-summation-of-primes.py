#!/usr/bin/env python

import math

def is_prime(primes, n):
    halt = math.sqrt(n)
    for p in primes:
        if p > halt:
            break
        if n % p == 0:
            return False
    return True

def sum_primos(halt):
    primes = [2]
    current = 3
    sum = 2
    while current < halt:
        if is_prime(primes, current):
            primes.append(current)
            sum += current
        current += 1
    return sum

