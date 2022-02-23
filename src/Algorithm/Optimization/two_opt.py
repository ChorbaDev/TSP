import numpy as np

from src.utils.help import routeLength


# Complexity of O(n^2)

def two_opt(path, tsp):
    improved = True
    best = path.copy()
    improve, comparisons, iterations = 0, 0, 0
    while improved:
        improved = False
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path)):
                comparisons += 1
                if j - i == 1:  continue  # same edge : (v,x)
                new_route = path[:]
                new_route[i:j] = path[j - 1:i - 1:-1]
                if routeLength(tsp, new_route) < routeLength(tsp, best):
                    best = new_route
                    improved = True
                    improve += 1
        path = best
        iterations += 1
    return best, routeLength(tsp, best), comparisons, improve, iterations
