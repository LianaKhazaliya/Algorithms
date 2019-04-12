from random import randint, random

MIN, MAX = -100, 100
VARIABLES = 5

MUT_MIN, MUT_MAX = -3, 3
NGEN, CXPB, MUTPB, MUTG = 10, 0.5, 0.1, 0.02
DEFAULT_MAIN_ARGS = NGEN, CXPB, MUTPB

BEST_INSTANCE_MSG = 'Best instance:'


def fitness(instance):
    u, w, x, y, z = instance

    powU = [2, 0, 1, 1, 0]
    powW = [2, 1, 1, 2, 0]
    powX = [1, 2, 1, 1, 0]
    powY = [1, 1, 0, 1, 1]
    powZ = [2, 1, 2, 2, 0]

    data = zip([u, w, x, y, z], [powU, powW, powX, powY, powZ])

    return sum(sum(el[0]**el[1][i] for el in data) for i in range(5))-Result


def mutate(instance, mutpb, mutgenpb):
    if random.random() <= mutpb:
        for gen in instance:
            if random() <= mutgenpb:
                gen += randint(MUT_MIN, MUT_MAX)


def selection(population, popnum):
    newpop = []
    
    for i in range(popnum):
        parents = []

        for j in range(3):
            inst1 = population[randint(0, popnum-1)]
            inst2 = population[randint(0, popnum-1)]
            if fitness(inst1) <= fitness(inst2):
                parents.append(inst1)
            else:
                parents.append(inst2)

        parents_pairs = zip(parents, parents[1:]+parents[0])
        newpop = map(cross, parents_pairs)


def cross(pair):
    parent1, parent2 = pair[0], pair[1]
    if random() < 0.5:
        parent1[2], parent2[2] = parent2[2], parent1[2]
    else:
        parent1[1:4], parent2[1:4] = parent2[1:4], parent1[1:4]
    return parent1, parent2


def main(ngen, ind_size, cxpb, mutpb):
    population = [[randint(MIN, MAX) for j in range(5)] for i in range(popsize)]
    popdata = dict(zip(population, map(fitness, population)))
    generation = 0
    while generation < GEN_MAX and 0 not in popdata.values():

    if 0 in popdata.values():
        popdata_rev = dict(v,k for k,v in popdata.iteritems())
        print popdata_rev[0]


if __name__ == '__main__':
    main(*DEFAULT_MAIN_ARGS)


