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
      	cout << __gcd(one,two)%MOD << endl;
    }
    return 0;
}
