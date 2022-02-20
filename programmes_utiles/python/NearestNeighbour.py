from help import pathCost
from sys import maxsize
from time import process_time

def NearestNeighbour(tsp,n,start):
    path=[]
    path.append(start)
    nextTown=start

    t1_start = process_time()
    while len(path)<n:
        minTown=minimum(tsp,path,n,nextTown,start)
        path.append(minTown)
        nextTown=minTown
    t1_stop = process_time()

    path.append(start)
    totalCost=0
    for i in range(n):
        totalCost+=tsp[(path[i],path[i+1])]

    return path,totalCost,(t1_stop-t1_start)


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
