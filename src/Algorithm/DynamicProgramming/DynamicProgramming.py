from time import process_time

from help import randomSolution,routeLength
from sys import maxsize
import random
#O(n^2*2^n) not optimal
def tsp(G,n,VISITED_ALL,mask,pos):
    if(mask==VISITED_ALL):
        return G[(pos,0)]
    ans=maxsize
    for city in range(n):
        if(mask&(1<<city))==0:
            newAns=G[(pos,city)]+tsp(G,n,VISITED_ALL,mask|(1<<city),city)
            ans=min(ans,newAns)
    return ans

def DynamicProgramming(G,n,start):
    VISITED_ALL=(1<<n)-1
    t1_start = process_time()
    cost=(tsp(G,n,VISITED_ALL,1,start))
    t1_stop = process_time()
    return [],cost,(t1_stop-t1_start)
