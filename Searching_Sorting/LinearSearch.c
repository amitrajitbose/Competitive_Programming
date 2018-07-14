/*
Linear Search Algorithm
-----------------------
Works both on sorted and unsorted data.

Algorithm:
1) Set i to 0
2) If L[i]=T, the search terminates and return i
3) Increment i by unity
4) If i<n, go to step (2) otherwise search unsuccesful

-----------------------
Author: Amitrajit Bose
*/
#include <stdio.h>
#include <stdlib.h>
int linearSearch(int *arr,int size,int target){
	int i;
	for(int i=0;i<size;i++){
		if(arr[i]-target==0)
			return i;
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
	status=linearSearch(arr,n,target);
  
	if(status == -1)
		printf("Element Not Found");
	else
		printf("Element Present At Position %d",status+1);
	return 0;
}

-----------------------
/*
Time Complexity: O(n)
Recurrence Relation: T(n)=T(n-1)+1, T(1)=1