import time
from time import process_time
from help import randomSolution,pathCost
from sys import maxsize

def RandomSolution(tsp,town,n,s):
    t_end= time.time()+s
    bestCost=maxsize
    bestPath=[]
    t1_start = process_time()
    while time.time() < t_end:
        path=randomSolution(n)
        cost=pathCost(tsp,town,path)
        if bestCost>cost:
            bestCost=cost
            bestPath=path.copy()

    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start)
    print("Elapsed time during the whole program in seconds:",t1_stop-t1_start)
    print("Best Cost:", bestCost)
    print("Best path:", bestPath)
