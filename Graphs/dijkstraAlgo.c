//DIJKSTRA ALGORITHM
#define MAX 10
#include <stdio.h>
#include <stdlib.h>
int mat[MAX][MAX];
int main()
{
	int k,v,e,i,j;

	printf("ENTER TOTAL NUMBER OF VERTICES: ");
	scanf("%d",&v);
	//printf("ENTER TOTAL NUMBER OF EDGES: ");
	//scanf("%d",&e);
	printf("PRESS '0 0' TO QUIT\n");
	while(1)
	{		
		printf("---EDGE %d ---",k+1);				
		printf("ENTER START VERTEX AND END VERTEX: ");
		scanf("%d %d",&i,&j);
		if(i==0) 
		break;
		printf("ENTER PATH WEIGHT: ");
		scanf("%d",&mat[i-1][j-1]);
	}
	printf("\n");
	for(i=0;i<v;i++){
		for(j=0;j<v;j++){
			printf("%d\t",mat[i][j]);
		}
		printf("\n");
	}
	return 0;
}

	
