import amino

aminoListChr = amino.getOrderedArray()

class scoreMatrix:
	def __init__(self):
		self.mat = []
		for i in xrange(22):
			r = []
			for i in xrange(22):
				r.append('u') #initialize with 'u' for uninitialized
			self.mat.append(r)
		#TODO: make index lookup
	def printMatrix(self):
		for i in self.mat:
			print i
	def get(self, v1, v2):
		#make sure v1p is always lower or equal to v2p, this enforces non duplication of data
		v1p = v1 if ord(v1)<ord(v2) else v2
		v2p = v1 if ord(v1)>=ord(v2) else v2
		#TODO: finish after index lookup is done

	#TODO: make fwrite
	#TODO: make fread
		


