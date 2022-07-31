#!/usr/bin/env python

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_year(year):
    summation = sum(days_per_month)
    if year % 4 == 0:
        summation = summation + 1
        if year % 100 == 0 and year % 400 > 0:
            summation = summation - 1
    return summation

def first_of_months(first_day, year):
    total_days = days_in_year(year)
    leap_year = total_days == 366
    firsts = [first_day]
    current = first_day
    for days in days_per_month:
        current = (current + days) % 7
        if leap_year and days == 28:
            current = (current + 1) % 7
        firsts = firsts + [current]
    first_of_next_year = firsts.pop()
    return firsts, first_of_next_year

_, first_day_of_1901 = first_of_months(0, 1900)

current_first_day = first_day_of_1901
sundays = 0
for year in range(1901, 2001):
    days_list, current_first_day = first_of_months(current_first_day, year) 
    sundays = sundays + len([d for d in days_list if d == 6]) 

print("number of sundays: {}".format(sundays))
