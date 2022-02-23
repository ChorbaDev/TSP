import time
from time import process_time
from src.utils.help import randomSolution, routeLength
from sys import maxsize


def RandomSolution(tsp, town, n, s):
    t_end = time.time() + s
    bestCost = maxsize
    bestPath = []
    t1_start = process_time()
    while time.time() < t_end:
        path = randomSolution(n, town)
        cost = routeLength(tsp, path)
        if bestCost > cost:
            bestCost = cost
            bestPath = path.copy()

    t1_stop = process_time()
    return bestPath, bestCost, (t1_stop - t1_start)
