#include <stdio.h>
#include <stdlib.h>
#define INF 999999

int g[4][4]={
		{0,10,15,20},
		{5,0,9,10},
		{6,13,0,12},
		{8,8,9,0}
	};

void tsp(int current, int n, int visited[], int tourcost, int source)
{
	int min=INF;
	visited[current]=1;
	printf("(%d)-->",current+1);
	int i,currcost,j;
	for(i=0;i<n;i++)
	{
		//if(!visited[i] && g[current][i] && (g[current][i]+g[i][current]<min))
		if(!visited[i] && g[current][i] && (g[current][i]<min))
		{
			//min=g[current][i]+g[i][current];
			min=g[current][i];
			currcost=g[current][i]; //travel cost
			j=i; //node index with min cost path
		}
	}

	if(min!=INF)
	{
		tourcost+=currcost;
		tsp(j,n,visited,tourcost, source);
	}
	else
	{
		//all nodes visited
		printf("(%d)\n",source+1);
		tourcost+=g[current][source];
		printf("Tour Cost: %d\n",tourcost);
	}
}
int main()
{
	
	int vis[]={0,0,0,0};
	tsp(0,4,vis,0,0);
	return 0;
}
