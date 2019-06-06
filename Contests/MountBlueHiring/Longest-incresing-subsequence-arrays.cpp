#include<bits/stdc++.h>
#include<iostream>
using namespace std;


#define abs(x) ((x)>0?(x):-(x))
#define MOD 1000000007
#define LL signed long long int
#define scan(x) scanf("%d",&x)

#define print(x) printf("%d\n",x)

#define scanll(x) scanf("%lld",&x)
#define printll(x) printf("%lld\n",x)


#define rep(i,from,to) for(int i=(from);i <= (to); ++i)

#define pii pair<int,int>

vector<int> G[2*100000+5];
LL pow(LL base, LL exponent,LL modulus)
{
    LL result = 1;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            result = (result * base) % modulus;
        exponent = exponent >> 1;
        base = (base * base) % modulus;
    }
    return result;
}

LL fact[1000000+5],ifact[1000000+5];
void pre_calc(int N)
{
    fact[0]=ifact[0]=1;
    for(int i=1; i<=N; ++i)
    {
        fact[i]=(fact[i-1]*i)%MOD;
        ifact[i]=pow(fact[i],MOD-2,MOD);
    }
}
LL ncr(int n,int r)
{
    LL ans=fact[n];
    ans=(ans*ifact[r])%MOD;
    ans=(ans*ifact[n-r])%MOD;
    return ans;
}
LL pN[500000+5];
LL pN_[500000+5];
int main(){
    int T;
    int N,M;
    pre_calc(500000);
    cin>>T;

    pN[0] = pN_[0] = 1;
    
    while(T--){
        cin>>M>>N;
        for(int i =1;i<=M;++i){
            pN[i] = pN[i-1]*N % MOD;
            pN_[i] = pN_[i-1]*(N-1) % MOD;
        }
        int ans = 0;
        for(int L = N;L<=M;++L){
            LL x = ncr(L-1,N-1) * pN_[L-N] % MOD;
            x = (x * pN[M-L]) % MOD;
            ans = ans + x;
            ans = ans % MOD;
        }
        cout<<ans<<'\n';
    }
}