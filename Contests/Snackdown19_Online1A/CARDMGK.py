
/*
 * Author: Amitrajit Bose
 */

#include <bits/stdc++.h>
#include <iostream>
#include <ctype.h>
#include <climits>
using namespace std;
typedef long long ll;
#define FOR(i,m,n) for(__typeof(n) i = m; i<(n); i++)
#define test int t; cin >> t; while(t--)
int main()
{
	test
	{
		ll n;
		cin >> n;
		ll *arr = new ll[n];
		int flag=0;
		FOR(i,0,n)
		{
			cin >> arr[i];
			if(i>0)
			{
				if(arr[i]<arr[i-1])
				{
					flag++;
				}
			}
		}
		if(arr[0]<arr[n-1])
		{
			flag++;
		}
		delete [] arr;
		arr = NULL;
		if(flag>=2)
			cout<<"NO"<<endl;
		else
			cout<<"YES"<<endl;
	}
	return 0;
}

