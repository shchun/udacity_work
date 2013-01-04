#!/usr/bin/env python

def subpattern_for_idx(pattern, rule, idx):

	#print 'len = ', len(pattern), 'idx =', idx
	if len(pattern) == (idx+1):
		ret = pattern[idx-1] + pattern[idx] + pattern[0]	
	else:
		ret = pattern[idx-1] + pattern[idx] + pattern[idx+1]	

	#print 'ret= ', ret, 'val=', eval_subpattern_for_idx(ret, rule)
	return eval_subpattern_for_idx(ret, rule)

def eval_subpattern_for_idx(sub_pattern, rule):
	val = 0
	if sub_pattern == '...':
		val = 1
	elif sub_pattern == '..x':
		val = 2
	elif sub_pattern == '.x.':
		val = 4
	elif sub_pattern == '.xx':
		val = 8
	elif sub_pattern == 'x..':
		val = 16
	elif sub_pattern == 'x.x':
		val = 32
	elif sub_pattern == 'xx.':
		val = 64
	elif sub_pattern == 'xxx':
		val = 128
	else:
		print 'error: eval subpattern for idx'

	if val & rule:
		return 'x'
	else:
		return '.'

def cellular_automaton(pattern, rule, depth):
	ret = ''
	if depth == 0:
		return pattern

	pattern_len = len(pattern)
	for i in range(0, pattern_len):
		ret += subpattern_for_idx(pattern, rule, i)
	return cellular_automaton(ret, rule, depth - 1)

if 0:
	#cellular_automaton('abcdefghi', 17, 1)
	#print cellular_automaton('.x.x.x.x.', 17, 2)
	print cellular_automaton('...........x...........', 142, 1)
	print cellular_automaton('...........x...........', 142, 2)
	print cellular_automaton('...........x...........', 142, 3)
	print cellular_automaton('...........x...........', 142, 4)
	print cellular_automaton('...........x...........', 142, 5)
	print cellular_automaton('...........x...........', 142, 6)
	print cellular_automaton('...........x...........', 142, 7)
	print cellular_automaton('...........x...........', 142, 8)

print cellular_automaton('.x.x.x.x.', 17, 2)
#>>> xxxxxxx..
print cellular_automaton('.x.x.x.x.', 249, 3)
#>>> .x..x.x.x
print cellular_automaton('...x....', 125, 1)
#>>> xx.xxxxx
print cellular_automaton('...x....', 125, 2)
#>>> .xxx....
print cellular_automaton('...x....', 125, 3)
#>>> .x.xxxxx

print cellular_automaton('...x....', 125, 4)
#>>> xxxx...x
print cellular_automaton('...x....', 125, 5)
#>>> ...xxx.x
print cellular_automaton('...x....', 125, 6)
#>>> xx.x.xxx
print cellular_automaton('...x....', 125, 7)
#>>> .xxxxx..
print cellular_automaton('...x....', 125, 8)
#>>> .x...xxx
print cellular_automaton('...x....', 125, 9)
#>>> xxxx.x.x
print cellular_automaton('...x....', 125, 10)
#>>> ...xxxxx
