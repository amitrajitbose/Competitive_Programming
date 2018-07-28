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
    ll digits[9];
    ll freq[10] = {0};
    char ch;
    for(ll i=0;i<9;i++)
    {
        cin>>digits[i]>>ch;
        freq[digits[i]]++;
    }    
    //explicity check
    bool loop = false;
    if(freq[2]>=1 && freq[4]>=1 && freq[0]>=4)
    {
        cout<<"24:00:00";
        loop = true;
    }
    else
    {
        for(ll hr=23;hr>=1;hr--)
            for(ll mins=59;mins>=0;mins--)
                for(ll sec=59;sec>=0;sec--)
                {
                    //
                    bool hobe = true;
                    ll freqtemp[10]={0};
                    if(hr<10) freqtemp[0]++;
                    if(mins<10) freqtemp[0]++;
                    if(sec<10) freqtemp[0]++;
                    ll thr = hr; ll tmin = mins; ll tsec = sec;
                    while(thr>0) { freqtemp[(thr%10)]++; thr/=10;} 
                    while(tmin>0) { freqtemp[(tmin%10)]++; tmin/=10;} 
                    while(tsec>0) { freqtemp[(tsec%10)]++; tsec/=10;}
                    for(ll i=0;i<10;i++)
                        if(freqtemp[i]>freq[i]){ hobe=false;break;}
                    if(hobe)
                    {
                        loop = true;
                        if(hr<10) cout<<"0";  cout<<hr<<":";
                        if(mins<10) cout<<"0"; cout<<mins<<":";
                        if(sec<10) cout<<"0"; cout<<sec;
                        goto label;
                    }
                }
    }
    if(!loop)
    {
        for(ll mins=59;mins>=0;mins--)
        {
            for(ll sec=59;sec>=1;sec--)
            {
                bool hobe = true;
                ll freqtemp[10]={0};
                freqtemp[0] = 2;
                if(mins<10) freqtemp[0]++;
                if(sec<10) freqtemp[0]++;
                ll tmin = mins; ll tsec = sec;
                while(tmin>0) { freqtemp[(tmin%10)]++; tmin/=10;} 
                while(tsec>0) { freqtemp[(tsec%10)]++; tsec/=10;}
               for(ll i=0;i<10;i++)
                    if(freqtemp[i]>freq[i]){ hobe=false;break;}
                if(hobe)
                {
                    loop = true;
                    cout<<"00:";
                    if(mins<10) cout<<"0"; cout<<mins<<":";
                    if(sec<10) cout<<"0"; cout<<sec;
                    goto label;
                }
            }
        }
    }
    if(!loop)
        cout<<"Impossible";
    label:
    return 0;
}