import sys

if(len(sys.argv)<2):
	print "File name required"
	exit()

fname = sys.argv[1]

f = open(fname,'r')

aa = set()
for line in f:
	for i in line:
		if(i != '\n'):
			aa.add(i)

print aa
