/*
Typical Example of Implementing Segmented Sieve
Problem: spoj.com/problems/PRIME1
Explanation: https://youtu.be/fByR5N-TseY
*/

#include <bits/stdc++.h>
#define MAX 100001
using namespace std;
typedef long long ll;

//Normal Sieve that returns a vector of boolean prime array
vector<int>* sieve(){
	bool isprime[MAX];
	memset(isprime,true,sizeof(isprime));
	isprime[1]=false;//one is not a prime number
	for(int i=2;i*i<MAX;i++){
		if(isprime[i]){
			for(int j=i*i;j<MAX;j+=i){
				isprime[j]=false; //making all multiples of i nonprime
			}
		}
	}
	vector<int>* primes=new vector<int>();
	primes->push_back(2);
	for(int i=3;i<MAX;i+=2){
		if(isprime[i]){
			primes->push_back(i);
		}
	}
	return primes;
}
//Segmented Sieve function that adjusts the index and stores only required amount of primes
void printPrimes(ll l, ll r, vector<int>* &primes){
    if(l==1)
        l++;
	bool isprime[r-l+1];
	memset(isprime,true,sizeof(isprime));

	for(int i=0;primes->at(i)*(ll)primes->at(i)<=r;i++){
		int currentPrime = primes->at(i);
		//Just smaller or equal to l, trying to reach as close as possible to l
		ll base = (l/currentPrime)*currentPrime;
		if(base<l){
			base=base+currentPrime;
		}
		//Mark all multiples false within L to R
		for(int j=base;j<=r;j+=currentPrime){
			isprime[j-l]=false; //index adjustment due to segmented array
		}
		//There may be a case where base is itself a prime, e.g L=2,L=3
		if(base==currentPrime){
			isprime[base-l]=true;
		}
	}
	for(int i=0;i<=r-l;i++){
		if(isprime[i]){
			cout<<i+l<<endl;
		}
	}
}
int main(){
	vector<int>* primes=sieve();
	int t;
	cin>>t;
	while(t--){
		ll m,n;
		cin>>m>>n;
		printPrimes(m,n,primes);
		cout<<endl;
	}
	return 0;
}