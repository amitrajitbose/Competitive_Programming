#include <stdio.h>
#include <stdlib.h>
void swap(int *a, int *b)
{
	int t=*a;
	*a=*b;
	*b=t;
}
int partition(int arr[], int p, int r)
{
	int pivot=arr[r];
	int pIndex=p;
	int i;
	for(i=p;i<r;i++)
	{
		if(arr[i]<=pivot)
		{
			swap(&arr[i],&arr[pIndex]);
			pIndex++;
		}
	}
	swap(&arr[pIndex],&arr[pivot]);
	return(pIndex);
}
void quicksort(int arr[],int p, int r)
{
	if(p<r)
	{
		int q=partition(arr,p,r);
		quicksort(arr,p,q-1);
		quicksort(arr,q+1,r);
	}
}
int main()
{
	int ar[]={5,3,7,1,9,4,8,2};
	int n=sizeof(ar)/sizeof(ar[0]);
	int i;
	quicksort(ar,0,n-1);
	for(i=0;i<n;i++){
		printf("%d ",ar[i]);
	}
	printf("\n");
	return 0;
}