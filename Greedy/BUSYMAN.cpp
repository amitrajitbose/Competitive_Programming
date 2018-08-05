// Problem Link: https://www.spoj.com/problems/BUSYMAN/
// UNWEIGHTED JOB SCHEDULING PROBLEM a.k.a ACTIVITY SELECTION PROBLEM

#include <bits/stdc++.h>
using namespace std;
struct Job
{
	int start,finish;
};

bool comparer(Job i, Job j){
	return (i.finish < j.finish);
}

int main(){
	int test;
	cin>>test;
	while(test--){
		int n;
		cin>>n;
		Job arr[n];
		for(int i=0;i<n;i++){
			cin>>arr[i].start>>arr[i].finish;
		}
		sort(arr,arr+n,comparer);
		int counter=1; //first activity will always be performed
		int j=0;
		for(int i=1;i<n;i++){
			if(arr[i].start>=arr[j].finish){
				counter++;
				j=i;
			}
		}
		cout<<counter<<endl;
	}
	return 0;
}
