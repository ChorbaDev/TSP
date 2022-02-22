import random

from src.utils.colors import bcolors


def randomSolution(n, town=None):
    cities = list(range(n))
    solution = [town]
    cities.remove(town)
    for i in range(n - 1):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)
    return solution


"""
 (v,x) ; (u,w)
 ( (v,w)+(ux) ) - ( (uw)+(vx) )
 new - old
"""


def cost_change(tsp, v, x, u, w):
    return tsp[(v, u)] + tsp[(x, w)] - tsp[(v, x)] - tsp[(u, w)]


def printGraph(tsp, n):
    for i in range(n):
        for j in range(n):
            if i == j:
                print(bcolors.OKBLUE + "  X" + bcolors.ENDC, end=" "),
            else:
                print(tsp[(i, j)], end=" "),
        print()


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
