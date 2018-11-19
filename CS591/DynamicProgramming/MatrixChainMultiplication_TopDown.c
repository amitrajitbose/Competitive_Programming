#include <stdio.h>
#include <stdlib.h>
#define MAX 10
#define INTMAX 999999

int m[MAX][MAX];
int s[MAX][MAX];

int mcm(int m[][MAX], int p[], int i, int j)
{
	if(m[i][j]<INTMAX)
		return m[i][j];
	if(i==j)
		m[i][j]=0;
	else
	{
		int k,q;
		for(k=i;k<j;k++)
		{
			q=mcm(m,p,i,k)+mcm(m,p,k+1,j)+(p[i-1]*p[k]*p[j]);
			if(q<m[i][j])
			{
				m[i][j]=q;
				s[i][j]=k;
			}
		}
	}
}
void PrintParenthesis(int i, int j){
	int k;
	if(i==j){
		printf(" A%d ",i);
	}
	else{
		printf("(");
		k=s[i][j];
		PrintParenthesis(i,k);
		PrintParenthesis(k+1,j);
		printf(")");
	}
}
int main()
{
	int i,j;
	int n=4;
	int p[]={1,2,3,4};
	for(i=0;i<=n;i++){
		for(j=0;j<=n;j++){
			m[i][j]=INTMAX;
		}
	}
	mcm(m,p,1,n);
  printf("MINIMUM OPERATIONS: %d\n",m[1][n-1]);
	printf("OPTIMAL PARENTHESIZATION: ");
	PrintParenthesis(1,n-1);
	printf("\n");
	return 0;
}