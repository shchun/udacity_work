#!/usr/bin/env python


def centrality_max(G, v):
    open_list = [v]
    current_level_list = open_list[:]
    visited = []
    centrality = 0 

    while len(open_list) > 0:
        node = open_list.pop(0)
        visited.append(node)

	print 'open_list=', open_list
	print 'node=', node, 'curr =', current_level_list

        if node not in current_level_list:
	    print 'current_level_list=', current_level_list, ', node=', node
            centrality += 1
            current_level_list = open_list[:]

	for neighbor in G[node]:
            if neighbor not in visited:
                open_list.append(neighbor)

    print 'centrality_max = ', centrality
    return centrality

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
    chain = ((1,2), (2,3), (3,4), (4,5), (5,6))
    G = {}
    for n1, n2 in chain:
        make_link(G, n1, n2)
    assert centrality_max(G, 1) == 5
    assert centrality_max(G, 3) == 3
    tree = ((1, 2), (1, 3),
            (2, 4), (2, 5),
            (3, 6), (3, 7),
            (4, 8), (4, 9),
            (6, 10), (6, 11))
    G = {}
    for n1, n2 in tree:
        make_link(G, n1, n2)
    assert centrality_max(G, 1) == 3
    assert centrality_max(G, 11) == 6

test()
