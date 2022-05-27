#!/usr/bin/env python

def sum_even_fibs(thurk):
    tup, acc = [thurk[k] for k in ('tup', 'acc')]
    siguiente = tup[0] + tup[1]
    if siguiente > 4000000:
        print("The first fib to exceed 4000000 is " + str(siguiente) + " and our sum is " + str(acc))
        return acc
    else:
        if siguiente % 2 == 0:
            acc += siguiente
        new_thurk = {'tup': (tup[1], siguiente), 'acc': acc}
        return(sum_even_fibs(new_thurk))

def even_leprosy(topple):
    tup = (1, 1)
    acc = 0
    siguiente = 0
    while siguiente < topple:
        if siguiente % 2 == 0:
            acc += siguiente
        siguiente = tup[0] + tup[1]
        tup = (tup[1], siguiente)
        yield (siguiente, acc)

ans1 = [x for x in even_leprosy(4000000)]
print("ans1: " + str(ans1))
