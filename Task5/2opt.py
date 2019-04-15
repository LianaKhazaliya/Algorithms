from random import randint, sample
from pprint import pprint
import more_itertools as mit
from operator import itemgetter

vert = 5
min_edges = (((vert+1)/2*(vert-1)/2)+(vert/2*(vert-2)/2))/2+1
matr = [[100000 for i in range(vert)] for j in range(vert)]

edges_weights = []

# define a weight for necessary number of vertices
edges_num = randint(min_edges, vert*(vert-1)/2)
for i in range(edges_num):
	v, u = sample(range(0, vert), 2)
	while matr[v][u] == 100000: #check that selected edge has not defined yet
		v, u = sample(range(0, vert), 2)
	w = randint(1, 50)
	matr[v][u] = matr[u][v] = w

	edges_weights.append([w, [min(u, v), max(u, v)]])


vert_seq = mit.random_permutation(range(vert))
vert_seq.append(hampath[0])

def weight_of_hampath(vert_seq, matr):
	weight = 0
	edges = []
	for i in range(vert):
		weight += matr[hampath[i]][hampath[i+1]]
		edges.append(matr[hampath[i]][hampath[i+1]], hampath[i], hampath[i+1])

	return weight, sorted(edges)[::-1]

cur_weight, edges = w_hampath(hampath, matr)

for ed1_ind in range(edges_num-2):
	for ed2_ind in range(ed1_ind+1,edges_num-1):
		s = matr[edges[ed1_ind][1], edges[ed2_ind][2]] + matr[edges[ed2_ind][1], edges[ed1_ind][2]]
		difference = edges[ed1_ind][0]+edges[ed2_ind][0] - a
		if difference:
			edges = edges[:ed1_ind+1]+edges[ed1_ind+1:ed2_ind:-1]+edges[ed2_ind:]


#ind_max = max(enumerate(edges), key=itemgetter(1))[0]
#max_w = edges[ind_max]
#edges[ind_max]
