
/*
 * Author: Amitrajit Bose
 * Problem Link: https://www.byte-by-byte.com/matrixproduct/
 * Approach: Dynamic Programming
 */

#include <bits/stdc++.h>
#include <iostream>
#include <ctype.h>
#include <climits>
using namespace std;
typedef long long ll;
#define rep(m,n) for(ll i=m; i<(n); i++)
#define test ll t; cin>>t; while(t--)
#define N 50
int mmax(int a, int b, int c)
{
	return max(a, max(b,c));
}
int tour(int A[N][N],int r,int c)
{
	int i,j;
	int dp[r][c];
	dp[0][0]=A[0][0];
	// precomputing the first row
	for(j=1;j<c;j++){
		dp[0][j]=dp[0][j-1]*A[0][j];
	}
	// precomputing the first column
	for(i=1;i<r;i++){
		dp[i][0]=dp[i-1][0]*A[i][0];
	}
	// now iteratively check and store
	for(i=1;i<r;i++){
		for(j=1;j<c;j++){
			dp[i][j]=max(dp[i][j-1],dp[i-1][j])*A[i][j];
		}
	}
	return dp[r-1][c-1];
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

