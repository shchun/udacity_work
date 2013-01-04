#!/usr/bin/env python


def rec_naive(a,b):
	if a == 0:
		return 0
	print 'addition!!'
	return b + rec_naive(a-1, b)

rec_naive(17,6)
