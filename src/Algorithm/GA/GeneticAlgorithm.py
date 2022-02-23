from time import process_time
import numpy as np
from src.utils.help import *

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


def random_gnome(n):
    cities = list(range(n))
    solution = []
    for i in range(n):
        random_city = cities[random.randint(0, len(cities) - 1)]
        solution.append(random_city)
        cities.remove(random_city)
    return solution


def init_pop(tsp, population_size, n):
    population = []

    for i in range(population_size):
        gnome = random_gnome(n)
        population.append(gnome)
    return population
    # population.append(randomGnome(n,populationSize))


def gnome_fitness(tsp, gnome):
    return routeLength(tsp, gnome)


def population_fitness(population, tsp, population_size):
    fitness_list = np.zeros(population_size)
    for i in range(population_size):
        fitness_list[i] = gnome_fitness(tsp, population[i])
    return fitness_list


def fitest_selection(population, fitness_list):
    total_fitness = fitness_list.sum()
    prob_list = fitness_list / total_fitness

    parent_list_a = np.random.choice(list(range(len(population))), len(population), p=prob_list, replace=True)
    parent_list_b = np.random.choice(list(range(len(population))), len(population), p=prob_list, replace=True)

    parent_list_a = np.array(population)[parent_list_a]
    parent_list_b = np.array(population)[parent_list_b]

    return np.array([parent_list_a, parent_list_b])


def breed_parent(parent_a, parent_b):
    child = parent_a[0:5]

    for city in parent_b:
        if city not in child:
            child = np.concatenate((child, [city]))
    return child


def breed_population(parent_list):
    new_population = []
    for i in range(parent_list.shape[1]):
        parent_a, parent_b = parent_list[0][i], parent_list[1][i]
        child = breed_parent(parent_a, parent_b)
        new_population.append(child)

    return new_population


def mutate_child(child, n, mu):
    for q in range(int(n * mu)):
        a = np.random.randint(0, n)
        b = np.random.randint(0, n)

        child[a], child[b] = child[b], child[a]

    return child


def mutate_population(new_population, n, mu):
    mutated_pop = []
    for child in new_population:
        mutated_pop.append(mutate_child(child, n, mu))

    return mutated_pop


def genetic_algorithm(tsp, n, population_size, mu, gen):
    best_gnome = [-1, np.inf, np.array([])]
    population = init_pop(tsp, population_size, n)
    fitness_list = population_fitness(population, tsp, population_size)
    parent_list = fitest_selection(population, fitness_list)
    new_population = breed_population(parent_list)
    mutated_population = mutate_population(new_population, n, mu)
    t1_start = process_time()
    for i in range(gen):
        fitness_list = population_fitness(mutated_population, tsp, population_size)

        if fitness_list.min() < best_gnome[1]:
            best_gnome[0] = i
            best_gnome[1] = fitness_list.min()
            best_gnome[2] = np.array(mutated_population)[fitness_list.min() == fitness_list]

        parent_list = fitest_selection(population, fitness_list)
        new_population = breed_population(parent_list)

        mutated_population = mutate_population(new_population, n, mu)
    t1_stop = process_time()
    best_gen = best_gnome[0]
    best_cost = best_gnome[1]
    best_solution = best_gnome[2].tolist()

    return best_solution[0], best_cost, (t1_stop - t1_start)
