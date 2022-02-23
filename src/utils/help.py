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


def rand_num(start, end):
    return random.randint(start, end - 1)


def swap(listToSwap, i1, i2):
    temp = listToSwap[i1]
    listToSwap[i1] = listToSwap[i2]
    listToSwap[i2] = temp
    return listToSwap


def next_perm(l):
    n = len(l)
    i = n - 2

    while i >= 0 and l[i] > l[i + 1]:
        i -= 1

    # that means we used all permutations
    if i == -1:
        return False

    j = i + 1
    while j < n and l[j] > l[i]:
        j += 1

    j -= 1

    l[i], l[j] = l[j], l[i]
    left = i + 1
    right = n - 1

    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return True
