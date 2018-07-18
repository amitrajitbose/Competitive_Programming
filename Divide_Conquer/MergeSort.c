/*
MERGE SORT
Author: Amitrajit Bose
****************
MERGE: Given two individually sorted list, this function merges the two
lists/arrays in sorted fashion. The total time complexity for this 
is O(n). The two separately sorted lists are A[p....q] and A[q+1....r]. Each element
is one by one compared and merged into the final array. This is the heart
of the algorithm.

Merge sort is the only out-of-place sorting algorithm that requires
extra space. The space complexity is O(n+logn)=O(n).

Purpose of infinity at the end (OPTIONAL): if one list is over, the other list
will get automatically copied to the merged array, by comparing each
element to infinity. Logically, infility is a very large number, i.e 
MAXINT type.

MERGESORT: Divide-and-Conquer algorithm. This basically divides the entire array
A[p...r] into two halves, A[p...q] and A[q+1...r]. Then they will finally get merged
after being sorted. MERGESORT works recursively. 

The recursion stack takes a space equivalent to O(ceil(logn) +1),
which is effectively O(log n). Thus total space complexity = 
O(n+logn)=O(n).
*/

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
void MERGE(int arr[],int p,int q, int r){
	int i,j,k;
	int n1 = q-p+2;
	int n2 = r-q+1;
	//temporary arrays with INT_MAX equivalent to infinity(logical)
	int L[n1], R[n2];
	for(i=0;i<n1-1;i++)
		L[i]=arr[p+i];
	L[n1-1]=INT_MAX;
	
	for(j=0;j<n2-1;j++)
		R[j]=arr[q+1+j];
	R[n2-1]=INT_MAX;
	
	//merge mechanism
	i=0;
	j=0;
	k=p;
	for(k=p;k<=r;k++)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
    }
}
void MERGESORT(int arr[],int p,int r){
	if(p<r){
		int q=floor((p+r)/2);
		//int q=floor((p+(r-p))/2);
		MERGESORT(arr,p,q);
		MERGESORT(arr,q+1,r);
		MERGE(arr,p,q,r);
	}
}
void printArray(int A[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}
int main(){
	int arr[]={19,17,16,12,11,13,14,10,9,6,7,2,1};
	int arr_size=sizeof(arr)/sizeof(arr[0]);
	printf("ORIGINAL ARRAY: ");
	printArray(arr,arr_size);
	MERGESORT(arr,0,arr_size-1);
	printf("SORTED ARRAY: ");
	printArray(arr,arr_size);
	return 0;
}