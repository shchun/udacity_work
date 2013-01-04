#!/usr/bin/env python
def numbers_in_lists(input):
	ret = []
	sub = []
	for val in input:
		if len(ret) == 0:	
			ret.append(int(val))
			continue
		if int(val) > ret[-1]:
			if len(sub) > 0:
				ret.append(sub)
				print 'sub = ', sub
				sub = []
			ret.append(int(val))
			continue
		else:
			sub.append(int(val))
	if len(sub) > 0:
		ret.append(sub)
		print 'sub = ', sub
	return ret

'''
	ret = ''
	for val in input:
		if type(val) == list:
			ret += str(numbers_in_lists(val))
		else:
			ret += str(val)
	print 'ret = ', ret
	return int(ret)
'''

#input1 = [5,[4,3],9,[8,7]]
input1 = '543987'
print numbers_in_lists(input1)
