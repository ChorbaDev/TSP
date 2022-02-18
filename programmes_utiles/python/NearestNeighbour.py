from help import pathCost
from sys import maxsize
from time import process_time

def NearestNeighbour(tsp,n,start):
    path=[]
    startTown=start
    t1_start = process_time()
    while len(path)<n-1:
        minTown=minimum(tsp,path,n,start,startTown)
        path.append(minTown)
        start=minTown
    totalCost=pathCost(tsp,path,start)
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start)
    print("Elapsed time during the whole program in seconds:",t1_stop-t1_start)

    print(path)
    print(totalCost)

def minimum(tsp,path,n,start,startTown):
    minCost=maxsize
    minPos=start
    for i in range(n):
        if start==i or startTown==i or i in path:
            continue
        if minCost>tsp[(start,i)]:
            minCost=tsp[(start,i)]
            minPos=i
    return minPos
