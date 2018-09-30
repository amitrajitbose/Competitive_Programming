// @amitrajitbose
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define MOD 1000003

int main()
{
    ll fact[MOD];
    fact[0]=1;
    fact[1]=1;
    fact[2]=2;
    for(ll i=3;i<MOD;i++)
        fact[i]=(i*fact[i-1])%MOD;
    ll t;
    cin >> t;
    while(t--)
    {
        ll n,x;
        cin >> n >> x;
        if(n<MOD){
            cout << (x*fact[n])%MOD << endl;
        }
        else{
            cout << "0" << endl;
        }
    }
    return 0;
}
