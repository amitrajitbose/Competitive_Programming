#include <stdio.h>
#include <stdlib.h>

void dfs(int v,int n, int adj[][n], int visited[])
{
	visited[v]=1;
	printf("Visit: %d\n",v);
	int w;
	for(w=0;w<n;w++)
	{
		if(adj[v][w]>0 && !visited[w])
		{
			dfs(w,n,adj,visited);
		}
	}
}
int main()
{
	int adj[4][4]={
              {0,0,1,10}, 
              {1,0,3,1}, 
              {1,1,0,1}, 
              {1,1,1,0} 
            }; 
  int visited[]={0,0,0,0};
  dfs(0,4,adj,visited);
  return 0;
}