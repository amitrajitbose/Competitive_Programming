

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

int main()
{
	test
	{
		ll i, n;
		cin >> n;

		int *arr = new int[n];
		ll ones=0;
		ll twos=0;
		
		rep(i,0,n)
		{
			cin >> arr[i];
			if(arr[i]==1)
				ones+=1;
			else
				twos+=1;
		}
		// if all ones or all twos
		if(twos==0 or ones==0)
			cout << n << endl;
		else
		{
			ll sum=accumulate(arr,arr+n,0);
			if(arr[0]==2 and arr[n-1]==2)
				cout << sum-1 << endl;
			else
				cout << sum << endl; // only because digits can be 1 or 2
		}
		delete [] arr;
		arr = NULL;
	}
	return 0;
}
