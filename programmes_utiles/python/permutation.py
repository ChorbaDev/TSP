#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# usage pour 1000 permutations :
#
#            ./permutation.py 1000
#

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

nb_perm = int(sys.argv[1])
T = [2*x for x in range(10)]

start_time = time.time()

for i in range(nb_perm):
	permut(T)
#  	print T
	
sec = (time.time()-start_time)
print "les", nb_perm, "permutations ont été générées en", "%.6f"%sec, "secondes"

