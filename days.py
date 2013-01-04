#!/usr/bin/env python
import time

daysForMonth = (31,28,31,30,31,30,31,31,30,31,30,31)
daysForMonthLeap = (31,29,31,30,31,30,31,31,30,31,30,31)

def isLeapYear(year):
    if (year%400) == 0:
        return True
    elif (year%100) == 0:
        return False
    elif (year%4) == 0:
        return True
    return False

def daysForYear(year):
    if isLeapYear(year):
        return 366
    return 365

def daysByMonthForYear(year, month):
    day = 0
    if isLeapYear(year):
        for m in range(1, month):
            day += daysForMonthLeap[m-1]
    else:
        for m in range(1, month):
            day += daysForMonth[m-1]
    return day   

def daysByYear(year):
    day = 0
    for y in range(1900, year):
        day += daysForYear(y)
    return day

def daysByYearAndMonthAndDay(year, month, day):
    ret = 0
    ret += daysByYear(year)
    ret += daysByMonthForYear(year, month)
    ret += day
    return ret

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    t1 = daysByYearAndMonthAndDay(year1, month1, day1)
    t2 = daysByYearAndMonthAndDay(year2, month2, day2)
    return t2- t1
# Test routine
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
