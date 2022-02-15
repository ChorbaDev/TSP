//
// Created by omar on 14/02/2022.
//

#include "PPV.h"
#include <limits.h>
int start1,sum=0,count=0;
void PPV(Graphe g,int nbVilles, int villeDep,int *visite,int *path){
    int minDistance=INT_MAX,cur,flag=-1,i,minVille;
    visite[villeDep]=1;
    for (i = 0; i < nbVilles; ++i) {
        if(visite[i]==1 || villeDep==i)
            continue;
        if(g[villeDep][i]<minDistance){
            minDistance=g[villeDep][i];
            minVille=i;
            cur=i;flag=0;
        }
    }
    path[count]=minVille;
    count++;
    if(flag==-1){
        sum+=g[villeDep][start1];
        printf("\nDistance total : %d\n",sum);
        return;
    }
    sum+=g[villeDep][cur];
    PPV(g,nbVilles,cur,visite,path);
}