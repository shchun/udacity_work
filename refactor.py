#!/usr/bin/env python

def bucket_find(bucket, key):
	for entry in bucket:
		if entry[0] == key:
			return entry
	return None

def hashtable_update(htable, key, value):
	bucket = hashtable_get_bucket(htable,key)
	entry = bucket_find(bucket, key)
	if entry:
		entry[1] = value
	else:
		bucket.append([key,value])

def hashtable_lookup(htable, key):
	entry = bucket_find(hashtable_get_bucket(htable,key), key)
	if entry:
		return entry[1]
	else:
		return None


