#ifndef TSP_NEARESTNEIGHBOUR_H
#define TSP_NEARESTNEIGHBOUR_H

void NearestNeighbour(int** tsp,int n,int start,int *path);
int find_closest(int** tsp,int* path,int n,int start,int startTown);

#endif //TSP_NEARESTNEIGHBOUR_H
