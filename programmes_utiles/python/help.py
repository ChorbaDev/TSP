import random

def randomSolution(n,town=None):
    cities=list(range(n))
    cities.remove(cities[town])
    solution=[]
    for i in range(n-1):
        randomCity=cities[random.randint(0,len(cities)-1)]
        solution.append(randomCity)
        cities.remove(randomCity)
    return solution

def pathCost(tsp,path,town=None):
    cost=0
    for i in range(len(path)):
        if path[i]==town:
            continue
        cost+=tsp[(town,path[i])]
        town=path[i]
    return cost

