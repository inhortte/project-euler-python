#!/usr/bin/env python

def chuck(n):
    for x in range(11, 21):
        if n % x != 0:
            return False
    return True

def g():
    bork = 21
    while True:
        if chuck(bork):
            yield bork
            break
        bork += 1

def buttock():
    y = 20
    x_list = range(1, y)
    captured = []
    while y > 0:
        x_list = [x for x in x_list if y % x != 0]
        print("y: " + str(y) + "\nx_list: " + str(x_list)) 
        if len(x_list) > 0:
            captured.append(y)
        y -= 1
    print("captured: " + str(captured))
