#include <stdio.h>
#include <stdlib.h>

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a > *(int*)b );
}
void binarysearch(int arr[], int n, int k, int left, int right)
{
	int mid=(int)((left+right)/2);
	if(right<left)
	{
		printf("ELEMENT NOT FOUND\n");
		return;
	}
	if(arr[mid]==k)
	{
		printf("ELEMENT FOUND AT INDEX %d\n",mid+1);
		return;
	}
	if(arr[mid]<k)
		binarysearch(arr,n,k,mid+1,right);
	if(arr[mid]>k)
		binarysearch(arr,n,k,left,mid-1);
}
int main()
{
	int i,n,searchkey;
	int arr[]={4,2,6,1,8,5,3};
	n=sizeof(arr)/sizeof(arr[0]);
	searchkey=3;
	qsort(arr, n, sizeof(int), cmpfunc);
	binarysearch(arr,n,searchkey,0,n-1);
	return 0;
}
