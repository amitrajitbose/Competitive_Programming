/*
 * Author: Amitrajit Bose
 * Problem Link:www.codechef.com/problems/CHBLLNS 
 * Approach: 
 */

#include <bits/stdc++.h>
#include <iostream>
#include <ctype.h>
#include <climits>
using namespace std;
typedef long long ll;
#define FOR(i,m,n) for(__typeof(n) i = m; i<(n); i++)
#define test ll t; cin >> t; while(t--)
int main()
{
test
{
	ll a[3];
	ll k;
	FOR(i,0,3)
	{
		cin >> a[i];
	}
	cin >> k;
	sort(a,a+3);
	ll c=0;
	if(k==1)
		c=1;
	else
	{
		if(a[0]>=k)
			c = k + 2*(k-1);
		else if(a[1]>=k)
			c = a[0] + k + (k-1);
		else if(a[2]>=k)
			c = a[0] + a[1] + k;
	}
	cout << c << endl;
}
return 0;
}

