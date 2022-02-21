import random


def randomSolution(n, town=None):
    cities = list(range(n))
    solution = [town]
    cities.remove(town)
    for i in range(n - 1):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)
    return solution


def routeLength(tsp, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[(solution[i - 1], solution[i])]
    return routeLength


"""
def pathCost(tsp,path,town=None):
    cost=0
    for i in range(len(path)):
        if path[i]==town:
            continue
        cost+=tsp[(town,path[i])]
        town=path[i]
    return cost
"""


def rand_num(start, end):
    return random.randint(start, end - 1)


def swap(listToSwap, i1, i2):
    temp = listToSwap[i1]
    listToSwap[i1] = listToSwap[i2]
    listToSwap[i2] = temp
    return listToSwap