import scoreMatrix as s
import amino
from math import copysign

aminoList = amino.getOrderedArray()
aminoPolarity = amino.getPolarity()
aminoHydrop = amino.getHydrop()


scoreMatrix = s.ScoreMatrix()

tol = 0.001 #tolerance for comparing polarity of amino acids
cmpF = lambda x,y: abs(x - y) < tol

#calculate maximum hydrophilic
mxPhil = 0.0
for i in aminoHydrop:
	if aminoHydrop[i] < mxPhil:
		mxPhil = aminoHydrop[i]
pMxPhil = -mxPhil
if(pMxPhil <0):
	raise RuntimeWarning

def calcScore(aa1, aa2, hWeight, pWeight):
	return hWeight*calcHydropScore(aa1, aa2) + pWeight*calcPolScore(aa1, aa2)
	

def calcPolScore(aa1, aa2):
	pol1 = aminoPolarity[aa1]
	pol2 = aminoPolarity[aa2]
	if(cmpF(pol1,0) or cmpF(pol2,0)):
		return 0
	s1 = copysign(1,pol1)
	s2 = copysign(1,pol2)
	if(s1 != s2):
		return 1
	else:
		return -1

def calcHydropScore(aa1, aa2):
	hy1 = aminoHydrop[aa1]
	hy2 = aminoHydrop[aa2]
	s1 = copysign(1,hy1)
	s2 = copysign(1,hy2)
	if(cmpF(hy1,0) or cmpF(hy2,0)):
		return 0 #no data is assumed for a score of 0
	if(s1 == -1 and s2 == -1):
		#mxPhil
		avg = (hy1 + hy2)/2
		score = abs(avg)/pMxPhil
		return score*0.3 + 0.1 #return score between 0.1 and 0.4
	else:
		return 0



def getScoreMatrix(hWeight, pWeight):
	scoreMatrix = s.ScoreMatrix()
	for i in xrange(len(aminoList)):
		for j in xrange(i,len(aminoList)):
			aa1 = aminoList[i]
			aa2 = aminoList[j]
			scoreMatrix.set(aa1,aa2, calcScore(aa1,aa2, hWeight, pWeight))
	return scoreMatrix
		
