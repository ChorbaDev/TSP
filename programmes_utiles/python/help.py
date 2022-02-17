import random

def randomSolution(n):
    cities=list(range(n))
    solution=[]
    for i in range(n):
        randomCity=cities[random.randint(0,len(cities)-1)]
        solution.append(randomCity)
        cities.remove(randomCity)
    return solution

def pathCost(tsp,town,path):
    cost=0
    for i in range(len(path)):
        if path[i]==town:
            continue
        cost+=tsp[(town,path[i])]
        town=path[i]
    return cost

