
/*
 * Author: Amitrajit Bose
 * Problem Link: Codechef Cats And Dogs 
 * Approach: 
 */

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define test ll t; cin >> t; while(t--)
int main()
{
	test
	{
		ll c,d,l;
		cin >> c >> d >> l;
		if((l-(4*d))<0 or l%4!=0)
			cout << "no" << endl;
		else
		{
			ll maxim=(c+d)*4; //everyone stands on their own leg
			ll minim=(d*4)+max((ll)0,((c-(2*d))*4));
			if(minim<=l and l<=maxim)
				cout << "yes" << endl;
			else
				cout << "no" << endl;
		}
	}
	return 0;
}
