/* 
Binary Search
Data has to be stored in array.
Data has to be sorted.
Also known as Half Interval Search or Logarithmic Search.

1)Set L=0 and R=n-1
2)If L>R, search terminates unsuccessfully
3)Set m to the floor of (L+R)/2, as the middle element
4)If target=Array[m], then search done return m
5)If target>Array[m], L=m+1 and go to step 2
6)If target<Array[m], R=m-1 and go to step 2
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int binarySearch(int arr[],int left,int right,int target){
	while(left<=right){
		int m=floor((left+right)/2);
		if(arr[m]==target)
			return m;
		else if(arr[m]>target)
			right=m-1;
		else if(arr[m]<target)
			left=m+1;
	}
	return -1;
}
int main()
{
	int *arr;
	int n,i,target,status;
	printf("Enter Size: ");
	scanf("%d",&n);
	arr=(int*)malloc(n*sizeof(int));
	for(i=0;i<n;i++){
		printf("Enter Value: ");
		scanf("%d",&arr[i]);
	}
	printf("Enter Search Element: ");
	scanf("%d",&target);
	status=binarySearch(arr,0,n-1,target);
  
	if(status == -1)
		printf("Element Not Found");
	else
		printf("Element Present At Position %d",status+1);
	return 0;
}
/*
Time complexity : O(log n) [base 2]
Recurrence Relation: T(n)=T(n/2)+1, if n>1
					 T(n)=1, if n=1
*/