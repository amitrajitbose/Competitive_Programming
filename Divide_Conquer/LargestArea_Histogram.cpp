	
/*
 * Author: Amitrajit Bose
 * Problem Link: https://www.spoj.com/problems/HISTOGRA/ 
 * Approach: 
We can use Divide and Conquer to solve this in O(nLogn) time. 
The idea is to find the minimum value in the given array. 
Once we have index of the minimum value, the max area is maximum of 
following three values.
a) Maximum area in left side of minimum value (Not including the min value)
b) Maximum area in right side of minimum value (Not including the min value)
c) Number of bars multiplied by minimum value.
The areas in left and right of minimum value bar can be calculated recursively. 
If we use linear search to find the minimum value, then the worst case time 
complexity of this algorithm becomes O(n^2).This is why we make use of segment tree and 
RMaxQ algorithm.
 */

#include<bits/stdc++.h>
#include<ctype.h>
#include<climits>
using namespace std;
typedef long long ll;

// A utility function to get minimum of two numbers in hist[] 
int minVal(int *hist, int i, int j) 
{ 
    if (i == -1) return j; 
    if (j == -1) return i; 
    return (hist[i] < hist[j])? i : j; 
} 
int getMid(int s, int e) 
{   
	return s + (e -s)/2;
} 

// build the binary tree - O(N)
void build(int node, int start, int end, int tree[], int A[])
{
    if(start == end){
        tree[node]=A[start];
    }
    else{
        int mid = (start+end)/2;
        build(2*node, start, mid, tree, A);
        build((2*node)+1, mid+1, end, tree, A);
        tree[node] = min(tree[2*node], tree[(2*node)+1]);
    }
}

int query(int node, int start, int end, int l, int r, int tree[])
{
    if(r<start or l>end){
        return -1;
    }
    else if(l<=start and r>=end){
        return tree[node];
    }
    else{
        int mid = (start+end)/2;
        int sidea = query(2*node, start, mid, l, r, tree);
        int sideb = query((2*node)+1, mid+1, end, l, r, tree);
        return min(sidea,sideb);
    }
}

int trimax(int a, int b, int c){
	return max(a,max(b,c));
}

int getMaxAreaRect(int hist[], int st[], int n, int l, int r)
{
	if(l>r) return -99999;
	if(l==r) return hist[l];
	int m = query(1,1,n,l,r,st);

	return trimax(getMaxAreaRect(hist,st,n,l,m-1), getMaxAreaRect(hist,st,n,m+1,r),((r-l+1)*(hist[m])));
}

int getMaxArea(int hist[], int n)
{
	//build tree
	int maxsize = 2*(int)pow(2,((int)ceil(log2(n)))) -1;
	int st[maxsize];
	build(1,1,n,st,hist);
	return getMaxAreaRect(hist, st, n, 1, n);
}
	
int main()
{
	int n;
	cin >> n; //first n
	while(n!=0)
	{
		int arr[n+1];
		for(int i=1;i<=n;i++)
			cin >> arr[i];
		// inputs taken
		cout << getMaxArea(arr, n) << endl;
		cin >> n; //next n
	}
	return 0;
}
