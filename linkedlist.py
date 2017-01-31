class LinkedList(object):
	# a doubly linked list structure
	class Node(object):
		# node for the linked list
		def __init__(self, val):
			self.val = val
			self.next = None
			self.previous = None
		
		def __repr__(self):
			return str(self.val)
	
	def __init__(self):
		self.root = None
		self.end = None
		self.ptr = None

	def __repr__(self):
		# output the structure of the linkedlist
		# return an empty string when the linked list
		# is empty
		if self.root == None:
			return ""		
		tmp_ptr = self.root
		string = ""
		while(True):
			string += str(tmp_ptr.val)
			tmp_ptr = tmp_ptr.next
			if tmp_ptr != None:
				string += "=>"
			else:
				break
		return string

	def add(self, val):
		# add a new node
		if self.root == None:
			self.root = self.Node(val)
			self.end = self.root
			self.ptr = self.root
		else:
			self.end.next = self.Node(val)
			self.end.next.previous = self.end
			self.end = self.end.next

	def delete(self):
		# delete the node that self.ptr points to
		if self.ptr == self.root:
			# delete the root
			if self.ptr == self.end:
				# there is only one node
				self.ptr = None
				self.root = None
				self.end = None
				# somehow release the memory,
				# same to below
			else:
				# there is more than one node
				self.ptr = self.ptr.next
				self.root = self.root.next
				self.root.previous = None
		elif self.ptr == self.end:
			# delete the end node
			# the case of only one node has already
			# been considered
			self.ptr = self.ptr.previous
			self.end = self.end.previous
			self.end.next = None
		else:
			# delete the node in the middle
			self.ptr.next.previous = self.ptr.previous
			self.ptr.previous.next = self.ptr.next
			self.ptr = self.ptr.previous

			
			
