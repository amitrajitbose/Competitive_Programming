/*
Author: Amitrajit Bose
CSE 3A (13)
Floyd Warshall Algorithm
*/

#include <stdlib.h>
#include <stdio.h>
#define MAX 10
#define INF 9999
#define for(i,a,b) for(i=a;i<=b;i++)
int min(int x,int y){
	return (x>y)?y:x;
}
int main()
{
	int D[MAX][MAX],P[MAX][MAX];
	int n,i,j,k;
	printf("Enter Total Vertices: ");
	scanf("%d ",&n);

	//initialising W and D
	for(i,1,n){
		for(j,1,n){
			D[i][j]=INF;
			P[i][j]=INF;
			if(i==j){
				D[i][j]=0;
				P[i][j]=0;
			}
		}
	}
	
	//taking input in the array D
	printf("**VERTEX INDEX STARTS FROM 1**\n**PRESS 0 0 TO STOP**\n");
	printf("**ENTER START INDEX, END INDEX**\n");
	printf("**EDGE WEIGHT**\n");
	
	while(1)
	{
		scanf("%d %d",&i,&j);
		scanf("%d ",&D[i][j]);
		P[i][j]=D[i][j];
		if(i==0 || j==0)
			break;
	}
	/*
	PRINT WEIGHTED MATRIX
	for(i,1,n){
		for(j,1,n){
			printf("%d ",D[i][j]);
		}
		printf("\n");
	}
	*/
	for(k,1,n){
		for(i,1,n){
			for(j,1,n){
				if(i!=k || j!=k)
					P[i][j]=min(D[i][j],(D[i][k]+D[k][j]));
			}
		}
		for(i,1,n){
			for(j,1,n){
				D[i][j]=P[i][j];
			}
		}
	}
	
	printf("\nDISTANCE MATRIX\n");
	for(i,1,n){
		for(j,1,n){
			printf("%d ",D[i][j]);
		}
		printf("\n");
	}
	return 0;
}
