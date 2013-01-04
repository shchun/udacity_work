#!/usr/bin/env python


def get_all_node(graph):
	allnode = set([]) 
	for edge in graph:
		allnode.add(edge[0])
		allnode.add(edge[1])

	return list(allnode)

def find_eulerian_tour(graph):
	eulpath = []
	odd_node = []
	tour = []

	allnode = get_all_node(graph)
	print 'allnode = ', allnode

	# make node - degree dictionary
	degrees = get_degree(graph)

	# for each odd degree node
	for node in allnode:
		if degrees[node] % 2 == 1: # odd
			odd_node.append(node)

	print 'odd node = ',  odd_node		
	if len(odd_node) == 0: # all even degree node
		return get_path_for_nodes(graph, allnode[0])
	elif len(odd_node) == 2: # 2 odd degree node
		return get_path_for_nodes(graph, odd_node[0])

	else:
		return None	
		# if no odd degree -> exit

		# if 2 odd degree -> make tour starting one of odd degreed node

		# if >2 odd degree -> None
def get_path_for_nodes(tour, start):
    """return the set of nodes reachable from
    the first node in `tour`"""
    a = start
    nodes = set([a])
    explore = set([a])
    while len(explore) > 0:
        # see what other nodes we can reach
        b = explore.pop()
        for t in tour:
            node = check_edge(t, b, nodes)
            if node is None:
                continue
            nodes.add(node)
            explore.add(node)
    return nodes

def get_degree(tour):
    degree = {}
    for x, y in tour:
        degree[x] = degree.get(x, 0) + 1
        degree[y] = degree.get(y, 0) + 1
    return degree

def check_edge(t, b, nodes):
    """
    t: tuple representing an edge
    b: origin node
    nodes: set of nodes already visited

    if we can get to a new node from `b` following `t`
    then return that node, else return None
    """
    if t[0] == b:
        if t[1] not in nodes:
            return t[1]
    elif t[1] == b:
        if t[0] not in nodes:
            return t[0]
    return None

def create_tour(nodes):
    # your code here
    print 'nodes = ', nodes
    tour = []
    nodes_len = len(nodes)
    for i in range(nodes_len):
        tour.append( (nodes[i], nodes[(i+1)% nodes_len]) )
        
    print 'tour = ', tour
    return tour

def connected_nodes(tour):
    """return the set of nodes reachable from
    the first node in `tour`"""
    a = tour[0][0]
    nodes = set([a])
    explore = set([a])
    while len(explore) > 0:
        # see what other nodes we can reach
        b = explore.pop()
        for t in tour:
            node = check_edge(t, b, nodes)
            if node is None:
                continue
            nodes.add(node)
            explore.add(node)
    return nodes

def is_eulerian_tour(nodes, tour):
    # all nodes must be even degree
    # and every node must be in graph
    degree = get_degree(tour)
    for node in nodes:
        try:
            d = degree[node]
            if d % 2 == 1:
                print "Node %s has odd degree" % node
                return False
        except KeyError:
            print "Node %s was not in your tour" % node
            return False
    connected = connected_nodes(tour)
    if len(connected) == len(nodes):
        return True
    else:
        print "Your graph wasn't connected"
        return False

def test():
	#a_graph = [(1, 2), (2, 3), (3, 1)]
	a_graph = [(1, 2), (2, 3), (3, 1), (3, 4)]
	print find_eulerian_tour(a_graph)
    
test()
