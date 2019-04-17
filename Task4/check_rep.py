inFile = open('sol.txt', 'r')
s = set()
for line in inFile:
	s.add(line)

print len(s)
