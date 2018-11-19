#include <stdio.h>
#include <stdlib.h>
#define N 4
int x[N];

int place(int k,int i)
{
	int j;
	for(j=0;j<k;j++)
	{
		if(x[j]==i || abs(x[j]-i)==abs(j-k) )
			return 0;
	}
	return 1;
}
int k=1;
void printer(int x[],int n)
{
	int i;
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
			x[k]=i;
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