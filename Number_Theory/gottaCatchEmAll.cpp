// Author: @amitrajitbose
/*
Used divisor sieve, counted frequency using hash, prefix logic used on hash
Problem : https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/gotta-beat-em-all/
*/
 
#include <bits/stdc++.h>
using namespace std;
#define MAX 33000
bool p[MAX];
// find prime number upto 33000, we don't need above 33000 because limit of case is 10^7, and 10^7 root is around 32000
void sieve(){
	memset(p,0,sizeof(p));
	p[0]=1;
	p[1]=1;
	for(int i=2;i<=MAX;i++){
		if(!p[i]){
			for(int j=i*i;j<=MAX;j+=i)
				p[j]=1;
		}
	}
}
 
int main()
{
	int t,cap;
	int arr[cap];
	for(int i=0;i<cap;i++)
		arr[i]=i+1;
	cin>>t>>cap;
	int factors[cap+1];
	memset(factors,0,sizeof(factors));
	//sieve logic for counting factors
	for(int i=1;i<=cap;i++)
	{
		for(int j=i;j<=cap;j+=i)
		{
			factors[j]+=1;
		}
	}
	
	int precount[cap+1];
	memset(precount,0,sizeof(precount));
	for(int i=1;i<=cap;i++)
	{
	    precount[factors[i]]++;
	}
	
	for(int i=1;i<=cap;i++)
	{
	    precount[i]+=precount[i-1];
	}
	while(t--)
	{
		int i;
		cin>>i;
		int x=factors[i];
		cout<<precount[x-1]<<endl;
	}
	return 0;
}