import numpy as np

from src.utils.help import routeLength


def two_opt(path, tsp):
    improved = True
    best=path.copy()
    improve,comparisons,iterations=0,0,0
    while improved:
        improved = False
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path)):
                comparisons+=1
                if j - i == 1:  continue  # same edge : (v,x)
                new_route=path[:]
                new_route[i:j] = path[j - 1:i - 1:-1]
                if routeLength(tsp,new_route) <routeLength(tsp,best):
                    best = new_route
                    improved = True
                    improve+=1
        path=best
        iterations+=1
    return best, routeLength(tsp,best),comparisons,improve,iterations


"""
def two_opt(path, tsp):
    firstPath=path
    bestPath = path
    improved = True

    while improved:
        improved = False
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path)):
                if j - i == 1:  # same edge : (v,x)
                    continue
                if cost_change(tsp, bestPath[i - 1], bestPath[i], bestPath[j - 1], bestPath[j]) < 0:
                    bestPath[i:j] = bestPath[j - 1:i - 1:-1]
                    path = bestPath
                    improved = True
        cost=routeLength(tsp,bestPath)
        print(cost)
        return bestPath,cost
"""
