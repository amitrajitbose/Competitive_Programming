//Longest Increasing Subsequence Problem O(n^2)
//HackerRank: https://www.hackerrank.com/challenges/longest-increasing-subsequent/problem (needs O(nlogn))
//GFG: https://www.geeksforgeeks.org/longest-increasing-subsequence/
//Author: Amitrajit Bose
//Thanks to GFG for the wonderful explanation
#include <bits/stdc++.h>
using namespace std;
#define MAX 1000001
#define ll long long int

ll lis(ll arr[],ll n){
	if(n==1)
		return 1;
	ll i,j;
	//create table to store lis values upto the index
	ll lis[n];
	//initialise all table values to 1 by default
	for(i=0;i<n;i++){
		lis[i]=1;
	}
	for(i=1;i<n;i++){
		for(j=0;j<i;j++){
			if(arr[i]>arr[j]){
				lis[i]=max(lis[i],lis[j]+1);
			}
		}
	}
	return lis[n-1];
}
int main(){
	ll n;
	//cout<<"Enter Array Size: ";
	cin>>n;
	ll arr[n];
	ll i;
	//cout<<"Enter Values: "<<endl;
	for(i=0;i<n;i++){
		cin>>arr[i];
	}
	//cout<<"Length of Longest Increasing Subsequence: "<<lis(arr,n)<<endl;
	cout<<lis(arr,n)<<endl;
	return 0;
}