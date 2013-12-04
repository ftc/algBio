import scoreMatrix
import pseudoScore

#equal weighting to both h bonds and ionic bonds
scm = pseudoScore.getScoreMatrix(0.5, 0.5) 

#s1 and s2 must be the same length
def scoreSeq(s1, s2):
	if len(s1) != len(s2):
		raise Exception
	score = 0
	for i in xrange(len(s1)):
		score += scm.get(s1[i],s2[i])
	score = score/len(s1)
	return score
