import scoreMatrix
import amino
import pseudoScore
import sys

#Note: this code could be improved with dynamic programming
#however the runtime for this project is low and I am lazy

#alpha unit can have gaps on beginning but not in the middle

#penalty scores (subtracted when gap is introduced)
alpGapPen = -0.05
rptGapPen = -0.05

scm = pseudoScore.getScoreMatrix(0.5,0.5)

#returns: (score, rptprime, alpprime)
def calcGap(rpt, alp):
	#calculates all possibility where alph begins with gap
	#Note: no base cases here, they are handled by calcRptGap
	wgap = calcGap(rpt[1:], alp)
	ngap = calcRptGap(rpt, alp)
	wgapScore = wgap[0]
	ngapScore = ngap[0]
	if ngapScore >= wgapScore:
		return ngap
	else:
		return (wgapScore+alpGapPen, '-' + wgap[1], rpt[0] + wgap[2])
def calcRptGap(rpt,alp):
	#calculates possibilities after initial gap in alpha
	#define base cases
	#gap penalty is assessed for ending gap too
	if(rpt == ""):
		return (len(alp)*rptGapPen, "-"*len(alp), alp)
	if(alp == ""):
		return (len(rpt)*rptGapPen, rpt, "-"*len(rpt))
	ngap = calcRptGap(rpt[1:],alp[1:])
	wgap = calcRptGap(rpt, alp[1:])
	ngapScore = ngap[0] + scm.get(rpt[0],alp[0])
	wgapScore = wgap[0] + rptGapPen

	if ngapScore >= wgapScore:
		return (ngapScore, rpt[0] + ngap[1], alp[0] + ngap[2])
	else:
		return (wgapScore, "-" + wgap[1], alp[0] + wgap[2])
		

if(len(sys.argv) > 1):
	fname = sys.argv[1]
	ofname = fname + ".out"
	f = open(fname,'r')
	of = open(ofname, 'w')
	for i in f:
		if i[0] != '#':
			a = i.strip().split(" ")
			if(len(a) == 2):
				of.write(str(calcRptGap(a[0],a[1])) + "\n")
			else:
				of.write("\n")
			
	
