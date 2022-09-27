#!env python

import math

def head(list):
    return list[0]

def tail(list):
    if len(list) == 1:
        return []
    return list[1:]

def combs(list):
    if len(list) == 0:
        return [[]]
    #if len(list) == 1:
        #return [list]
    head_combs = []
    tail_combs = combs(tail(list))
    for comb in tail_combs:
        head_combs += [[head(list)] + comb]
    return head_combs + tail_combs

def prod(ns):
    if len(ns) == 0:
        return 0
    p = 1
    for i in ns:
        p = p * i
    return p

def prods(list_of_combs):
    return [prod(c) for c in list_of_combs]

def contains(x, arr):
    for y in arr:
        if x == y:
            return True
    return False

def primes(victim):
    ps = []
    prime = 2
    n = victim
    while prime <= math.floor(victim / 2):
        while(n % prime == 0):
            ps += [prime]
            n = math.floor(n / prime)
        prime += 1
    return ps

def divisors(victim):
    ps = primes(victim)
    cs = combs(ps)
    ds = [1]
    for d in prods(cs):
        if d > 0 and d != victim and not contains(d, ds):
            ds += [d]
    return ds

def sum_of_divisors(victim):
    return sum(divisors(victim))

def add_if_not_present(arr, n):
    if not contains(n, arr):
        return arr + [n]
    return arr

def not_exactly_amicables(limit):
    where_are_we = 2
    sum_map = {}
    while where_are_we < limit:
        s = sum_of_divisors(where_are_we) 
        if sum_map.get(s):
            sum_map[s] = add_if_not_present(sum_map[s], where_are_we)
        else:
            sum_map[s] = [where_are_we]
        where_are_we += 1
    amicable_numbers = []
    for s in sum_map.keys():
        ns = sum_map[s]
        if len(ns) == 2:
            for n in ns:
                amicable_numbers = add_if_not_present(amicable_numbers, n)
    return amicable_numbers

def amicables(limit):
    current = 2
    anums = []
    while current < limit:
        if not contains(current, anums):
            s = sum_of_divisors(current)
            if not s == current and sum_of_divisors(s) == current:
                anums = anums + [current, s]
        current += 1
    return anums
