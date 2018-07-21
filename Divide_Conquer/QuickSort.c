/*
Implementation of QuickSort algorithm
*/
#include <stdio.h>
#include <stdlib.h>
void swap(int *a,int *b){
	int t=*a;
	*a=*b;
	*b=t;
}
int Partition(int A[],int p, int r)