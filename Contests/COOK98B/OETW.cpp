
/*
 * Author: Amitrajit Bose
 * Problem Link: 
 * Approach: 
 */

#include <bits/stdc++.h>
#include <iostream>
#include <ctype.h>
#include <climits>
using namespace std;
typedef long long ll;
#define rep(i,m,n) for(i = m; i < (n); i++)
#define test ll t; cin >> t; while(t--)

//arrayPrinter
void print(int arr[], int n){
	ll i;
	rep(i,0,n){
		cout<<arr[i]<<" ";
	}
	cout<<endl;
}

int main()
{
	test
	{
		ll i, n;
		ll ps=0;
		ll s=0;
		cin >> n;
		int *arr = new int[n];
		int *checksum = new int[(2*n)+1];
		fill(checksum, checksum+(2*n)+1, 0);
		//forward addition check
		rep(i,0,n){
			cin>>s;
			arr[i] = s;
			ps=ps+s;
			if(checksum[s]!=1)
				checksum[s]=1;
			if(checksum[ps]!=1)
				checksum[ps]=1;
		}
		//backward deduction check
		rep(i,0,n){
			ps=ps-arr[i];
			if(checksum[ps]!=1)
				checksum[ps]=1;
		}
		checksum[0]=0;
		cout<<accumulate(checksum, checksum+(2*n)+1, 0)<<endl;
		delete [] checksum;
		delete [] arr;
	}
	return 0;
}

