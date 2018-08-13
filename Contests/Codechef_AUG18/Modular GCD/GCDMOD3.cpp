//Problem: https://www.codechef.com/AUG18B/problems/GCDMOD

//CLEARS SUBTASK 1 ONLY - PARTIAL CORRECT

#include <bits/stdc++.h>
#include <cmath>
#include <climits>
#define test int t; cin>>t; while(t--)
#define rep0(n) for(ll i=0;i<(n);i++)
#define rep1(n) for(ll i=1;i<=(n);i++)
using namespace std;

#define MOD 1000000007

typedef long long ll;
ll fastxp(ll base,ll exp,ll mod)
{
  ll res = 1;
  while(exp>0)
  {
    if(exp%2==1)
      res = (res*base)%mod;
    exp/=2;
    base=(base*base)%mod;
  }
  return res;
}

// Function for extended Euclidean Algorithm
ll gcdExtended(ll a, ll b, ll *x, ll *y)
{
  // Base Case
  if (a == 0)
  {
    *x = 0;
    *y = 1;
    return b;
  }

  ll x1, y1; // To store results of recursive call
  ll gcd = gcdExtended(b%a, a, &x1, &y1);

  // Update x and y using results of recursive
  // call
  *x = y1 - (b/a) * x1;
  *y = x1;

  return gcd;
}

int main()
{
    /*ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);*/
    test
    {
        ll a,b,n,x,y;
      	cin>>a>>b>>n;
      	ll two = (abs(a-b)) ;
      	ll one = (fastxp(a,n,MOD) + fastxp(b,n,MOD)) ;
      	//cout<<one<<" "<<two<<endl; //DEBUG LINE
      	cout << gcdExtended(one, two, &x, &y)%MOD << endl;
    }
    return 0;
}
