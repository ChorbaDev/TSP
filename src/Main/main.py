from lire_data import lire
from src.Algorithm.ACO.ACO import ACO
from src.Algorithm.BruteForce.BruteForce import BruteForce
from src.Algorithm.HillClimbing.HillClimbing import hillClimbing
from src.Algorithm.NearestInsertion.NearestInsertion import NearestInsertion
from src.Algorithm.NearestNeighbour.NearestNeighbour import NearestNeighbour
from src.Algorithm.Optimization.EchangeDeuxSommets import EchangeDeuxSommets
from src.Algorithm.Optimization.three_opt import three_opt
from src.Algorithm.Optimization.two_opt import two_opt
from src.Algorithm.Random.Random import RandomSolution
from src.Algorithm.GA.GeneticAlgorithm import genetic_algorithm
from src.utils.colors import bcolors
from src.utils.help import printGraph, routeLength
from src.utils.drawingMap import drawPath
import sys

nom = "../../communes/communes/" + sys.argv[1]
file = "../../communes/communes.xlsx"

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
path, cost, time = [], 0, 0
if algo == 1:
    path, cost, time = RandomSolution(G, chosenStartTown, n, chosenTime)
elif algo == 2:
    path, cost, time = BruteForce(G, n, chosenStartTown)
elif algo == 3:
    path, cost, time = NearestNeighbour(G, n, chosenStartTown)
elif algo == 4:
    path, cost, time = NearestInsertion(G, n, 7)
elif algo == 5:
    path, cost, time = hillClimbing(G, n, chosenStartTown)
elif algo == 6:
    path, cost, time = genetic_algorithm(G, n, 100, 0.3, 10000)
elif algo==7:
    path, cost, time=ACO(G,n, chosenStartTown, 100000, 0.05,0.0453, 1,1,1)

print(bcolors.BOLD + "Starting city :", bcolors.OKGREEN, int(sys.argv[2], 10), bcolors.ENDC)
print(bcolors.BOLD + "Path: ", bcolors.OKGREEN, path, bcolors.ENDC)
print(bcolors.BOLD + "Cost: ", bcolors.OKGREEN, cost, bcolors.ENDC)
print(bcolors.BOLD + bcolors.OKCYAN + "Time: %.6f " % time, bcolors.ENDC)
# optimization
print(bcolors.BOLD + bcolors.WARNING + "Do you want to optimize?:")
print(bcolors.UNDERLINE + "1- Simple Exchange")
print("2- (2-Opt) Exchange")
print("3- (3-Opt) Exchange")
print("4- No, Thanks." + bcolors.ENDC)
answer = int(input("->"))
bestPath, bestCost, comparisons, improve, iterations = [], 0, 0, 0, 0
if answer == 1:
    bestPath, bestCost, comparisons, improve, iterations = EchangeDeuxSommets(G, path.copy(), chosenTime)
elif answer == 2:
    bestPath, bestCost, comparisons, improve, iterations = two_opt(path.copy(),G)
elif answer == 3:
    bestPath, bestCost, comparisons, improve, iterations = three_opt(path.copy(),G)

if answer in range(1, 4):
    print(bcolors.BOLD + "Number of improvements is: ", bcolors.OKGREEN, improve, bcolors.ENDC)
    print(bcolors.BOLD + "Number of iterations is: ", bcolors.OKGREEN, iterations, bcolors.ENDC)
    path = bestPath.copy()
    if answer == 2 or answer==3:
        print(bcolors.BOLD + "Number of comparisons is: ", bcolors.OKGREEN, comparisons, bcolors.ENDC)
    print(bcolors.BOLD + "The optimized path is: ", bcolors.OKGREEN, bestPath, bcolors.ENDC)
    print(bcolors.BOLD + "The optimized cost is: ", bcolors.OKGREEN, bestCost, bcolors.ENDC)

print(bcolors.BOLD + bcolors.WARNING + "Do you want to plot the graph?")
print(bcolors.UNDERLINE + "1- Plot graph.")
print("2- Please, exit." + bcolors.ENDC)
answer = int(input("->"))
if answer == 1:
    path.append(path[0])
    drawPath(file=file, scale=n, paths=path)

print(bcolors.HEADER + "See you! Salesman.")
# 2731

# print(two_opt([0, 9, 7, 2, 1, 4, 6, 3, 8, 5] ,G))
