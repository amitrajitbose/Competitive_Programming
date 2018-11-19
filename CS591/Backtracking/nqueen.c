#include <stdio.h>
#include <stdlib.h>
#define N 4
int x[N];

int place(int k,int i)
{
	// this function checks if placing a queen at i is possible
	int j;
	for(j=0;j<k;j++)
	{
		//checks if any other queen previously is present is the same column
		//then also check if it is present on the diagonal
		if(x[j]==i || abs(x[j]-i)==abs(j-k) )
			return 0;
	}
	return 1;
}

void printer(int x[],int n)
{
	int i;
  	static int kc=1;
  	printf("Sol-%d  ",k++);
	for(i=0;i<n;i++)
	{
		printf("%d ",x[i]);
	}
	printf("\n");
}
void nqueen(int k,int n)
{
	int i;
	for(i=0;i<n;i++)
	{
		if(place(k,i))
		{
			//if placeable then place
			x[k]=i;
			//check if any more k is possible or not, if not then print that combination
			//k is the number if queens placed
			//if more queens can be placed then recurse with k=k+1 
			if(k==n-1)
				printer(x,N);
			else
				nqueen(k+1,n);
		}
	}
}

int main()
{
  nqueen(0,N);
  return 0;
}