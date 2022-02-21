import time
from time import process_time
from help import randomSolution,routeLength
from sys import maxsize

def RandomSolution(tsp,town,n,s):
    t_end= time.time()+s
    bestCost=maxsize
    bestPath=[]
    t1_start = process_time()
    while time.time() < t_end:
        path=randomSolution(n,town)
        cost=routeLength(tsp,path)
        if bestCost>cost:
            bestCost=cost
            bestPath=path.copy()

    t1_stop = process_time()
    return bestPath,bestCost,(t1_stop-t1_start)


def cost_change(tsp, a, b, c, d):
    return tsp[(a, c)] + tsp[(b, d)] - tsp[(a, b)] - tsp[(c, d)]

def two_opt(path, tsp):
    bestPath = path
    improved = True
    while improved:
        improved = False
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path)):
                if j - i == 1: continue
                if cost_change(tsp, bestPath[i - 1], bestPath[i], bestPath[j - 1], bestPath[j]) < 0:
                    bestPath[i:j] = bestPath[j - 1:i - 1:-1]
                    improved = True
        path = bestPath
    return bestPath

def RandomSolutionImproved1(tsp, town, n, s):
    t_end = time.time() + s
    bestCost = maxsize
    bestPath = []
    t1_start = process_time()
    while time.time() < t_end:
        path = randomSolution(n, town)
        path = two_opt(path, tsp)
        cost = routeLength(tsp, path)
        if bestCost > cost:
            bestCost = cost
            bestPath = path.copy()

    t1_stop = process_time()
    return bestPath, bestCost, (t1_stop - t1_start)
