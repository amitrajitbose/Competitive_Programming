
/*
 * Author: Amitrajit Bose
 * Problem : Making Coin Change 
 * Approach: Bottom Up Dynamic Programming
 */

#include<bits/stdc++.h>
#include <iostream>
#include<ctype.h>
#include<climits>

using namespace std;
typedef long long ll;
#define rep(m,n) for(ll i=m; i<(n); i++)
#define test ll t; cin>>t; while(t--)

ll makeChange(ll arr[], ll len, ll amt)
{
	ll cache[amt+1];
	cache[0]=0; // we need zero coins to make change of zero
	for(ll i=1; i<=amt;i++)
	{
		ll minCoin = INT_MAX;
		// now check for every denomination we have, then keep minimum
		for(ll j=0; j<len; j++)
		{
			if(i-arr[j] >= 0)
			{
				ll currCoin = cache[(i-arr[j])]+1; //that coin (i-arr[j]) and the number of coins required to get that coin
				minCoin = min(minCoin, currCoin);
			}
		}
		cache[i] = minCoin;
	}
	/*
	//CACHE TABLE
	for(ll i=0;i<=amt;i++)
		cout<<cache[i]<<" ";
	cout<<endl;
	*/
	return cache[amt];
}
int main()
{
	ll n; // number of currency coins
	cin >> n;
	ll arr[n];
	rep(0,n){
		cin >> arr[i];
	}
	ll amt; // amount to be made
	cin >> amt;
	ll coinsReq = makeChange(arr,n,amt);
	cout << coinsReq << endl;
	return 0;
}

/*
3
1 6 10
12

OUT: 2
*/