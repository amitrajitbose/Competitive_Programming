//Memoization Based Dynamic Programming
//Top Down
//nth Fibonacci Number
//Author: Amitrajit Bose
/*
NOTE: 
Zeroth value(n=0) is fibonacciseries[0]=0
First value(n=1) is fibonacciseries[1]=1
Second value(n=2) is fibonacciseries[2]=1
Third value(n=3) is fibonacciseries[3]=2
..
so on
*/
#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define MAX 1000001
ll lookuptable[MAX];
ll fibo(ll n){
    if(n==1){
    	lookuptable[1]=1;
    	return 1;
    }
    else if(n==0){
    	lookuptable[0]=0;
    	return 0;
    }
    else
    {
    	if(lookuptable[n]==-1){
    		lookuptable[n] = fibo(n-1)+fibo(n-2);
    		return lookuptable[n];
    	}

    	else
    		return lookuptable[n];
    }
}
int main() {
	ll n;
	cin>>n;
	memset(lookuptable,-1,sizeof(lookuptable));
	//memset can only set to 0 or -1 values nothing else
	//memset will be done only once, thus inside main
	//memset can be only done inside some function
	cout<<fibo(n);
	return 0;
}
