#include <stdio.h>
#include <stdlib.h>
void merge(int arr[], int p, int q, int r)
{
	int lsize=q-p+1+1;
	int rsize=r-(q+1)+1+1;
	int left[lsize], right[rsize];
	int i,j,k;
	//initialising left array
	for(i=0;i<lsize-1;i++)
		left[i]=arr[p+i];
	left[lsize-1]=9999;
	
	//initialising right array
	for(i=0;i<rsize-1;i++)
		right[i]=arr[q+1+i];
	right[rsize-1]=9999;
	
	//merging arrays
	i=0,j=0,k=p;
	for(k=p;k<=r;k++)
	{
		if(left[i]<=right[j])
		{
			arr[k]=left[i];
			i++;
		}
		else
		{
			arr[k]=right[j];
			j++;
		}
	}
}
void mergesort(int arr[], int p, int r)
{
	if(p<r)
	{
		int q=(int)((p+r)/2);
		mergesort(arr,p,q);
		mergesort(arr,q+1,r);
		merge(arr,p,q,r);
	}
}
int main(){
	int arr[]={19,17,16,12,11,13,14,10,9,6,7,2,1};
	int n=sizeof(arr)/sizeof(arr[0]);
	int i;
	mergesort(arr,0,n-1);
	printf("SORTED ARRAY: ");
	for(i=0;i<n;i++)
		printf("%d ",arr[i]);
	printf("\n");
	return 0;
}