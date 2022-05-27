#!/usr/bin/env python

ans1 = sum(filter(lambda x: x % 5 == 0 or x % 3 == 0, range(0, 1000)))
print("ans1: " + str(ans1))

ans2 = sum(x for x in range(0, 1000) if x % 5 == 0 or x % 3 == 0)
print("ans2: " + str(ans2))
