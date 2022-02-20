import math
import random

Q = 1


class Edge:
    """
    in order to know if a path is interesting, edges need to contain a certain amount of information
    first the cities that are connected through this edge let i and j
    then the amount of pheromones present on this edge
    we also need the heuristic value attributed to an edge
    """

    def __init__(self, i, j, phi, heuristic):
        self.i = i
        self.j = j
        self.phi = phi
        self.heuristic = heuristic


class Ant:
    def __init__(self, alpha, beta, nCities, edges):
        """
        an ant needs to be able to deposit a certain amount of pheromones
        alpha is the parameter that will allow us to control the amount of pheromones (usually a number between 0 and 1)
        beta is the parameter that will add randomness in the decision of the path during the selection
        an ant needs to know the distance it has traveled, so we can calculate the best path
        in a path, an ant will travel to n_cities using edges
        """
        self.alpha = alpha
        self.beta = beta
        self.nCities = nCities
        self.dist = 0
        self.path = None
        self.edges = edges

    def selectCity(self, tsp):
        """
        Ants will follow the strongest pheromone trail when constructing a solution, but sometimes ants will decide to
        take another path (the randomness) that is useful to find new and better paths. But we need to do this smartly
        So to do this we will introduce a heuristic value, this value will help point towards the best solution possible
        in our case we want the ant to find the shortest path possible between 2 cites.

        TLDR : the ant will sometimes want to pick an edge because it's shorter and the shorter, the better

        in order to accomplish this we use a formula of the following
        probability of an ant picking an edge between city i and j
        = (the pheromone on said edge(with parameter alpha) * the heuristic value of said edge( with parameter beta))
        /
        the sum of the allowed path which means the cities not visited by a given ant

        we apply this using a roulette-wheel -style selection
        :return newCity:
        """
        rouletteWheel = 0
        cities = tsp
        heuristicValue = 0
        for newCity in cities:
            heuristicValue += self.edges[self.path[-1]][newCity].heuristic
        for newCity in cities:
            tau = math.pow(self.edges[self.path[-1]][newCity].phi, self.alpha)
            eta = math.pow(heuristicValue / self.edges[self.path[-1]][newCity].heuristic, self.beta)
            rouletteWheel += tau * eta

        randomValue = random.random()
        wheelPosition = 0

        for newCity in cities:
            tau = math.pow(self.edges[self.path[-1]][newCity].phi, self.alpha)
            eta = math.pow(heuristicValue / self.edges[self.path[-1]][newCity].heuristic, self.beta)
            wheelPosition += tau * eta

            if wheelPosition >= randomValue:
                return newCity

    # def updateLocalPhi(self):
    #     """
    #     every time an ant successfully constructs a solution we update the local pheromone
    #     like in nature, here we need to vary th amount of deposited phi on an edge depending on the solutions score
    #     in our case it depends on the total distance
    #
    #     :return self.path:
    #     """

    def calcDist(self):
        self.dist=0
        for k in range(self.nCities):
            self.dist+=self.edges[self.path[k]][self.path[(k+1)%self.nCities]].heuristic
        return self.dist
