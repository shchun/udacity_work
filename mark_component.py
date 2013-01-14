#!/usr/bin/env python

def mark_component(G, node, marked):
    marked[node] = True
    total_marked = 0
    open_list = [node]

    while len(open_list) > 0:
	print 'open_list = ', open_list
	cur = open_list.pop(0)
    	marked[cur] = True
        total_marked += 1
	for i in G[cur]:
            if i not in marked:
                open_list.append(i)

    print 'total_marked = ', total_marked
    print 'marked = ', marked
    return total_marked

#########
# Code for testing
#
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def test():
    test_edges = [(1, 2), (2, 3), (4, 5), (5, 6)]
    G = {}
    for n1, n2 in test_edges:
        make_link(G, n1, n2)
    marked = {}
    assert mark_component(G, 1, marked) == 3
    assert 1 in marked
    assert 2 in marked
    assert 3 in marked
    assert 4 not in marked
    assert 5 not in marked
    assert 6 not in marked

test()
