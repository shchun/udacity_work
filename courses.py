#!/usr/bin/env python

courses = {
	'feb2012': { 'cs101': {'name': 'Building a Search Engine',
		'teacher': 'Dave',
		'assistant': 'Peter C.'},
	'cs373': {'name': 'Programming a Robotic Car',
		'teacher': 'Sebastian',
		'assistant': 'Andy'}},
	'apr2012': { 'cs101': {'name': 'Building a Search Engine',
		'teacher': 'Dave',
		'assistant': 'Sarah'},
	'cs212': {'name': 'The Design of Computer Programs',
		'teacher': 'Peter N.',
		'assistant': 'Andy',
		'prereq': 'cs101'},
	'cs253': 
	{'name': 'Web Application Engineering - Building a Blog',
		'teacher': 'Steve',
		'prereq': 'cs101'},
	'cs262': 
	{'name': 'Programming Languages - Building a Web Browser',
		'teacher': 'Wes',
		'assistant': 'Peter C.',
		'prereq': 'cs101'},
	'cs373': {'name': 'Programming a Robotic Car',
		'teacher': 'Sebastian'},
	'cs387': {'name': 'Applied Cryptography',
		'teacher': 'Dave'}},
	'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
		'teacher': 'Dorina'},
	'cs003': {'name': 'Programming a Robotic Robotics Teacher',
		'teacher': 'Jasper'},
	}
}


def involved(courses, person):
	res = {}	
	for hexamester in courses:
		#print hexamester
		#print courses[hexamester]
		for cls in courses[hexamester]:
			#print hexamester, cls, courses[hexamester][cls]['teacher']
			for key in courses[hexamester][cls]:
				if courses[hexamester][cls][key] == person:
					if hexamester not in res:
						res[hexamester] = []
					res[hexamester].append(cls)

	#print 'res = ', res
	return res
print involved(courses, 'Dave')
print involved(courses, 'Peter C.')
print involved(courses, '')
