from random import random
from pprint import pprint

W = [random() for i in range(int(input('How many initial elements ')))]
kont = dict()
print W

def adding(w, kont):
	cur = 1
	while (cur in kont) and (kont[cur][0] < w):
		cur += 1

	if cur not in kont:
		kont[cur] = [1-w, [w]]
	else:
		kont[cur][0] -= w
		kont[cur][1].append(w)

	pprint(kont)

for w in W:
	adding(w, kont)


for i in range(100):
	w = input('Numerator ')*1.0/input('Denominator ')
	adding(w, kont)
