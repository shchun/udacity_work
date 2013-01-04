#!/usr/bin/env python


def get_all_node(graph):
	allnode = set([]) 
	for edge in graph:
		allnode.add(edge[0])
		allnode.add(edge[1])

	return allnode

def find_eulerian_tour(graph):
	eulpath = []
	odd_node = []
	tour = []

	allnode = get_all_node(graph)
	#print 'allnode = ', allnode

	# make node - degree dictionary
	degrees = get_degree(graph)

	print 'degrees = ', degrees
	# for each odd degree node
	for node in allnode:
		if degrees[node] % 2 == 1: # odd
			odd_node.append(node)

	#print 'odd node = ',  odd_node		
	if len(odd_node) == 0: # all even degree node
		# if no odd degree -> make tour starting node_0
		allnode_list = list(allnode)
		return get_path_for_nodes(graph, allnode_list[0], allnode, allnode,[])
	elif len(odd_node) == 2: # 2 odd degree node
		# if 2 odd degree -> make tour starting one of odd degreed node
		return get_path_for_nodes(graph, odd_node[0])
	else:
		# if >2 odd degree -> None
		return None	


def get_path_for_nodes(tour, current, to_visit, alln, path):
    a_path = []
    
    print 'get_path current=', current, ', to_visit = ', to_visit, ', path =', path
    if to_visit !=  None and len(to_visit) == 0:
	return path

    # get adj nodes
    adj = set([])
    for t in tour:
	if(t[0] == current):
            adj.add(t[1])
	
	elif(t[1] == current):
            adj.add(t[0])
    for node in adj:
	if to_visit != None:
		to_visit.remove(node)
		path.append(node)
		a_path = get_path_for_nodes(tour, node, to_visit, alln, path)
	if a_path != None and len(a_path) > 0:
		return path


    '''
    a = start
    nodes = set([a])
    explore = set([a])
    p = [a]
    while len(explore) > 0:
        # see what other nodes we can reach
        b = explore.pop()
        for t in tour:
            node = check_edge(t, b, nodes)
            if node is None:
                continue
            nodes.add(node)
            explore.add(node)
            p.append(node)
    #print '### get_path = ', p
    return p
    '''

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
	a_graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
	#a_graph = [(1, 13), (1, 6), (6, 11), (3, 13), (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9), (1, 12), (4, 12), (5, 14), (0, 1), (2, 3), (4, 11), (6, 9), (7, 14), (10, 13)]
	#a_graph = [(8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14), (1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
	#a_graph = [(1, 2), (2, 3), (3, 1), (3, 4)]
	return find_eulerian_tour(a_graph)
    
print test()
