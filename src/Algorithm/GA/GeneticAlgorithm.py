from time import process_time

import numpy as np
import pandas as pd

from src.utils.help import *
import operator as op

"""
Steps :
1. creating initial population
2. calculating fitness
3. selecting the best genes
4. crossing over
5. mutating to introduce variation

Algorithm:
1. Init pop
2. Determine the fitness of the chromosome
3. Until done repeat:
    1. Select parents
    3. Calculate the fitness of the new population
    4. Append it to the gene pool
"""


class Fitness:

    def __init__(self, gnome) -> None:
        self.gnome = gnome
        self.dist = 0
        self.fitness = 0.0

    def gnomeFitness(self, tsp):
        if self.fitness == 0:
            self.fitness = 1 / float(routeLength(tsp, self.gnome))
        return self.fitness


def createGnome(n):
    gnome = randomGnome(n)
    return gnome


def initPopulation(POPSIZE, n):
    population = []

    for i in range(0, POPSIZE):
        population.append(createGnome(n))
    return population


def rankGnomes(population, tsp):
    fitnessLeaderboard = {}
    for i in range(0, len(population)):
        fitnessLeaderboard[i] = Fitness(population[i]).gnomeFitness(tsp)
    return sorted(fitnessLeaderboard.items(), key=op.itemgetter(1), reverse=True)


def naturalSelection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Rank", "Fitness"])
    df['SommeCum'] = df['Fitness'].cumsum()
    df['PourcentCum'] = 100 * df['SommeCum'] / df['Fitness'].sum()

    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])

    for i in range(0, len(popRanked) - eliteSize):
        pick = 100 * random.random()
        for j in range(0, len(popRanked)):
            if pick <= df.iat[j, 3]:
                selectionResults.append(popRanked[j][0])
                break
    return selectionResults


def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        matingpool.append(population[selectionResults[i]])
    return matingpool


def breed(p1, p2):
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random.random() * len(p1))
    geneB = int(random.random() * len(p1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(p1[i])
    childP2 = [item for item in p2 if item not in childP1]

    child = childP1 + childP2

    return child


def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool) - i - 1])
        children.append(child)

    return children


def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if (random.random() < mutationRate):
            swap(individual, swapped, int(random.random() * len(individual)))

    return individual


def mutatePopulation(population, mutationRate):
    mutatedPop = []
    for indiv in range(0, len(population)):
        mutatedPop.append(mutate(population[indiv], mutationRate))
    return mutatedPop


def nextGeneration(currentGen, eliteSize, mutationRate, tsp):
    return mutatePopulation(
        breedPopulation(
            matingPool(
                currentGen, naturalSelection(
                    rankGnomes(
                        currentGen, tsp
                    ),
                    eliteSize
                )
            ),
            eliteSize
        ),
        mutationRate
    )


def randomGnome(n):
    cities = list(range(n))
    solution = []
    for i in range(n):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)
    return solution


def geneticAlgorithm(tsp, n, popSize, eliteSize, mutationRate, generations):
    pop = initPopulation(popSize, n)
    print("Starting distance : " + str(1 / rankGnomes(pop, tsp)[0][1]))
    t1_start = process_time()
    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate, tsp)
        print(len(pop))
    t1_stop = process_time()
    bestGnomeIndex = rankGnomes(pop, tsp)[0][0]
    bestGnome = pop[bestGnomeIndex]
    bestGnomeCost = routeLength(tsp, bestGnome)
    return bestGnome, bestGnomeCost, (t1_stop - t1_start)
