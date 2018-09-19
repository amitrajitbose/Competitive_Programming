#include<bits/stdc++.h>
#include <iostream>
#include<ctype.h>
#include<climits>
using namespace std;
typedef long long ll;
#define rep(i,m,n) for(ll i=m; i<(n); i++)
#define test ll t; cin>>t; while(t--)

void build(ll node, ll start, ll end, ll tree[], ll A[])
{
	if(start == end){
		tree[node]=A[start];
	}
	else{
		ll mid = (start+end)/2;
		build(2*node, start, mid, tree, A);
		build((2*node)+1, mid+1, end, tree, A);
		tree[node] = (tree[2*node]) | (tree[(2*node)+1]);
	}
}

ll query(ll node, ll start, ll end, ll l, ll r, ll tree[])
{
	if(r<start or l>end){
		return 0;
	}
	else if(l<=start and r>=end){
		return tree[node];
	}
	else{
		ll mid = (start+end)/2;
		ll sidea = query(2*node, start, mid, l, r, tree);
		ll sideb = query((2*node)+1, mid+1, end, l, r, tree);
		return (sidea | sideb);
	}
}

int main()
{
	ll n;
	cin >> n;
	ll arr[n+1];
	ll i;
	rep(i,1,n+1){
		cin >> arr[i]; //input
	}
	ll tree[(2*n)+10]; // extra just to be safe
	build(1, 1, n, tree, arr);
	
	ll counter = 0;
	for(ll x=1;x<=n;x++){
		for(ll y=x;y<=n;y++){
			ll bitandval = query(1,1,n,x,y,tree);
			//cout << bitandval << endl;
			counter += bitandval;
		}
	}
	cout <<counter <<endl;
	return 0;
}
