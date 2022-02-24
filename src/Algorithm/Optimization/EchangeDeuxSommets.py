from src.utils.help import routeLength
from src.utils.help import next_perm
import random

import time


def randomValue(a, b, start):
    x = random.randint(a, b)
    while x == start:
        x = random.randint(a, b)
    return x


def randomEdge(n, start):
    x = randomValue(0, n - 1, start)
    y = randomValue(0, n - 1, start)
    while x == y:
        y = randomValue(0, n - 1, start)
    return x, y


def EchangeDeuxSommets(tsp, path, s):
    t_end = time.time() + s
    bestPath = path.copy()
    bestCost = routeLength(tsp, path)
    improve, comparisons, iterations = 0, 0, 0
    t1_start = time.process_time()
    while time.time() < t_end:
        next_perm(path)
        cost = routeLength(tsp, path)
        if bestCost > cost:
            improve += 1
            bestCost = cost
            bestPath = path.copy()
        iterations += 1
    t1_stop = time.process_time()
    return bestPath, bestCost, comparisons, improve, iterations, (t1_stop - t1_start)
