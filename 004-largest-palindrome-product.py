#!/usr/bin/env python

import math

def is_palindrome(n):
    if n < 10:
        return True
    limit = math.ceil(math.log10(n) / 2)
    # print("initial limit -> " + str(limit))
    while limit > 0:
        lsd = n % 10;
        # print("lsd: " + str(lsd))
        n = math.floor(n / 10)
        gsd = math.floor(n / math.pow(10, math.floor(math.log10(n))))
        # print("gsd: " + str(gsd))
        if lsd != gsd:
            return False
        m = n - math.floor(gsd * math.pow(10, math.floor(math.log10(n))))
        if m == 0:
            return True
        n_order = math.floor(math.log10(n))
        m_order = math.floor(math.log10(m))
        if n_order - m_order > 1:
            while n_order - 1 > m_order:
                if m % 10 != 0:
                    return False
                n_order -= 1
                m = math.floor(m / 10)
        n = m
        # print("new n: " + str(n))
        if n < 10:
            return True
        else:
            limit = math.ceil(math.log10(n) / 2)
            # print("new limit: " + str(limit) + "\n")
    return True

def dual_countdown(jen_high=999, jen_low=100, taf_high=999, taf_low=100):
    orig_taf_high = taf_high
    while jen_high >= jen_low:
        while taf_high >= taf_low:
            product = jen_high * taf_high;
            if is_palindrome(product):
                yield product
            taf_high -= 1
        taf_high = orig_taf_high    
        jen_high -= 1

