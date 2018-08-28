/*
 * Author: Amitrajit Bose
 *
 * Problem: Given an undirected (edge weights do not matter) graph,
 * determine if it can be colored with maximum of m colors. So, that
 * it satisfies the graph coloring problem properties.
 * https://en.wikipedia.org/wiki/Graph_coloring
 *
 * Approach: Backtracking & Recursion
 * 
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define N 5

int graph[N][N]={
        {0,1,0,1,1},
        {0,0,1,0,0},
        {0,1,0,1,0},
        {1,0,0,0,1},
        {1,0,0,1,0}
    };

int m=3;
int x[N];
int i;

void print(int color[N]){
    int i;
    for(i=0;i<N;i++){
        printf("%d ",color[i]);
    }
    printf("\n");
}

void nextColor(int k){
    while(true){
        x[k]=(x[k]+1)%(m+1); //next highest color assigned
        if(x[k]==0) //returning back to 0 viz, 1,2,3,4,..n,0, thus color exhausted
            return;
        int i;
        for(i=0;i<N;i++){
            if(graph[i][k]==1 && x[k]==x[i])
                break;
        }
        if(i==N)
            return; //new color found
        //because i can never be n inside the loop, thus this will be returned
        //only when the entire for loop is executed for all values
    }
}

void mColor(int k){
    while(true){
        nextColor(k);
            if(x[k]==0)
                return;
            else if(k==N)
                print(x);
            else
                mColor(k+1);
    }
}
int main(){
    for(i=0; i<N; i++)
        x[i]=0;
    mColor(0);
    return 0;
}