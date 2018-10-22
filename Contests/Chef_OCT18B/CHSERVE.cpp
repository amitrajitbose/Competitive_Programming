
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
#define FOR(i,m,n) for(__typeof(n) i = m; i<(n); i++)
#define test ll t; cin >> t; while(t--)
int main()
{
	test
	{
		ll p1,p2,k;
		cin >> p1 >> p2 >> k ;
		if(((p1+p2)/k)%2 == 0)
			cout << "CHEF" << endl;
		else
			cout << "COOK" << endl;
	}
	return 0;
}
