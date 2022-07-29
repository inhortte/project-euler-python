#!/usr/bin/env python

import itertools

single_digit = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["ten", "twenty", "thirty", "forty", "fifty", "sitxy", "seventy", "eighty", "ninety"]
teens = ["eleven", "twelve", "thir", "four", "fif", "six", "seven", "eigh", "nine"]
for idx, number_string in enumerate(teens):
    if idx > 1:
        teens[idx] = teens[idx] + "teen"

everything_to_99 = single_digit + [tens[0]] + teens
for idx, ten in enumerate(tens):
    if idx > 0:
        ten_group = [ten]
        for single in single_digit:
            ten_group += [ten + single]
        everything_to_99 += ten_group
        
sum = len("".join(everything_to_99)) * 10
def hundredify(s):
    return s + "hundred"
hundreds = [hundredify(s) for s in single_digit]
def andify(h, s):
    return h + "and" + s
def expand_hundred(s):
    return [s] + [andify(s, t) for t in everything_to_99]
hundreds_and_children = [expand_hundred(s) for s in hundreds]
hundreds_and_children = list(itertools.chain(*hundreds_and_children))
# print("hundreds: {}".format(hundreds_and_children))
everything = everything_to_99 + hundreds_and_children + ["onethousand"]
sum = len("".join(everything))

print("what have we here? {}".format(sum))
