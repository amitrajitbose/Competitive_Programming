/*
 * Author: Amitrajit Bose
 * Problem Link: https://www.byte-by-byte.com/matrixproduct/
 * Approach: Dynamic Programming
 * 
 * Given a matrix, find the path from top left to bottom right with the greatest product by moving only down and right.
 */

#include <bits/stdc++.h>
#include <iostream>
#include <ctype.h>
#include <climits>
using namespace std;
typedef long long ll;
#define rep(m,n) for(ll i=m; i<(n); i++)
#define test ll t; cin>>t; while(t--)
#define N 100

int mymax(int a, int b, int c, int d){
    return max(a,max(b,max(c,d)));
}

int mymin(int a, int b, int c, int d){
    return min(a,min(b,min(c,d)));
}

int tour(int A[N][N],int r,int c)
{
	int i,j;
	int dpmax[r][c]; //stores maximum
	int dpmin[r][c]; //same as above, store minimum because there can be situations of negative values
	dpmax[0][0]=A[0][0];
	dpmin[0][0]=A[0][0];
	// precomputing the first row
	for(j=1;j<c;j++){
		dpmax[0][j]=dpmax[0][j-1]*A[0][j];
		dpmin[0][j]=dpmin[0][j-1]*A[0][j];
	}
	// precomputing the first column
	for(i=1;i<r;i++){
		dpmax[i][0]=dpmax[i-1][0]*A[i][0];
		dpmin[i][0]=dpmin[i-1][0]*A[i][0];
	}
	// now iteratively check and store
	for(i=1;i<r;i++){
		for(j=1;j<c;j++){
			dpmax[i][j]=mymax(dpmax[i][j-1]*A[i][j], dpmax[i-1][j]*A[i][j], dpmin[i][j-1]*A[i][j], dpmin[i-1][j]*A[i][j]);
			dpmin[i][j]=mymin(dpmax[i][j-1]*A[i][j], dpmax[i-1][j]*A[i][j], dpmin[i][j-1]*A[i][j], dpmin[i-1][j]*A[i][j]);
		}
	}
	return max(dpmax[r-1][c-1], dpmin[r-1][c-1]);
}

int main()
{
	int m,n;
	cin >> m >> n;
	int i,j;
	int A[N][N];
	for(i=0;i<m;i++){
		for(j=0;j<n;j++){
			cin >> A[i][j];
		}
	}
	int maxPathCost = tour(A,m,n);
	cout << maxPathCost << endl;
	return 0;
}
/*
INPUT: 
3 3
-1 2 3
4 5 -6
7 8 9

OUTPUT:
1080

INPUT:
3 3
1 2 3
4 5 6
7 8 9

OUTPUT:
2016
*/