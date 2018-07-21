//Author: Riddhi Dutta
#include<bits/stdc++.h>
#include<cmath>
#include<climits>
#define test ll t; cin>>t; while(t--)
#define rep0(n) for(ll i=0;i<(n);i++)
#define rep1(n) for(ll i=1;i<=(n);i++)
using namespace std;
typedef long long ll;
int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    ll n,p;
    char ch;
    cin>>n>>ch>>p;
    ll *a = new ll[n];
    ll sum = 0;
    rep0(n)
    {
        cin>>a[i]>>ch;
        sum+=a[i];
    }
    ll dp[501][50][4];
    for(ll i=0;i<=500;i++)
        for(ll j=0;j<50;j++)
            for(ll k=0;k<=3;k++)
            {
                if(j==0 && k==0)
                    dp[i][j][k] = 1;
                else
                    dp[i][j][k] = 0;
            }
    for(ll i=1;i<=n;i++)
        for(ll j=0;j<p;j++)
            for(ll k=1;k<=3;k++)
            {
                dp[i][j][k] = dp[i-1][j][k];
                for(ll t=0;t<p;t++)
                    if( (t+a[i-1])%p==j )
                        dp[i][j][k] = (dp[i][j][k]+dp[i-1][t][k-1])%1009;
            }
    
    cout<<dp[n][0][3]<<endl; //here 3 is the cardinality
    return 0;
}
