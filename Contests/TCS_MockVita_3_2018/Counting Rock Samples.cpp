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
    ll s,r;
    cin>>s>>r;
    ll *samples = new ll[s];
    ll freq[1001] = {0};
    rep0(s)
    {
        cin>>samples[i];
        freq[samples[i]]++;
    }
    ll preFeqSamples[1001];
    preFeqSamples[0] = 0;
    for(ll i=1;i<=1000;i++)
        preFeqSamples[i] = preFeqSamples[i-1] + freq[i];
        
    while(r--)
    {
        ll l,u; 
        cin>>l>>u;
        cout<<preFeqSamples[u] - preFeqSamples[l-1]<<endl;
    }
    return 0;
}