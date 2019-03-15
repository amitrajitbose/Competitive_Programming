
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
#define test ll t; cin >> t; while(t--)
int main()
{
test
{
	ll i,n;
	ll ps=0;
	ll ng=0;
	cin >> n;
	ll A[n];
	FOR(i,0,n)
	{
		cin >> A[i];
		if(A[i]>=0)
			ps++;
		else
			ng++;
	}
	if(ps==n or ng==n)
		cout << n << " " << n << endl;
	else
		cout << max(ps,ng) << " " << min(ps,ng) << endl;
}
return 0;
}
