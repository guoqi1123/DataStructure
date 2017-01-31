# Implementing string buffer
class StringBuffer(object):
	def __init__(self, val = ""):
		self.str = ArrayList()
	
	def __repr__(self):
		string = ""
		for i in range(len(self.str)):
			string += self.str[i]
		return string
		
	def concate(self, val):
		self.str.append(val)	
		
