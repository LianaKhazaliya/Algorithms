import gen

#outFile = open('output.txt', 'w')
ans = []
for i in range(1000):
	a, b = gen.main(5, 30)
	if(b == 0):
		print a

#outFile.close()