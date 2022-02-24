from src.utils.help import routeLength
from src.utils.help import next_perm
import random

import time

def EchangeDeuxSommets(tsp, path, s):
    t_end = time.time() + s
    bestPath = path.copy()
    bestCost = routeLength(tsp, path)
    improve, comparisons, iterations = 0, 0, 0
    t1_start = time.process_time()
    while time.time() < t_end:
        for i in range(1,len(path)):
            for j in range(i+1,len(path)):
                iterations += 1
                test=bestPath.copy()
                test[i],test[j]=test[j],test[i]
                cost = routeLength(tsp, test)
                if bestCost > cost:
                    improve += 1
                    bestCost = cost
                    bestPath = test.copy()
                    break
    t1_stop = time.process_time()
    return bestPath, bestCost, comparisons, improve, iterations, (t1_stop - t1_start)

