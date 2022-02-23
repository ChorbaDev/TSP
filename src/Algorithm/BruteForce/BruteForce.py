from math import factorial
from sys import maxsize
from time import process_time
from src.utils.help import next_perm

#complexity of O(n!)

def BruteForce(tsp,n,startCity):
    vertex=[]
    for i in range(n):
        if i != startCity:
            vertex.append(i)
    minCost=maxsize
    bestPath=[]
    bestPath.append(startCity)
    t1_start = process_time()
    while next_perm(vertex):
        currentCost=0
        k=startCity
        for i in range(len(vertex)):
            currentCost+=tsp[(k,vertex[i])]
            if currentCost>=minCost:
                break
            k=vertex[i]
        currentCost+=tsp[(k,startCity)]
        if currentCost<minCost:
            minCost=currentCost
            bestPath=vertex.copy()
    t1_stop = process_time()
    bestPath.insert(0,startCity)
    return bestPath,minCost,(t1_stop-t1_start)


