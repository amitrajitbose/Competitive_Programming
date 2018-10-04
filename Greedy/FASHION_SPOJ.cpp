/*
Author : @amitrajitbose
Problem : SPOJ FASHION
*/

#include <bits/stdc++.h>
#include <iostream>
using namespace std;
typedef long long ll;
#define FOR(i,m,n) for(__typeof(n) i = m; i<(n); i++)

int main()
{
	ll t;
  cin >> t;
	while(t--)
	{
		ll n, *m, *w;
		cin >> n;
		m = new ll[n];
		w = new ll[n];
		FOR(i,0,n)
		{
			cin >> m[i];
		}
		sort(m,m+n);
		FOR(i,0,n)
		{
			cin >> w[i];
		}
		sort(w,w+n);
		ll summ=0;
		FOR(i,0,n)
		{
			summ += (m[i]*w[i]);
		}
    delete [] m;
    delete [] w;
		cout << summ << endl;
	}
	return 0;
}
