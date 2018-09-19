
/*
 * Author: Amitrajit Bose
 * Problem Link: https://www.codechef.com/SEPT18B/problems/ANDSQR 
 * Approach : 
 */

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
		tree[node] = (tree[2*node]) & (tree[(2*node)+1]);
	}
}

ll query(ll node, ll start, ll end, ll l, ll r, ll tree[])
{
	if(r<start or l>end){
		return (pow(2,31))-1;
	}
	else if(l<=start and r>=end){
		return tree[node];
	}
	else{
		ll mid = (start+end)/2;
		ll sidea = query(2*node, start, mid, l, r, tree);
		ll sideb = query((2*node)+1, mid+1, end, l, r, tree);
		return (sidea & sideb);
	}
}
bool isPerfectSquare(ll x) 
{   
  // Find floating poll value of  
  double sr = sqrt(x); 
  // If square root is an integer 
  return ((sr - floor(sr)) == 0); 
} 

int main()
{
	test{
		ll n,q;
		cin >> n >> q;
		ll arr[n+1];
		ll i;
		rep(i,1,n+1){
			cin >> arr[i]; //input
		}
		ll tree[(2*n)]; // extra just to be safe
		build(1, 1, n, tree, arr);
		/*for(i=1;i<(2*n);i++)
			cout << tree[i] << ",";
		cout<<endl;
		cout << query(1,1,n,1,1,tree) << endl;
		cout << query(1,1,n,1,2,tree) << endl;
		cout << query(1,1,n,1,3,tree) << endl;
		cout << query(1,1,n,2,2,tree) << endl;
		cout << query(1,1,n,2,3,tree) << endl;
		cout << query(1,1,n,3,3,tree) << endl;
		*/
		
		ll left,right;
		for(i=0;i<q;i++){
			cin >> left >> right;
			ll counter = 0;
			for(ll x=left;x<=right;x++){
				for(ll y=x;y<=right;y++){
					ll bitandval = query(1,1,n,x,y,tree);
					//cout << bitandval << endl;
					if(isPerfectSquare(bitandval)){
						counter++;
					}
				}
			}
			cout <<counter <<endl;
		}
		
	}
	return 0;
}
