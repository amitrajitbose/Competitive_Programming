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


// Stein's Algorithm
ll gcd(ll a, ll b)
{
  if (a == b)
    return a;

  // GCD(0, b) == b; GCD(a, 0) == a,
  // GCD(0, 0) == 0
  if (a == 0)
    return b;
  if (b == 0)
    return a;

  // look for factors of 2
  if (~a & 1) // a is even
  {
    if (b & 1) // b is odd
      return gcd(a >> 1, b);
    else // both a and b are even
      return gcd(a >> 1, b >> 1) << 1;
  }

  if (~b & 1) // a is odd, b is even
    return gcd(a, b >> 1);

  // reduce larger number
  if (a > b)
    return gcd((a - b) >> 1, b);

  return gcd((b - a) >> 1, a);
}


int main()
{
    /*ios_base::sync_with_stdio(false); 
    cin.tie(NULL); 
    cout.tie(NULL);*/
    test
    {
        ll a,b,n;
      	cin>>a>>b>>n;
      	ll two = (abs(a-b)) ;
      	ll one = (fastxp(a,n,MOD) + fastxp(b,n,MOD)) ;
      	//cout<<one<<" "<<two<<endl; //DEBUG LINE
      	cout << gcd(one,two)%MOD << endl;
    }
    return 0;
}
