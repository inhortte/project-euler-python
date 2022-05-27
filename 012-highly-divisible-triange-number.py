#!/usr/bin/env python

import math

def triangle(limit):
    n = 1
    c = 2
    while n < limit:
        yield (n, number_of_divisors(n))
        n = n + c
        c += 1

def divisible(numbers, victim):
    for x in numbers:
        if victim % x == 0:
            return True
    return False

def next_prime(primes, current_prime):
    for n in range(current_prime + 1, current_prime * 2):
        if not divisible(primes, n):
            return (primes + [n], n)
    return (primes, current_prime)

def update_fact_map(fact_map, n):
    update = {n: 1}
    for k in fact_map:
        if k == n:
            update = {n: fact_map.get(n) + 1}
            break
    fact_map.update(update)
    return fact_map

def prime_factors(n):
    primes = [2]
    current_prime = 2
    fact_map = {}
    while n > 1:
        if n % current_prime == 0:
            n = math.floor(n / current_prime)
            fact_map = update_fact_map(fact_map, current_prime)
        else:
            (primes, current_prime) = next_prime(primes, current_prime)
    return fact_map

def number_of_divisors(n):
    divisors = 1
    for n in prime_factors(n).values():
        divisors = divisors * (n + 1)
    return divisors

    
