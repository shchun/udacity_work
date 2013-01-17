#!/usr/bin/env python

#
# write up_heapify, an algorithm that checks if
# node i and its parent satisfy the heap
# property, swapping and recursing if they don't
#
# L should be a heap when up_heapify is done
#

def up_heapify(L, i):
    # your code here
    print 'up_heapify i=', i , 'len(L)=', len(L)   
    if i == 0:
        return
    
    if len(L) == (i+1):
        if L[i] < L[parent(i)]:
            (L[i], L[parent(i)]) = (L[parent(i)], L[i])
        up_heapify(L, parent(i))
        return
    
    # two child
    if min(L[i], L[i+1]) < L[parent(i)]:
        if L[i] > L[i+1]:
            (L[i+1], L[parent(i)]) = (L[parent(i)], L[i+1])
        else:
            (L[i], L[parent(i)]) = (L[parent(i)], L[i])
        
    up_heapify(L, parent(i))
    return

def parent(i): 
    return (i-1)/2
def left_child(i): 
    return 2*i+1
def right_child(i): 
    return 2*i+2
def is_leaf(L,i): 
    return (left_child(i) >= len(L)) and (right_child(i) >= len(L))
def one_child(L,i): 
    return (left_child(i) < len(L)) and (right_child(i) >= len(L))

def test():
    L = [2, 4, 3, 5, 9, 7, 7]
    L.append(1)
    up_heapify(L, 7)
    print 'L=', L
    assert 1 == L[0]
    assert 2 == L[1]

test()

