
/*
 * Author: Amitrajit Bose
 * Problem: Select the kth smallest element from an unsorted array without sorting it 
 * Approach: Randomized Select, Randomized Partition, Divide Conquer, Recursion
 */

#include <bits/stdc++.h>
#include <iostream>
#include <ctype.h>
#include <climits>

using namespace std;
typedef long long ll;
#define rep(m,n) for(i=m; i<(n); i++)
#define test ll t; cin>>t; while(t--)
int randPartition(int arr[], int a, int b); //signature declaration
int randSelect(int arr[], int p, int r, int k)
{
	// select kth smallest in arr[p..q]
	if(k>0 and k<=r-p+1)
	{
		if(p==r)
			return arr[p];// only one element in this side
		int q = randPartition(arr,p,r);
		if(q-p==k)
			return arr[q];// if position is same
		if(q > k)
			return randSelect(arr,p,q-1,k); // recurse to the left
		else
			return randSelect(arr,q+1,r,k-(q-p+1));
	}
	return INT_MAX;
}

void swap(int *a, int *b)
{
	int t = *a;
	*a = *b;
	*b = t;
}

int randPartition(int arr[], int l, int r)
{
	int x = arr[r];
	int i = l;//selecting a pivot
	for(int j=l;j<r;j++)
	{
		if(arr[j]<=x)
		{
			swap(&arr[i], &arr[j]);
			i++;
		}
	}
	swap(&arr[i], &arr[r]);
	return i;
}

int main()
{
	int arr[]={245,434,76,34,834,74,343,765,23,22,5,7343,65};
	int n = sizeof(arr)/sizeof(arr[0]);
	int median = floor(n/2);//considering n=odd, here 13
	cout << "MEDIAN USING ALGO: "<< randSelect(arr,0,n-1,median)<<endl;
	return 0;
}

