import random
from time import process_time

from src.utils.help import routeLength
from sys import maxsize

"""
G: Matrix
n: number of towns 
PER: Pheromone Evaporation Rate 0.05
AP: Artificial Pheromone 0.0453
"""


def ACO(G, n, startTown, iteration, AP, alpha=1, beta=1):
    startAgain=startTown
    bestTravel=[]
    bestCost=maxsize
    t1_start = process_time()
    for j in range(iteration):
        notVisited = [*range(n)]
        notVisited.remove(startTown)
        travel = [startTown]
        while len(notVisited)>0:
            tour = {i: 0 for i in notVisited}
            sum = 0
            for town in notVisited:
                tour[town]=(AP**alpha * (1. / G[(startTown, town)])**beta)
                sum += tour[town]
            for i in notVisited:
                tour[i] = tour.get(i) / sum
            Solution_Set = { i: 1 for i in range(n)}
            add = 0
            for i in notVisited:
                Solution_Set[i]=tour[i] + add
                add += tour[i]
            randomValue = random.random()
            for solu in notVisited:
                if randomValue <= Solution_Set[solu]:
                    travel.append(solu)
                    notVisited.remove(solu)
                    startTown = solu
                    break
        cost=routeLength(G,travel)
        startTown=startAgain
        if cost<bestCost:
            bestCost=cost
            bestTravel=travel.copy()
    t1_stop = process_time()
    return bestTravel, routeLength(G, bestTravel),(t1_stop-t1_start)
