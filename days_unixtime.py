#!/usr/bin/env python
import time

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    t1 = (year1, month1, day1, 0, 0, 0, 0, 0, 0)
    #t1 = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
    print 't1=', t1
    t2 = (year2, month2, day2, 0, 0, 0, 0, 0, 0)
    sec1 = time.mktime(t1)
    sec2 = time.mktime(t2)
    
    return (sec2-sec1)/(60*60*24)

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

