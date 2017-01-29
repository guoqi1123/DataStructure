# Practice writing a hash table using python list
from LinkedList import *
class HashTable(object):
	def __init__(self):
		# length of the list
		self.len = 1
		# random bias 
		self.bias = 5
		# random multiply
		self.ratio = 13
		# mod
		self.mod = 232133
		# the list that stores the data, each element
		# points to a linked list
		self.vars = [LinkedList() for i in range(self.len)] 

	def hashValue(self, key):
		# return the hash value for a key
		# do not remember the name of this function 
		return (hash(key) * self.ratio + self.bias) % self.mod % self.len
		
	def __setitem__(self, key, val):
		# set the value to key 
		# first search to see if there is already
		# such a key
		hval = self.hashValue(key)
		self.vars[hval].ptr = self.vars[hval].root
		# search for the key in the list
		while(self.vars[hval].ptr != None):
			if self.vars[hval].ptr.val[0] == key:
				# if there is one, directly change it
				self.vars[hval].ptr.val[1] = val
			self.vars[hval].ptr = self.vars[hval].ptr.next
		# if there is not, add it
		self.vars[self.hashValue(key)].add([key, val])

	def __getitem__(self, key):
		# return the value in key
		# return none if not exists
		hval = self.hashValue(key)
		self.vars[hval].ptr = self.vars[hval].root
		# search for the key in the list
		while(self.vars[hval].ptr != None):
			if self.vars[hval].ptr.val[0] == key:
				return self.vars[hval].ptr.val[1]
			self.vars[hval].ptr = self.vars[hval].ptr.next
		return None
