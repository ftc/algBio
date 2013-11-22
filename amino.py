filename = "amino_acids"
splitChar = " "
#NOTE: do not access aminoMap directly, call getAminoMap
aminoMap = {} #create empty map
f = open(filename,'r')
for i in f:
	c = i.split(splitChar)
	aminoMap[c[0]] = c[1].strip()

def getAmino():
	return aminoMap.copy()

def getOrderedArray():
	return sorted(aminoMap.keys())
	
	
