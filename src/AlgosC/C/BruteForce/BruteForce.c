#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include "../../utils/help.c"
// swap two characters of string
void swap(int* sb,int l,int r)
{
    char temp = sb[l];
    sb[l]=sb[r];
    sb[r]=temp;
}

void reverse(int* sb,int l,int r)
{
    while(l < r)
    {
        swap(sb,l,r);
        l++;
        r--;
    }
}

// function to search a character lying between index l and r
// which is closest greater (just greater) than val
// and return it's index
int binarySearch(int* sb,int l,int r,char val)
{
    int index = -1;

    while (l <= r)
    {
        int mid = (l+r)/2;
        if (sb[mid] <= val)
        {
            r = mid - 1;
        }
        else
        {
            l = mid + 1;
            if (index == -1 || sb[index] >= sb[mid])
                index = mid;
        }
    }
    return index;
}
void insertInPos(int * path,int n,int pos, int town){
 n++;
    for (int i = n-1; i >= pos; i--)
        path[i] = path[i - 1];
    // insert town at pos
    path[pos - 1] = town;
}

// this function generates next permutation (if there exists any such permutation) from the given string
// and returns True
// Else returns false
int nextPermutation(int *sb,int n)
{
    int len = n;
    int i = len-2;

    while (i >= 0 && sb[i] >= sb[i+1])
        i--;

    if (i < 0)
        return -1;
    else
    {
        int index = binarySearch(sb,i+1,len-1,sb[i]);
        swap(sb,i,index);
        reverse(sb,i+1,len-1);
        return 1;
    }
}

void BruteForce(int** tsp,int n,int startCity,int* path){
    int *vertex= malloc(sizeof(int)*n);
    int j=0;
    for (int i = 0; i < n; ++i) {
        if(i!=startCity){
            vertex[j]=i;
            j++;
        }
    }
    int minCost=INT_MAX;
    int *bestPath= malloc(sizeof(int)*n);
    while (nextPermutation(vertex,n-1)>0){
        int currentCost=0;
        int k=startCity;
        for (int i = 0; i < n-1; ++i) {
            currentCost+=tsp[k][vertex[i]];
            if(currentCost>=minCost)
                break;
            k=vertex[i];
        }
        currentCost+=tsp[k][startCity];
        if(currentCost<minCost){
            copyArray(bestPath,vertex,n);
            minCost=currentCost;
        }
    }
    insertInPos(bestPath,n,0,startCity);
    copyArray(path,bestPath,n);
    free(bestPath);
    free(vertex);
}