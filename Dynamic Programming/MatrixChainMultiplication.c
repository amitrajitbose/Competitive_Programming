/*
The classic matrix multiplication chain problem.
Solved using top-down dynamic programming (overlapping subproblems and optimal substructure)
Problem is easily available on Internet.
Author: Amitrajit Bose

A[i][j] * B[j][k] = C[i][k] ( i*j*k multiplication operations needed)

Recursive Tree Diagram: https://www.geeksforgeeks.org/wp-content/uploads/polyTriang.png

Recursion Base Case: Single matrix has zero operations to perform.
Recursive Formula: f(i,j)=min( f(i,k)+f(k+1,j)+1 )

*/

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
int topdowndp [100][100];
int MatrixChain(int m[],int i, int j){
	int k,temp;
	int ans=INT_MAX;
	if(i==j)
	{
		//BASE CASE
		topdowndp[i][j] = 0;
		return 0;
	}
	if(topdowndp[i][j]!=-1)
	{
		return topdowndp[i][j];
		//OVERLAPPING SUBPROBLEM
	}
	
	for(k=i;k<j;k++){
		temp=MatrixChain(m,i,k)+ MatrixChain(m,k+1,j)+m[i-1]*m[k]*m[j]; //COST OF COMPUTATION
		ans=(ans<temp)?ans:temp;
	}
	topdowndp[i][j]=ans;
	return ans;
}
int main()
{
	int n,i,j;
	int tmp;
	int mat[100]; //STORES MATRICES

	printf("ENTER NUMBER OF MATRICES: ");
	scanf("%d",&n);

	printf("ENTER ROWS & COLUMNS OF MATRIX 1: ");
	scanf("%d %d",&mat[0],&mat[1]);

	for(i=2;i<=n;i++){
		printf("ENTER ROWS & COLUMNS OF MATRIX %d: ",i);
		scanf("%d %d",&tmp,&mat[i]);
		if(tmp!=mat[i-1]){
			printf("INVALID INPUT !\n\n");
			return 0;
		}
	}

	n=n+1;
	//memset (tdp,-1,sizeof(tdp));
	for(i=1;i<n;i++){
		for(j=1;j<n;j++){
			topdowndp[i][j]=-1; //INITIALISE WITH -1
		}
	}
	printf("MINIMUM OPERATIONS: %d\n",MatrixChain(mat,1,n-1));
	/*
	//PRINT DP TABLE
	for(i=1;i<n;i++){
		for(j=1;j<n;j++){
			printf("%d\t",topdowndp[i][j]);
		}
		printf("\n");
	}
	*/
	return 0;
}