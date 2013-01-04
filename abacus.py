#!/usr/bin/env python

pattern = '00000*****'
def print_abacus(value):
    for i in range(0, 10):
        print '|',
	sp = False
	for j in range (10):
	    if j == (10 - (value / 10**(9-i)  % 10)):
                print '   ',
		sp = True
            print pattern[j],
	if not sp: print '   ',

        print '|'

print_abacus(0)
print_abacus(1339)

