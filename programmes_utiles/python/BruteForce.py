from sys import maxsize
from time import process_time

def BruteForce(tsp,n,startCity):
    vertex=[]
    for i in range(n):
        if i != startCity:
            vertex.append(i)
    minCost=maxsize
    t1_start = process_time()
    count=0
    while next_perm(vertex):
        currentCost=0
        k=startCity
        for i in range(len(vertex)):
            currentCost+=tsp[(k,vertex[i])]
            if currentCost>=minCost:
                break
            k=vertex[i]
        currentCost+=tsp[(k,startCity)]
        minCost = min(minCost, currentCost)
        count+=1
    print(count)
    print(minCost)
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start)
    print("Elapsed time during the whole program in seconds:",t1_stop-t1_start)


def next_perm(l):
    n = len(l)
    i = n-2

    while i >= 0 and l[i] > l[i+1]:
        i -= 1

    if i == -1:
        return False

    j = i+1
    while j < n and l[j] > l[i]:
        j += 1

    j -= 1

    l[i], l[j] = l[j], l[i]
    left = i+1
    right = n-1

    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return True
