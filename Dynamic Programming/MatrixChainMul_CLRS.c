// Matrix Chain Multiplication
// Amitrajit Bose
// CLRS Sec-15.2 Page-370

#include <stdio.h>
#include <stdlib.h>
#define MAX 10
#define INT_MAX 999999 //theoretically infinite
int m[MAX][MAX];
int s[MAX][MAX];
int p[MAX];
void MatrixChainOrder(int p[],int lenp){
	int n=lenp-1;
	int i,j,k,l,q; //where l is the length of the chain
	for(i=1;i<=n;i++){
		m[i][i]=0;
	}
	for(l=2;l<=n;l++){
		for(i=1;i<=(n-l+1);i++){
			j=i+l-1;
			m[i][j]=INT_MAX;
			for(k=i;k<=(j-1);k++){
				q=m[i][k]+m[k+1][j]+(p[i-1]*p[k]*p[j]);
				if(q<m[i][j]){
					m[i][j]=q;
					s[i][j]=k;
				}
			}
		}
	}
}
void PrintParenthesis(int i, int j){
	int k;
	if(i==j){
		printf("A%d",i);
	}
	else{
		printf("(");
		k=s[i][j];
		PrintParenthesis(i,k);
		PrintParenthesis(k+1,j);
		printf(")");
	}
}
int main(){
	int i,j,n;
	printf("ENTER CHAIN SIZE: ");
	scanf("%d",&n);
	printf("ENTER CHAIN: ");
	for(i=0;i<n;i++){
		scanf("%d",&p[i]);
	}
	MatrixChainOrder(p,n);
	/*
	//Prints the m[][] table
	for(i=1;i<n;i++){
		for(j=1;j<n;j++){
			printf("%d ",m[i][j]);
		}
		printf("\n");
	}
	*/
	printf("MINIMUM OPERATIONS: %d\n",m[1][n-1]);
	/*
	//Prints the s[][] table
	for(i=1;i<n;i++){
		for(j=1;j<n;j++){
			printf("%d ",s[i][j]);
		}
		printf("\n");
	}*/
	printf("OPTIMAL PARENTHESIZATION: ");
	PrintParenthesis(1,n-1);
	printf("\n");

	return 0;
}
