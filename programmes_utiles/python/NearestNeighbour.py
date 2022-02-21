from sys import maxsize
from time import process_time
from help import routeLength
def NearestNeighbour(tsp,n,start):
    path=[start]
    nextTown=start

    t1_start = process_time()
    while len(path)<n:
        minTown=find_closest(tsp,path,n,nextTown,start)
        path.append(minTown)
        nextTown=minTown
    t1_stop = process_time()

    totalCost=routeLength(tsp,path)

    return path,totalCost,(t1_stop-t1_start)


def find_closest(tsp,path,n,start,startTown):
    minCost=maxsize
    minPos=start
    for i in range(n):
        if start==i or startTown==i or i in path:
            continue
        if minCost>tsp[(start,i)]:
            minCost=tsp[(start,i)]
            minPos=i
    return minPos
