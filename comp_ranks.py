#!/usr/bin/env python

def is_reciproval(graph, origin, current, depth):
	#print 'is_reciproval =', origin, current, depth	
	if depth <= 0:
		if origin == current:
			return True
		else:
			return False

	#print 'current =', current, 'link =', graph[current]
	for node in graph[current]:
		if is_reciproval(graph, origin, node, depth-1):
			return True
	return False

def compute_ranks(graph, k):
    d = 0.8 # damping factor
    numloops = 10
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    if not is_reciproval(graph, node, page, k):
                    	newrank = newrank + d * (ranks[node]/len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


# For example

g = {'a': ['a', 'b', 'c'], 'b':['a'], 'c':['d'], 'd':['a']}

print compute_ranks(g, 0) # the a->a link is reciprocal
#>>> {'a': 0.26676872354238684, 'c': 0.1216391112164609,
#     'b': 0.1216391112164609, 'd': 0.1476647842238683}
print compute_ranks(g, 1)
print compute_ranks(g, 2)


if False:
	#print is_reciproval(g, 'a', 'a', 0)
	#print is_reciproval(g, 'b', 'a', 0)
	#print is_reciproval(g, 'b', 'a', 1)

	print 'aaa1=', is_reciproval(g, 'c', 'b', 0);
	print 'aaa2=', is_reciproval(g, 'c', 'b', 1);
	print 'aaa3=', is_reciproval(g, 'c', 'b', 2);
	print 'aaa4=', is_reciproval(g, 'c', 'b', 3);
