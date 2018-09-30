
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
		int n;
		cin >> n; 
		ll cnt=0;
		ll i,x;
		int *marker = new int[n+1];
		
		fill(marker, marker+n+1, 0);
		//memset(marker, 0, sizeof(marker));

		rep(i,1,n+1){
			cin >> x;
			if(x>n or marker[x]==1)
				cnt++;
			else
				marker[x]=1;
		}
		cout << cnt << endl;
		delete [] marker;
		marker=NULL;
	}
	return 0;
}
