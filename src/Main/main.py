from lire_data import lire
from src.Algorithm.BruteForce.BruteForce import BruteForce
from src.Algorithm.HillClimbing.HillClimbing import hillClimbing
from src.Algorithm.NearestInsertion.NearestInsertion import NearestInsertion
from src.Algorithm.NearestNeighbour.NearestNeighbour import NearestNeighbour
from src.Algorithm.Optimization.EchangeDeuxSommets import EchangeDeuxSommets
from src.Algorithm.Optimization.two_opt import two_opt
from src.Algorithm.Random.Random import RandomSolution
from src.Algorithm.GA.GeneticAlgorithm import geneticAlgorithm
from src.utils.colors import bcolors
from src.utils.help import printGraph
import sys

nom = "../../communes/communes/" + sys.argv[1]

numberOfAlgos = 11
while True:
    print(bcolors.BOLD + "Choose your algorithm:" + bcolors.ENDC + bcolors.OKBLUE)
    print("1- Random")
    print("2- Brute Force")
    print("3- Nearest Neighbor")
    print("4- Nearest Insertion")
    print("5- Hill Climbing")
    print("6- Genetic Algorithm")
    print("7- Ant Colony Optimization" + bcolors.ENDC)
    algo = int(input(bcolors.WARNING + "->" + bcolors.ENDC))
    if algo in range(1, numberOfAlgos):
        break
n, m, G = lire(nom)
print(bcolors.BOLD + "Number of towns :" + bcolors.OKGREEN, n, bcolors.ENDC)
print(bcolors.BOLD + "Number of edges   :" + bcolors.OKGREEN, m, bcolors.ENDC)
print(bcolors.BOLD + "Graph :" + bcolors.ENDC)
printGraph(G, n)
chosenTime = int(sys.argv[3], 10)
chosenStartTown = int(sys.argv[2], 10)
switcher = {
    1: RandomSolution(G, chosenStartTown, n, chosenTime),
    2: BruteForce(G, n, chosenStartTown),
    3: NearestNeighbour(G, n, chosenStartTown),
    4: NearestInsertion(G, n, 7),
    5: hillClimbing(G, n, chosenStartTown),
    6: geneticAlgorithm(G, n, 100, 20, 0.01, generations=500),
    # 7:NearestInsertion(G,n,7),
}
path, cost, time = switcher.get(algo)
print(bcolors.BOLD + "Starting city :", bcolors.OKGREEN, int(sys.argv[2], 10), bcolors.ENDC)
print(bcolors.BOLD + "Path: ", bcolors.OKGREEN, path, bcolors.ENDC)
print(bcolors.BOLD + "Cost: ", bcolors.OKGREEN, cost, bcolors.ENDC)
print(bcolors.BOLD + bcolors.OKCYAN + "Time: %.6f " % time, bcolors.ENDC)
# optimization
print(bcolors.BOLD + bcolors.WARNING + "Do you want to optimize?:")
print(bcolors.UNDERLINE + "1- Simple Exchange")
print("2- (2-Opt) Exchange")
print("3- No, Thanks." + bcolors.ENDC)
answer = int(input("->"))
if answer in range(1,3):
    switcher={
        1:EchangeDeuxSommets(G,path.copy(),chosenTime),
        2:two_opt(path.copy(),G),
    }
    bestPath,bestCost,comparisons,improve,iterations=switcher.get(answer)
    print(bcolors.BOLD+"Number of improvements is: ",bcolors.OKGREEN,improve,bcolors.ENDC)
    print(bcolors.BOLD+"Number of iterations is: ",bcolors.OKGREEN,iterations,bcolors.ENDC)
    if answer==2:
        print(bcolors.BOLD+"The comparisons is: ",bcolors.OKGREEN,comparisons,bcolors.ENDC)
    print(bcolors.BOLD+"The optimized path is: ",bcolors.OKGREEN,bestPath,bcolors.ENDC)
    print(bcolors.BOLD+"The optimized cost is: ",bcolors.OKGREEN,bestCost,bcolors.ENDC)
print(bcolors.HEADER+"See you! Salesman.")
#2731
#print(routeLength(G,[0, 9, 7, 2, 1, 4, 6, 3, 8, 5] ))
#print(two_opt([0, 9, 7, 2, 1, 4, 6, 3, 8, 5] ,G))
