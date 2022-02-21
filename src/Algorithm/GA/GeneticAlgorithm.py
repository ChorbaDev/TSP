from src.utils.help import *

"""
Steps :
1. creating initial population
2. calculating fitness
3. selecting the best genes
4. crossing over
5. mutating to introduce variation

Algorithm:
1. Init pop
2. Determine the fitness of the chromosome
3. Until done repeat:
    1. Select parents
    3. Calculate the fitness of the new population
    4. Append it to the gene pool
"""

INT_MAX = 9223372036854775807

N_CITIES = 10

START = 0

POP_SIZE = 10


class LifeForm:

    def __init__(self) -> None:
        self.gnome = ""
        self.fitness = 0

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness


def mutatedGene(gnome):
    gnome = list(gnome)
    while True:
        r1 = rand_num(1, N_CITIES)
        r2 = rand_num(1, N_CITIES)
        if r2 != r1:
            return swap(gnome, r1, r2)

