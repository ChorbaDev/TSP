import random
from time import process_time
from help import randomSolution
def routeLength(tsp, solution):
    routeLength=0
    for i in range(len(solution)):
        routeLength+=tsp[(solution[i-1],solution[i])]
    return routeLength


def getNeighbours(solution):
    neighbours=[]
    for i in range(len(solution)):
        for j in range(i+1,len(solution)):
            neighbour=solution.copy()
            neighbour[i]=solution[j]
            neighbour[j]=solution[i]
            neighbours.append(neighbour)
    return neighbours

def getBestNeighbour(tsp,neighbours):
    bestRouteLength=routeLength(tsp,neighbours[0])
    bestNeighbour=neighbours[0]
    for neighbour in neighbours:
        currentRouteLength=routeLength(tsp,neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength=currentRouteLength
            bestNeighbour=neighbour
    return bestNeighbour,bestRouteLength

def hillClimbing(tsp,n,town):
    currentSolution=randomSolution(n,town)
    currentRouteLength=routeLength(tsp,currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour,bestNeighbourRouteLength=getBestNeighbour(tsp,neighbours)

    t1_start = process_time()
    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution=bestNeighbour
        currentRouteLength=bestNeighbourRouteLength
        neighbours=getNeighbours(currentSolution)
        bestNeighbour,bestNeighbourRouteLength=getBestNeighbour(tsp,neighbours)
    t1_stop = process_time()
    return currentSolution,currentRouteLength,(t1_stop-t1_start)