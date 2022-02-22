from src.utils.help import routeLength
import random

import time


def randomValue(a, b, start):
    x=random.randint(a,b)
    while x==start:
        x=random.randint(a,b)
    return x


def randomEdge(n,start):
    x= randomValue(0,n-1,start)
    y=randomValue(0,n-1,start)
    while x==y:
       y=randomValue(0,n-1,start)
    return x,y

def permute(path, i, j):
    aux=path[i]
    path[i]=path[j]
    path[j]=aux
    return path


def EchangeDeuxSommets(tsp,path,s):
    t_end= time.time()+s
    bestPath=path.copy()
    bestCost=routeLength(tsp,path)
    start=path[0]
    improve,comparisons,iterations=0,0,0

    while time.time() < t_end:
        i,j=randomEdge(len(path),start)
        path=permute(path,i,j)
        cost=routeLength(tsp,path)
        if bestCost>cost:
            improve+=1
            bestCost=cost
            bestPath=path.copy()
        iterations+=1
    return bestPath,bestCost,comparisons,improve,iterations
