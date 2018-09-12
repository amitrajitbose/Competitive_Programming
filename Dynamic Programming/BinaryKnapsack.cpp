
/*
 * Author: Amitrajit Bose
 * Problem : 0/1 Knapsack Problem 
 * Approach: Dynamic Programming & Memoization
 * Resrc : https://youtu.be/xOlhR_2QCXY , https://youtu.be/8LusJS5-AGo ,
 */

#include<bits/stdc++.h>
#include <iostream>
#include<ctype.h>
#include<climits>
using namespace std;

typedef long long ll;
#define rep(m,n) for(ll i=m; i<(n); i++)
#define test ll t; cin>>t; while(t--)
#define MAX 1000
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
	cin >> n; //total items
	obj items[n+1];

	//items[0].val=0; initialisation for this does not matter, the first place is just a dummy value
	//items[0].wt=0; whenever we reach zero index, we return zero

	for(i=1;i<=n;i++){
		cin >> items[i].val >> items[i].wt;
	}

	cin >> bagmax;
	int cache[bagmax+1][MAX]; //assuming number of items is less than MAX
	memset(cache, -1, sizeof(cache)); //initialise all values with -1

	int ans = knapsack(bagmax, n, items, cache); 
	cout << ans << endl;
	
	return 0;
}


/*
4
1 1
4 3
5 4
7 5
7

OUT: 9

TABLE WOULD LOOK LIKE:
\n-0-1-2-3-4
c--
0--0-0-0-0-0
1--0-1-1-1-1
2--0-1-1-1-1
3--0-1-4-4-4
4--0-1-5-5-5
5--0-1-5-6-7
6--0-1-5-6-8
7--0-1-5-9-9 <--ANSWER

*/