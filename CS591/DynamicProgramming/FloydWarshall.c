#include <stdio.h>
#include <stdlib.h>
#define INF 999999

int min(int a, int b)
{
	return (a>b)?b:a;
}

int main()
{
	int n=5; //number of vertices
	int A[5][5]={
		{0, 1, -1, 1, 5},
		{9, 0, 3, 2, -1},
		{-1,-1,0,4,-1},
		{-1,-1,2,0,3},
		{3,-1,-1,-1,0}};
	//convert -1 edges(no edge) to infinities
	int i,j,k,num;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(A[i][j]==-1){
				A[i][j]=INF;
			}
		}
	}
	//Floyd Warshall Algorithm begins here
	for(k=0;k<n;k++)
	{
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				A[i][j]=min(A[i][j],(A[i][k]+A[k][j]));
			}
		}
	}
	//print resultant matrix
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(A[i][j]==INF)
				printf("-1 ");
			else
				printf("%d ",A[i][j]);
		}
		printf("\n");
	}
	return 0;
}