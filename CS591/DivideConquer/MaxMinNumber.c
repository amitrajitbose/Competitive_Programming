#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int max,min; //globally declared 
void maxmin(int arr[], int l, int r)
{
	if(r-l==0)
	{
		max=arr[l];
		min=arr[l]; //this case will arise for odd length arrays
	}
	else if(r-l==1)
	{
		max=(arr[l]>=arr[r])?arr[l]:arr[r]; //for even length arrays
		min=(arr[l]<arr[r])?arr[l]:arr[r];
	}
	else
	{
		int m=floor((l+r)/2);
		maxmin(arr,l,m);
		int tmax=max; //max of first half
		int tmin=min; //min of first half
		maxmin(arr,m+1,r);
		max=(tmax>max)?tmax:max;
		min=(tmin<min)?tmin:min;
	}
}
int main()
{
	int n;
	int arr[]={4,1,7,4,9,3,3,7,8,6,2,6,0,5,1};
	n=sizeof(arr)/sizeof(arr[0]);

	maxmin(arr,0,n-1);
	printf("MAX: %d\nMIN: %d\n",max,min);
	return 0;
}