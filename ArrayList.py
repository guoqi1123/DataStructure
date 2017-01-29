# my implementation of arraylist
class ArrayList(object):
	# an arraylist data structure using python List
	def __init__(self):
		self.len = 1
		self.appendPtr = 0
		self.vals = [None for i in range(self.len)]
	
	def __repr__(self):
		string = "["
		for i in range(self.appendPtr):
			string += str(self.vals[i])
			if i != (self.appendPtr-1):
				string += ", "
		string += "]"		
		return string

	def __len__(self):
		return self.appendPtr

	def __getitem__(self, idx):
		if idx >= self.appendPtr:
			return "Error: index out of bound"
		else:
			return self.vals[idx]

	def __setitem__(self, idx, val):
		if idx >= self.appendPtr:
			return "Error: index out of bound"
		else:
			self.vals[idx] = val
		
	def append(self, val):
		if self.appendPtr >= self.len:
			# if it exceeds the range, make a longer one		
			newvals = [None for i in range(self.len*2)]
			for i in range(self.len):
				newvals[i] = self.vals[i]
			self.vals = newvals
			self.len *= 2
		# add the new values
		self.vals[self.appendPtr] = val
		self.appendPtr += 1
		return 

	def delete(self, val):
		# delete the first occurence of value val
		# we implement an O(n) deletion
		idx = 0		
		while(self.vals[idx] != val):
			# first check if idx is out of bound
			if(idx >= self.appendPtr):
				return
			idx += 1
		# delete it by moving all elements behind idx
		# for one index
		for i in range(idx+1, self.appendPtr):
			self.vals[i-1] = self.vals[i]
		self.appendPtr -= 1
		return
