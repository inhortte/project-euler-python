#!/usr/bin/env python

leper = [(a, b, c) for c in range(1, 1000) for b in range(2, c) for a in range(1, b) if a + b + c == 1000 and a*a + b*b == c*c]
(a, b, c) = leper[0]
print("ans: " + str(a * b * c))
