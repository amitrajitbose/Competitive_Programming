/*
Implementation of QuickSort algorithm.
The way that quicksort uses divide-and-conquer is a little different 
from how merge sort does. In merge sort, the divide step does hardly 
anything, and all the real work happens in the combine step. 
Quicksort is the opposite: all the real work happens in the divide step. 
In fact, the combine step in quicksort does absolutely nothing.

More: https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/overview-of-quicksort

*/
#include <stdio.h>
#include <stdlib.h>
void swap(int *a,int *b){
	int t=*a;
	*a=*b;
	*b=t;
}
int Partition(int A[],int p, int r){
	int pivot=A[r];
	int i=p-1;
	int tmp,j;
	for(j=p;j<r;j++){
		if(A[j]<=pivot)
		{
			i++;
			swap(&A[i],&A[j]);
		}
	}
	swap(&A[i+1],&A[j]);
	return (i+1);
}
void quickSort(int A[],int p, int r){
	if(p<r){
		int q=Partition(A,p,r);
		//element at q is already sorted
		//recursively run the algorithm on the left and right subarray
		quickSort(A,p,q-1);
		quickSort(A,q+1,r);
	}
}
//Taking inputs from command line, just for fun ;)
int main(int argc, char const *argv[])
{
	int n = argc-1;
	printf("ARRAY SIZE: %d\n",n);
	int *arr = (int *) malloc (n * sizeof(int));
	//int arr[100];
	int i;

	//Scanning arguments
	for(i=1;i<=n;i++){
		sscanf(argv[i], "%d", &arr[i-1]);
		//arr[i-1]=(argv[i]);
	}

	printf("OLD ARRAY: ");
	for(i=0;i<n;i++){
		printf("%d ",arr[i]);
	}
	printf("\n");

	quickSort(arr,0,n-1);
	printf("NEW ARRAY: ");
	for(i=0;i<n;i++){
		printf("%d ",arr[i]);
	}
	printf("\n");
	return 0;
}

/*
OUTPUT:
./a.out 632 3278 326 328 7 736 8 9 56 28 89 2 9 0 9 7 5 7 8 9 12
ARRAY SIZE: 21
OLD ARRAY: 632 3278 326 328 7 736 8 9 56 28 89 2 9 0 9 7 5 7 8 9 12 
NEW ARRAY: 0 2 5 7 7 7 8 8 9 9 9 9 12 28 56 89 326 328 632 736 3278
*/

/*
https://www.khanacademy.org/computing/computer-science/algorithms
*/