import gen
inFile = open('sol.txt', 'r')
for line in inFile:
	a = list(map(int, line[1:-2].split(', ')))
	print gen.fitness(a)

inFile.close()