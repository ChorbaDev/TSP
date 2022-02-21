#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# usage pour 1000 permutations :
#
#            ./permutation.py 1000
##attention c'est du 2.7 donc pas du 3.0 donc risque de pas marcher j'ai ajouter des () mais je sais pas si ça marche

import sys
import time
import numpy as np

def permut(L):
	N = len(L)
	for i in range(N-1):
# 		nombre au hasard entre 1 et N-1 inclus
		v = np.random.randint(i, N)
		yam = L[i]
		L[i] = L[v]
		L[v] = yam

nb_perm = int(sys.argv[1],10)
T = [2*x for x in range(10)]

start_time = time.time()

for i in range(nb_perm):
	print(T)
	permut(T)
#  	print T
	
sec = (time.time()-start_time)
print ("les", nb_perm, "permutations ont été générées en", "%.6f"%sec, "secondes")
#print("les", nb_perm, "permutations ont été générées en", "%.6f"%sec, "secondes")

