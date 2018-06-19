//Tabulation Based Dynamic Programming
//Bottom up
//nth Fibonacci Number
//Author: Amitrajit Bose
/*
NOTE: 
First value(n=1) is fibonacciseries[0]=0
Second value(n=2) is fibonacciseries[1]=1
Third value(n=3) is fibonacciseries[2]=1
Fourth value(n=4) is fibonacciseries[3]=2
..
so on
*/
#include <iostream>
using namespace std;
#define ll long long int
ll fibo(ll n){
    if(n==1)
    return 0;
    else if(n==2)
    return 1;
    else
    {
    ll lookuptable[n+1];
    lookuptable[0]=0;
    lookuptable[1]=1;
    for(ll i=2;i<=n;i++){
        lookuptable[i]=lookuptable[i-1]+lookuptable[i-2];
    }
    return lookuptable[n-1];
    }
}
int main() {
    ll n;
	cin>>n;
	cout<<fibo(n);
	return 0;
}