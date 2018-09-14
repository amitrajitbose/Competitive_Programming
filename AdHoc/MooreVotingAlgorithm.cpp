/*
 * Author: Amitrajit Bose
 * Problem Link: https://www.spoj.com/problems/MAJOR/ 
 * Approach: Moore's Voting Algorithm
 * Complexity : Time O(n) Space O(1)
 */

#include<bits/stdc++.h>
#include <iostream>
#include<ctype.h>
#include<climits>
using namespace std;
typedef long long ll;
#define rep(i,m,n) for(ll i=m; i<(n); i++)
#define test ll t; cin>>t; while(t--)
int main()
{
	test
	{
		ll n,i,j;
		cin >> n;
		ll arr[n]; 

		rep(i,0,n)
		{
			cin >> arr[i];
		}
		//Phase 1 : Choose a candidate - O(n)
		ll k = 0;
		ll count = 1; // candidate is present itself
		rep(i,1,n)
		{
			if(arr[k]==arr[i])
				count++;
			else
				count--;
			if(count==0)
			{
				k=i; // the element that nullified our current predicted candidate may be
				// a prospective candidate. Thus choose him.
				count=1;
			}
		}
		ll candidate = arr[k];
		//Phase 2 : Ensure that the candidate is indeed a majority element - O(n)
		count = 0;
		int flag = 0;
		rep(i,0,n)
		{
			if(arr[i]==candidate)
				count++;
			if(count>n/2)
			{
				flag=1;
				cout << "YES "<< candidate <<endl;
				break;
			}
		}
		if(flag == 0)
			cout << "NO" << endl;
	}
	return 0;
}
