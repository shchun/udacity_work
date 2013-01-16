#!/usr/bin/env python

def mode(L):
    G = {}
    for item in L:
        if item in G:
            G[item] += 1
        else:
            G[item] = 1
    
    print 'G=', G
    
    isfirst = 1
    for item in G:
	if isfirst:
            isfirst = 0
            maxval = G[item]
            maxkey = item

        if G[item] > maxval:
            maxval = G[item]
            maxkey = item
    return maxkey


L = [10, 4, 4, 5, 4, 5, 1, 4, 3, 8]
print 'mode = ', mode(L)
