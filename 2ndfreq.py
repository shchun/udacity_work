#!/usr/bin/env python

def prepareData():
	freq = {}
	f = open('yob1995.txt', 'r')
	for line in f:
		print 'line =', line,
		name, sex, fr= line.split(',')
		print 'name =', name, 'sex =', sex, 'fr =', fr
		if sex == 'F':
			if name in freq:
				freq[name] = int(fr)
			else:
				freq[name] = int(fr)

	print 'freq =', freq
	print 'max =', getmax(freq)

def getmax(freq):
	first_freq = 0
	second_freq = 0
	first_name = ''
	second_name = ''
	for k in freq:
		if first_freq < freq[k]:		
			second_freq = first_freq
			first_freq = freq[k]
			second_name = first_name
			first_name = k
		elif second_freq < freq[k]:
			second_name = k
			second_freq = freq[k]

	print 'first freq =', first_freq
	print 'first name =', first_name
	print 'second freq =', second_freq
	print 'second name =', second_name
	

prepareData()

