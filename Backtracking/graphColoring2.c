/*
 * Author: Amitrajit Bose
 *
 * Problem: Given an undirected (edge weights do not matter) graph,
 * determine if it can be colored with maximum of m colors. So, that
 * it satisfies the graph coloring problem properties.
 * https://en.wikipedia.org/wiki/Graph_coloring
 * --->This is the generalised implementation.<---
 * Approach: Backtracking & Recursion
 * 
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define N 5

void print(int color[N]){
    int i;
    static int kcount=0;
    printf("#%d:\t ",++kcount);
    for(i=0;i<N;i++){
        printf("%d ",color[i]);
    }
    printf("\n");
}

void nextColor(int k, int x[N], int graph[N][N], int m){
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

void mColor(int k, int x[N], int graph[N][N], int m){
    while(true){
        nextColor(k,x,graph,m);
            if(x[k]==0)
                return;
            else if(k==N)
                print(x);
            else
                mColor(k+1,x,graph,m);
    }
}
int main(){
    int graph[N][N]={
        {0,1,0,1,1},
        {0,0,1,0,0},
        {0,1,0,1,0},
        {1,0,0,0,1},
        {1,0,0,1,0}
    };
    /*
    
    Graph looks like this somewhat:
    
    (E)---(A)---(B)
     \    |     |
      \  |     |
       (D)---(C)

    */
    int m;
    printf("Enter m: ");
    scanf("%d",&m);
    int x[N];
    int i;
    for(i=0; i<N; i++)
        x[i]=0;
    printf("__Possible Solutions__\n\n");
    mColor(0,x,graph,m);
    return 0;
}