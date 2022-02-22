from src.utils.help import cost_change,routeLength


def two_opt(path, tsp):
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
                    improved = True
        path = bestPath
    return bestPath,routeLength(tsp,bestPath)
