/*
Finding maximum and minimum number of an array 
using plain divide and conquer approach

Divide the array into two subarrays until we reach the smallest unit
that can be trivially conquer/calculated.

We cancuate the maximum and minimum of small arrays (size 1 or 2). then
compare it with larger subproblem, thus computing the final max and min.
*/
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
int max,min; //global declaration

void MaxMin(int A[],int i,int j);

int main(){
	int n,i,*arr;
	printf("Enter Size: ");
	scanf("%d",&n);
	arr=(int*)malloc(n*sizeof(int));
	for(i=0;i<n;i++){
		printf("Enter Value at %d: ",i+1);
		scanf("%d",&arr[i]);
	}
	MaxMin(arr,0,n-1);
	printf("Maximum= %d\nMinimum= %d\n",max,min);
	return 0;
}

void MaxMin(int A[],int i, int j){
	if(i==j){
		//array of length unity
		//conquer
		max=A[i];
		min=A[i];
	}
	else if(j-i==1){
		//array of length two
		//considering odd length arrays
		//conquer
		max=(A[i]>=A[j])?A[i]:A[j];
		min=(A[i]<A[j])?A[i]:A[j];
	}
	else{
		//divide
		int mid=floor((i+j)/2);
		MaxMin(A,i,mid);
		int max1=max;
		int min1=min;
		MaxMin(A,mid+1,j);
		if(max1>max)
			max=max1;
		if(min1<min)
			min=min1;
	}
}

/*
If you're running this code on linux GNU bash terminal, then
gcc filename.c will generate an error because floor exists in math.h
header file.
Error: undefined reference to 'floor'

We need to link it using the -lm flag.
Run this command to compile the program: gcc filename.c -lm -o a.out
Then normally run it using ./a.out

Here, a.out is the object that got created. We then execute it.
*/