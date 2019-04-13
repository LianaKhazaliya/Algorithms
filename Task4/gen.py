from random import randint, random

MIN, MAX = -100, 100
VARS = 5

MUT_MIN, MUT_MAX = -3, 3
NGEN, CXPB, MUTPB, MUTGENPB = 10, 0.5, 0.1, 0.02
DEFAULT_MAIN_ARGS = NGEN, CXPB, MUTPB


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


def mutate(instance):
    if random.random() <= MUTPB:
        for gen in instance:
            if random() <= MUTGENPB:
                gen += randint(MUT_MIN, MUT_MAX)

def mutation(population):
    return map(mutate, population)


def selection(population, popsize):    
    parents_pairs = []
    for i in range(popsize):
        parents = []
        for j in range(3):
            inst1 = population[randint(0, popnum-1)]
            inst2 = population[randint(0, popnum-1)]
            if fitness(inst1) <= fitness(inst2):
                parents.append(inst1)
            else:
                parents.append(inst2)

        parents_pairs += zip(parents, parents[1:]+parents[0])
    return parents_pairs


def crossover(pair):
    parent1, parent2 = pair[0], pair[1]
    if random() < 0.5:
        parent1[2], parent2[2] = parent2[2], parent1[2]
    else:
        parent1[1:4], parent2[1:4] = parent2[1:4], parent1[1:4]
    return parent1, parent2


def newpop_selection(population):
    newpop = []
    curpop = sorted(zip(map(fitness, population), population))[::-1]
    newpop_data += curpop[:popsize/10]
    while len(newpop) != popsize:
        newpop_data += curpop[randint(3*popsize-1)]

    newpop = [data[1] for data in newpop_data]
    return newpop


def create_population(popsize, ngen):
    return [(randint(MIN, MAX) for j in range(ngen))] for i in range(popsize)]

def fitness_calc(population):
    return dict(zip(map(fitness, population), population)), dict(zip(population, map(fitness, population)))

def is_zero(popdata_fi):
    return 0 not in popdata_fi.keys()

def is_nextgen(generation):
    return generation < GEN_MAX

def is_continue(generation, popdata):
    return is_zero and is_nextgen


def main(ngen, popsize):
    population = create_population(popsize, ngen)
    popdata_fi, popdata_if = fitness_calc(population)
    generation = 0

    while is_continue(generation, popdata):
        parents_pairs = selection(population, popsize)
        childs = [crossover(pair) for pair in parents_pairs]
        mut_childs = mutation(childs)
        population = newpop_selection(mut_childs)
        popdata_fi,popdata_if = fitness_calc(population)
        generation += 1

    if not is_zero(popdata):
        print popdata_fi[0]

    else:
        print popdata_if[min(popdata_if.keys())]


if __name__ == '__main__':
    population = create_population(10, 5)
    print fitness_calc(population)


