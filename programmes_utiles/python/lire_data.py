#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# usage :
#            ./lire_data.py communes_10.txt
#

import sys
from HillClimbing import hillClimbing
from BruteForce import  BruteForce
from Random import RandomSolution
from NearestNeighbour import NearestNeighbour
def lire(name):
	f = open(name,"r")
	s = f.readline()
	[n, m] = [int(x) for x in s.split(" ")]
	g = dict()
	for i in range(m):
		s = f.readline()
		if s=="":
			break
		else:
			[i, j, p] = [int(x) for x in s.split(" ")]
			g[(i, j)] = p
			g[(j, i)] = p
	f.close()
	return n, m, g

G = dict()
nom = sys.argv[1]
n, m, G = lire(nom)

print ("nombre de sommets :", n)
print ("nombre d'arêtes   :", m)
print ("tableau des distances :")
for i in range(n):
	for j in range(n):
		if i == j:
			print("  0", end=" "),
		else:
			print (G[(i,j)], end=" "),
	print()
#BruteForce(G,n,0)
#RandomSolution(G,0,n,2)
NearestNeighbour(G,n,0)
