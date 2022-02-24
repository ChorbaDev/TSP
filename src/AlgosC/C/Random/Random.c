//
// Created by omar on 21/02/2022.
//
#include "../../utils/help.c"
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
void randomPath(int** tsp,int town,int n,int* path,int permutations){
    srand(time(NULL));
    int *bestPath= malloc(sizeof(int)*n);
    int bestCost=INT_MAX,cost;
    for (int i = 0; i < permutations; ++i) {
        randomSolution(n,town,path);
        cost= routeLength(tsp,n,path);
        if(bestCost>cost){
            copyArray(bestPath,path,n);
            bestCost=cost;
        }
    }
    copyArray(path,bestPath,n);
}

