u = 1
w = 2
x = 0.30277286414
y = 3
z = 0.00001
powU = [2, 0, 1, 1, 0]
powW = [2, 1, 1, 2, 0]
powX = [1, 2, 1, 1, 0]
powY = [1, 1, 0, 1, 1]
powZ = [2, 1, 2, 2, 0]
Result = 34

data = zip([u, w, x, y, z], [powU, powW, powX, powY, powZ])
S = 0
for i in range(5):
	S += sum([el[0]**el[1][i] for el in data])

print S





