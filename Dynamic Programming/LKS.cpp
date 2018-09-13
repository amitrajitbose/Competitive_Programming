/*
 * Author: Amitrajit Bose
 * Problem : SPOJ -> LKS 
 * Approach: Dynamic Programming & Memoization
 */

#include<bits/stdc++.h>
#include <iostream>
#include<ctype.h>
#include<climits>
using namespace std;
#define rep(m,n) for(ll i=m; i<(n); i++)
#define test ll t; cin>>t; while(t--)
#define MAX 501
struct obj{
	int val,wt;
};

int knapsack(int C, int n, obj items[], int dp[][MAX]){
	int res; //stores result
	if(dp[C][n]!=-1) //memoized previously, here is when dynamic programming saves your time
		return dp[C][n];
	if(n==0 or C==0) //no items to choose from, or bag size is zero, basically you can't pick anything
		res=0;
	else if(items[n].wt>C) //current item cannot be accomodated in knapsack
		res=knapsack(C,n-1,items,dp); //do not pick item, go for other items
	else
	{
		int t1 = knapsack(C,n-1,items,dp); //leave it, go for next item, state 0
		int t2 = knapsack(C-items[n].wt,n-1,items,dp)+items[n].val; //take it, reduce bag size, state 1
		res = max(t1, t2); //since I need to maximize the value 
	}
	dp[C][n] = res;
	return res;
}
int main()
{
	int n,bagmax,i;
	cin >> bagmax >> n; //total items and bagmax
	obj items[n+1];

	//items[0].val=0; initialisation for this does not matter, the first place is just a dummy value
	//items[0].wt=0; whenever we reach zero index, we return zero

	for(i=1;i<=n;i++){
		cin >> items[i].val >> items[i].wt;
	}
	int cache[bagmax+1][MAX]; //assuming number of items is less than MAX
	memset(cache, -1, sizeof(cache)); //initialise all values with -1

	int ans = knapsack(bagmax, n, items, cache); 
	cout << ans << endl;
	return 0;
}
