// https://www.codechef.com/problems/PPERM

#include <bits/stdc++.h>
#define MAX 5000001
using namespace std;
typedef long long ll;

ll isprime[MAX];
ll primes[MAX];
ll perm[MAX];

void sievePerm(){
	fill(isprime, isprime+MAX, 1);
	primes[1]=0;
	perm[1]=1;

	isprime[1]=0;//one is not a prime number
	for(ll i=2; i*i<MAX; i++){
		if(isprime[i]){
			for(ll j=i*i; j<MAX; j+=i){
				isprime[j]=0; //making all multiples of i nonprime
			}
		}
	}
	ll MOD = 1000000007;
	for(ll i=2;i<MAX;i++){
		primes[i]=primes[i-1]+isprime[i];
		perm[i]=(perm[i-1]*(1+primes[i]))%MOD;
	}
}
int main()
{
    sievePerm();
	ll t;
	scanf("%lld",&t);
	while(t--)
	{
		ll n;
		scanf("%lld",&n);
		printf("%lld\n",perm[n]);
	}
	return 0;
}