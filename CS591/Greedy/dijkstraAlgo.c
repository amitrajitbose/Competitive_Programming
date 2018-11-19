//DIJKSTRA ALGORITHM
//Non Heap Implementation

#include<stdio.h>
#include<stdlib.h>
#define INFINITY 999999
#define MAX 10
 
void dijkstra(int G[MAX][MAX],int n,int startnode);
 
int main()
{
    printf("THIS PROGRAM USES 1-BASED INDEXING FOR MATRIX\n\n\n");
    int G[MAX][MAX],i,j,n,u,k,choice;
    printf("ENTER TOTAL NUMBER OF VERTICES: ");
    scanf("%d",&n);
    for(i=0;i<n;i++){
      for(j=0;j<n;j++){
        G[i][j]=0;
      }
    }
    printf("PRESS '0 0' TO QUIT\n");
    k=0;
    while(1)
    {		
      printf("---EDGE %d ---",k+1);
      k+=1;				
      printf(" ENTER START VERTEX AND END VERTEX: ");
      scanf("%d %d",&i,&j);
      if(i==0 && j==0) 
        break;
      printf("ENTER PATH WEIGHT: ");
      scanf("%d",&G[i-1][j-1]);
    }
    printf("\n");
    
    printf("ARE THE EDGES DIRECTED? (1=YES),(0=NO): ");
    scanf("%d",&choice);
    printf("\n");
    if(choice==0){
      //undirected edges
      for(i=0;i<n;i++){
        for(j=i+1;j<n;j++){
          if(G[i][j]>0){
            G[j][i]=G[i][j];
          }
        }
      }
    }
    else if(choice!=0 && choice!=1)
    {
      printf("INVALID CHOICE");
      exit(0);
    }
    printf("THE ADJACENCY MATRIX IS: \n");
    for(i=0;i<n;i++){
      for(j=0;j<n;j++){
        printf("%d\t",G[i][j]);
      }
      printf("\n");
    }

    printf("\nEnter the starting node:");
    scanf("%d",&u);
    u=u-1;
    dijkstra(G,n,u);
    printf("\n");
    return 0;
}
 
void dijkstra(int G[MAX][MAX],int n,int startnode)
{
 
    int cost[MAX][MAX],distance[MAX],pred[MAX];
    int visited[MAX],count,mindistance,nextnode,i,j;
    
    //pred[] stores the predecessor of each node
    //count gives the number of nodes seen so far
    //create the cost matrix
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            if(G[i][j]==0)
                cost[i][j]=INFINITY;
            else
                cost[i][j]=G[i][j];
    
    //initialize pred[],distance[] and visited[]
    for(i=0;i<n;i++)
    {
        distance[i]=cost[startnode][i];
        pred[i]=startnode;
        visited[i]=0;
    }
    
    distance[startnode]=0;
    visited[startnode]=1;
    count=1;
    
    while(count<n-1)
    {
        mindistance=INFINITY;
        
        //nextnode gives the node at minimum distance
        for(i=0;i<n;i++)
            if(distance[i]<mindistance&&!visited[i])
            {
                mindistance=distance[i];
                nextnode=i;
            }
            
            //check if a better path exists through nextnode            
            visited[nextnode]=1;
            for(i=0;i<n;i++)
                if(!visited[i])
                    if(mindistance+cost[nextnode][i]<distance[i])
                    {
                        distance[i]=mindistance+cost[nextnode][i];
                        pred[i]=nextnode;
                    }
        count++;
    }
 
    //print the path and distance of each node
    for(i=0;i<n;i++)
        if(i!=startnode)
        {
            printf("\nDistance of Vertex %d = %d",i+1,distance[i]);
            printf("\nPath = %d",i+1);
            
            j=i;
            do
            {
              j=pred[j];
              printf("<--%d",j+1);
            }while(j!=startnode);
    }
}

// https://www.thecrazyprogrammer.com/2014/03/dijkstra-algorithm-for-finding-shortest-path-of-a-graph.html