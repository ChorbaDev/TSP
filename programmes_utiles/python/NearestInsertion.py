#complexity O(n^2)
from help import randomSolution,routeLength
from sys import maxsize
import random
from time import process_time

def NearestInsertion(tsp,n,town):
	points = list(range(n))
	current = town
	points.remove(current)

	i = current
	j = points[0]
	cij = tsp[(i,j)]
	for point in points:
		if tsp[(i, point)] < cij:
			cij = tsp[(i, point)]
			j = point
	points.remove(j)

	edges = [(i,j)]

	visited = []
	visited.append(i)
	visited.append(j)

	t1_start = process_time()
	while len(points) > 0:
		i = visited[0]
		k = points[0]
		crj = tsp[(k, i)]

		for point in points:
			for c in visited:
				dist = tsp[(point, c)]
				if dist < crj:
					k = point

		i = edges[0][0]
		j = edges[0][1]

		c_min = tsp[(i, k)]  + tsp[(k, j)]  - tsp[(i, j)]
		#step 4
		for e in edges:
			aux_i = e[0]
			aux_j = e[1]
			dist = tsp[(aux_i, k)]  + tsp[(k,aux_j)] - tsp[(aux_i,aux_j)]
			if dist < c_min:
				c_min = dist
				i = aux_i
				j = aux_j

		edges.remove((i,j))
		edges.append((i,k))
		edges.append((k,j))

		visited.append(k)
		points.remove(k)
	t1_stop = process_time()


	cost = 0
	for e in edges:
		cost += tsp[e]
	return edges,cost,(t1_stop-t1_start)

"""
Step 1. Start with a sub-graph consisting of node i only.
Step 2. Find node r such that cir is minimal and form sub-tour i-r-i.
Step 3. (Selection step) Given a sub-tour, find node r not in the sub-tour closest to any node j in the sub-tour; i.e. with minimal crj
Step 4. (Insertion step) Find the arc (i, j) in the sub-tour which minimizes cir + crj - cij . Insert r between i and j.
Step 5. If all the nodes are added to the tour, stop. Else go to step 3
"""
