#!/usr/bin/python

def shift_n_letters(letter, n):
	val = ord(letter) - ord('a') + n
	return chr(val%26+ ord('a'))

print 'val a = ', ord('a')
print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
