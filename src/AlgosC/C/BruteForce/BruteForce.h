#ifndef TSP_BRUTEFORCE_H
#define TSP_BRUTEFORCE_H

void swap(int* sb,int l,int r);
void BruteForce(int** tsp,int n,int startCity,int* path);
int nextPermutation(int *sb,int n);
void reverse(int* sb,int l,int r);
int binarySearch(int* sb,int l,int r,char val);
void insertInPos(int * path,int n,int pos, int town);

#endif //TSP_BRUTEFORCE_H
