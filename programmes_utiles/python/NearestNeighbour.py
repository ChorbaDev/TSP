from help import pathCost
from sys import maxsize

def NearestNeighbour(tsp,n,start):
    path=[]
    startTown=start
    while len(path)<n-1:
        minTown=minimum(tsp,path,n,start,startTown)
        path.append(minTown)
        start=minTown
    totalCost=pathCost(tsp,path,start)
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
