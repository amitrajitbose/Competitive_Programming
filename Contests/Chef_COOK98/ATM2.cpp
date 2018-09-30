
/*
 * Author: Amitrajit Bose
 * Problem Link: 
 * Approach: 
 */

#include<bits/stdc++.h>
#include <iostream>
#include<ctype.h>
#include<climits>
using namespace std;
typedef long long ll;
#define rep(m,n) for(i=m; i<(n); i++)
#define test ll t; cin>>t; while(t--)
int main()
{
test
{
	ll n,k,x;
	cin >> n >> k;
	//cout << n << " " << k <<endl;
	int gets[n];
	memset(gets,0,sizeof(gets));
	for(ll i=0;i<n;i++)
	{
		cin >> x;
		if(x<=k){
			k-=x;
			gets[i]=1; //marked
		}
	}
	for(ll i=0;i<n;i++)
	{
		cout << gets[i];
	}
	cout<<endl;
}
return 0;
}
