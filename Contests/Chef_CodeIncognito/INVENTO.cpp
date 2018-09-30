
/*
 * Author: Amitrajit Bose
 * Problem Link: 
 * Approach: 
 */
/*
THIS CODE IS LOGICALLY CORRECT
BUT WRONG ANSWER DUE TO LOG2()
SO BE CAREFUL
*/

#include <bits/stdc++.h>
#include <iostream>
#include <ctype.h>
#include <climits>
using namespace std;

typedef long long ll;

#define rep(m,n) for(ll i=m; i<(n); i++)
#define test ll t; cin >> t; while(t--)

int main()
{
test
{
	ll n;
	cin >> n;
	ll c=0;
	if(n==1)
		cout<<"1"<<endl;
	else if(n==2)
		cout<<"2"<<endl;
	else
	{
		c=floor(log2(n))+1;
		cout<<c<<endl;
	}
}
return 0;
}

