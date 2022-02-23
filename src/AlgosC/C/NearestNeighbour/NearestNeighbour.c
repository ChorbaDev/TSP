#include <limits.h>
#include <stdio.h>
#include "../../utils/help.c"

int find_closest(int** tsp,int* path,int n,int start,int startTown){
    int minPos=start,minCost=INT_MAX;
    for (int i = 0; i < n; ++i) {
        if( start==i || startTown==i || existsIn(path,n,i)==1){
            continue;
        }

        if(minCost> tsp[start][i]){
            minCost=tsp[start][i];
            minPos=i;
        }
    }
    return minPos;
}
void NearestNeighbour(int** tsp,int n,int start,int *path){
    path[0]=start;
    int nextTown=start,lengthPath=0;
    while (lengthPath<n-1){
        int minTown=find_closest(tsp,path,n,nextTown,start);
        lengthPath++;
        path[lengthPath]=minTown;
        nextTown=minTown;
    }
}
