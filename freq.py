#!/usr/bin/env python

def freq_analysis(message):
	ret = []
	len_message = len(message);
	for i in range(0,26):
		ret.append(0.0)

	for ch in message:
		ret[ord(ch) - ord('a')] += 1

	for i in range(0,26):
		ret[i] /= len_message
	return ret



#Tests

print freq_analysis("abcd")

