#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# usage :
#            ./lire_data.py communes_10.txt
#
import sys
# from src.Algorithm.Random.Random import RandomSolution
# from src.utils.help import routeLength

def lire(name):
    f = open(name, "r")
    s = f.readline()
    [n, m] = [int(x) for x in s.split(" ")]
    g = dict()
    for i in range(m):
        s = f.readline()
        if s == "":
            break
        else:
            [i, j, p] = [int(x) for x in s.split(" ")]
            g[(i, j)] = p
            g[(j, i)] = p
    f.close()
    return n, m, g
