import random
from time import process_time
def randomSolution(n):
    cities=list(range(n))
    solution=[]
    for i in range(n):
        randomCity=cities[random.randint(0,len(cities)-1)]
        solution.append(randomCity)
        cities.remove(randomCity)
    return solution


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

def hillClimbing(tsp,n):
    currentSolution=randomSolution(n)
    currentRouteLength=routeLength(tsp,currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour,bestNeighbourRouteLength=getBestNeighbour(tsp,neighbours)

    t1_start = process_time()
    while bestNeighbourRouteLength < currentRouteLength:
        print(currentSolution)
        currentSolution=bestNeighbour
        currentRouteLength=bestNeighbourRouteLength
        neighbours=getNeighbours(currentSolution)
        bestNeighbour,bestNeighbourRouteLength=getBestNeighbour(tsp,neighbours)
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start)
    print("Elapsed time during the whole program in seconds:",t1_stop-t1_start)
    print(currentSolution)
    print(currentRouteLength)
