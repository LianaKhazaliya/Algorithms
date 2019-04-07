from random import randint

u = randint(0, 5)
w = randint(0, 5)
x = randint(0, 5)
y = randint(0, 5)
z = randint(0, 5)

powU = [2, 0, 1, 1, 0]
powW = [2, 1, 1, 2, 0]
powX = [1, 2, 1, 1, 0]
powY = [1, 1, 0, 1, 1]
powZ = [2, 1, 2, 2, 0]

Result = 34

data = zip([u, w, x, y, z], [powU, powW, powX, powY, powZ])
print data
print sum(sum(el[0]**el[1][i] for el in data) for i in range(5))-Result



