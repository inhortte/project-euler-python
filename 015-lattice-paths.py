#!/usr/bin/env python

def knees_that_jerk(x, y, limit_x, limit_y):
    nexts = []
    if x < limit_x:
        nexts.append((x+1, y))
    if y < limit_y:
        nexts.append((x, y+1))
    acc = 0
    for coords in nexts:
        acc += knees_that_jerk(coords[0], coords[1], limit_x, limit_y)
    if x == limit_x and y == limit_y:
        return acc + 1
    else:
        return acc
