inFile = open('output.txt', 'r')
outFile = open('sol.txt', 'w')

for line in inFile:
    if line[0] == '[': 
    	outFile.write(line)
    	
inFile.close()
outFile.close()