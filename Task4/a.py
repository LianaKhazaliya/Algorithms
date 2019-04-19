from random import randint, random
from pprint import pprint
from operator import itemgetter
import time

MIN, MAX = -100, 100
VARS = 5
GEN_MAX = 100
MUT_MIN, MUT_MAX = -3, 3
MUTPB, MUTGENPB = 0.2, 0.2          # for general probability of mutation 4,1%
POP_SIZE = 30


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


def mutate(instance, mut_min, mut_max, mutpb, mutgenpb):
    if random() <= mutpb:
        for i in range(len(instance)):
            if random() <= mutgenpb:
                instance[i] += randint(mut_min, mut_max)
    return instance

def mutation(population, mut_min, mut_max, mutpb, mutgenpb):
    return [mutate(inst, mut_min, mut_max, mutpb, mutgenpb) for inst in population]


def selection(population, popsize):    
    parents_pairs = []
    for i in range(popsize):
        parents = []
        for j in range(6):
            inst1 = population[randint(0, popsize-1)]
            inst2 = population[randint(0, popsize-1)]
            if fitness(inst1) <= fitness(inst2):
                parents.append(inst1)
            else:
                parents.append(inst2)

        parents_pairs += zip(parents[:3], parents[3:])
    return parents_pairs


def crossover(pair):
    parent1, parent2 = pair[0], pair[1]
    if random() < 0.5:
        parent1[2], parent2[2] = parent2[2], parent1[2]
    else:
        parent1[1:4], parent2[1:4] = parent2[1:4], parent1[1:4]
    return [parent1, parent2]


def newpop_selection(population, popsize, generation, gen_max, elite_inst, stop_rand, rand_inst):
    newpop_data = []
    curpop = sorted(zip(map(fitness, population), population))
    newpop_data += curpop[:int(popsize*elite_inst)]

    if generation < gen_max*stop_rand:

        while len(newpop_data) != (popsize*(1-rand_inst)):
            newpop_data.append(curpop[randint(0, 6*popsize-1)])

        newpop = [data[1] for data in newpop_data]

        while len(newpop) != popsize:
            newpop += [[randint(MIN, MAX) for j in range(5)]]

    else:

        while len(newpop_data) != popsize:
            newpop_data.append(curpop[randint(0, 6*popsize-1)])

        newpop = [data[1] for data in newpop_data]

    return newpop


def create_population(popsize, ngen):
    return [[randint(MIN, MAX) for j in range(ngen)] for i in range(popsize)]


def is_zero(popdata_f):
    return 0 not in popdata_f

def is_nextgen(generation, gen_max):
    return generation < gen_max

def is_continue(generation, popdata_f, gen_max):
    return is_zero(popdata_f) and is_nextgen(generation, gen_max)


def main(ngen, popsize, gen_max, mut_min, mut_max, mutpb, mutgenpb, elite_inst, stop_rand, rand_inst):
    population = create_population(popsize, ngen)
    popdata_f = fitness_calc(population)
    generation = 0

    while is_continue(generation, popdata_f, gen_max):

        parents_pairs = selection(population, popsize)
        childs = []
        for pair in parents_pairs:
            childs += crossover(pair)
        mut_childs = mutation(childs, mut_min, mut_max, mutpb, mutgenpb)
        population = newpop_selection(mut_childs, popsize, generation, gen_max, elite_inst, stop_rand, rand_inst)
        popdata_f = fitness_calc(population)
        generation += 1


    return population[min(enumerate(popdata_f), key=itemgetter(1))[0]], fitness(population[min(enumerate(popdata_f), key=itemgetter(1))[0]])

if __name__ == '__main__':
    import time
    start_time = time.time()
    print(main(5, 50, 2000, -5, 5, 0.1, 0.5, 0.5, 1, 0.2))
    print("--- %s seconds ---" % (time.time() - start_time))
#[2, -6, -13, -46, 2]