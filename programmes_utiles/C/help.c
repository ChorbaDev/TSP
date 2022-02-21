#include <time.h>
#include <stdlib.h>
#include <stdio.h>
void affiche_path(int * path, int n){
    for (int i = 0; i < n; ++i) {
        printf("%d ",path[i]);
    }
    printf("\n");
}
int existsIn(int* path,int n,int i){
    for (int j = 0; j < n; ++j) {
        if(i==path[j])
            return 1;
    }
    return -1;
}
int randomIntInPath(int n,int startTown,int* path){
    int randomnumber = rand() % n;
    while ( (randomnumber==startTown) || (existsIn(path,n,randomnumber)==1) ){
        randomnumber = rand() % n;
    }

    return randomnumber;
}
void initPath(int* path,int n){
    for (int i = 0; i < n; ++i) {
        path[i]=-1;
    }
}
void randomSolution(int n,int startTown,int* path){
    initPath(path,n);
    path[0]=startTown;
    for (int i = 0; i < n-1; i++) {
        int a=randomIntInPath(n,startTown,path);
        path[i+1]=a;

    }
}
void copyArray(int* dst,int* src,int n){
    for (int i = 0; i < n; ++i) {
        dst[i]=src[i];
    }
}
int cost_change(int **tsp,int v,int x,int u,int w){
    return tsp[v][u] + tsp[x][w] - tsp[v][x]- tsp[u][w];
}

int routeLength(int **tsp,int n,int* solution){
    int routeLength=0;
    routeLength+=tsp[solution[0]][solution[n-1]];
    for (int i = 0; i < n-1; ++i) {
        routeLength+=tsp[solution[i]][solution[i+1]];
    }
    return routeLength;
}
