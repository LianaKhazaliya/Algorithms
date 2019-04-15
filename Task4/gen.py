from random import randint, random
from pprint import pprint
from operator import itemgetter


MIN, MAX = -100, 100
VARS = 5
GEN_MAX = 100
MUT_MIN, MUT_MAX = -5, 5
MUTPB, MUTGENPB = 0.1, 0.2          # for general probability of mutation 4,1%
POP_SIZE = 25


def fitness(instance):
    u, w, x, y, z = instance

    powU = [2, 0, 1, 1, 0]
    powW = [2, 1, 1, 2, 0]
    powX = [1, 2, 1, 1, 0]
    powY = [1, 1, 0, 1, 1]
    powZ = [2, 1, 2, 2, 0]
    Result = 34

    data = zip([u, w, x, y, z], [powU, powW, powX, powY, powZ])

    return abs(sum(sum(el[0]**el[1][i] for el in data) for i in range(5))-Result)


def fitness_calc(population):
    return map(fitness, population)


def mutate(instance):
    if random() <= MUTPB:
        for i in range(len(instance)):
            if random() <= MUTGENPB:
                instance[i] += randint(MUT_MIN, MUT_MAX)
    return instance

def mutation(population):
    return map(mutate, population)


def selection(population, popsize):    
    parents_pairs = []
    for i in range(popsize):
        parents = []
        for j in range(3):
            inst1 = population[randint(0, popsize-1)]
            inst2 = population[randint(0, popsize-1)]
            if fitness(inst1) <= fitness(inst2):
                parents.append(inst1)
            else:
                parents.append(inst2)

        parents_pairs += zip(parents, parents[1:]+parents[:1])
    return parents_pairs


def crossover(pair):
    parent1, parent2 = pair[0], pair[1]
    if random() < 0.5:
        parent1[2], parent2[2] = parent2[2], parent1[2]
    else:
        parent1[1:4], parent2[1:4] = parent2[1:4], parent1[1:4]
    return [parent1, parent2]


def newpop_selection(population, popsize, generation):
    newpop_data = []
    curpop = sorted(zip(map(fitness, population), population))
    newpop_data += curpop[:popsize/5]

    if generation < GEN_MAX*0.9:

        while len(newpop_data) != (popsize-3):
            newpop_data.append(curpop[randint(0, 6*popsize-1)])

        newpop = [data[1] for data in newpop_data]+[[randint(MIN, MAX) for j in range(5)] for i in range(3)]

    else:

        while len(newpop_data) != popsize:
            newpop_data.append(curpop[randint(0, 6*popsize-1)])

        newpop = [data[1] for data in newpop_data]

    return newpop


def create_population(popsize, ngen):
    return [[randint(MIN, MAX) for j in range(ngen)] for i in range(popsize)]


def is_zero(popdata_f):
    return 0 not in popdata_f

def is_nextgen(generation):
    return generation < GEN_MAX

def is_continue(generation, popdata_f):
    return is_zero(popdata_f) and is_nextgen(generation)


def main(ngen, popsize):
    population = create_population(popsize, ngen)
    popdata_f = fitness_calc(population)
    generation = 0

    while is_continue(generation, popdata_f):

        parents_pairs = selection(population, popsize)
        childs = []
        for pair in parents_pairs:
            childs += crossover(pair)
        mut_childs = mutation(childs)
        population = newpop_selection(mut_childs, popsize, generation)
        popdata_f = fitness_calc(population)
        generation += 1

    return population[min(enumerate(popdata_f), key=itemgetter(1))[0]], fitness(population[min(enumerate(popdata_f), key=itemgetter(1))[0]])

if __name__ == '__main__':
    main(VARS, POP_SIZE)

#-10, 3, -6, -49, -6 -> 0
#-18 -3 0 -88 5 -> 0
#8 7 -7 -98 8 -> 0
#-4 -4 11 -42 -2 -> 0
#-8 2 -8 -53 -7 -> 0
#-6 -1 0 1 0 -> 0
#10 -4 -5 -70 7 -> 0
#-10 -2 -10 -90 -9 -> 0
#-12 3 -11 -51 0 -> 0
#-10 -7 0 -40 -3 -> 0
#-4 1 17 -82 1 -> 0