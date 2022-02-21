import random

def randomSolution(n,town=None):
    cities=list(range(n))
    solution=[town]
    cities.remove(town)
    for i in range(n-1):
        randomCity=cities[random.randint(0,len(cities)-1)]
        solution.append(randomCity)
        cities.remove(randomCity)
    return solution
"""
 (v,x) ; (u,w)
 ( (v,w)+(ux) ) - ( (uw)+(vx) )
 new - old
"""
def cost_change(tsp, v, x, u, w):
    return tsp[(v, u)] + tsp[(x, w)] - tsp[(v, x)] - tsp[(u, w)]

def routeLength(tsp, solution):
    routeLength=0
    for i in range(len(solution)):
        routeLength+=tsp[(solution[i-1],solution[i])]
    return routeLength
