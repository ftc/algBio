filename = "amino_acids"
splitChar = " "
aminoMap = {} #create empty map
aminoPolarity = {}
aminoHydrop = {}
f = open(filename,'r')
for i in f:
	c = i.split(splitChar)
	aminoMap[c[0]] = c[1].strip()
	aminoPolarity[c[0]] = c[2].strip()
	aminoHydrop[c[0]] = float(c[3].strip())

def getAmino():
	return aminoMap.copy()
def getPolarity():
	return aminoPolarity.copy()
def getHydrop():
	return aminoHydrop.copy()

def getOrderedArray():
	return sorted(aminoMap.keys())
	
	
