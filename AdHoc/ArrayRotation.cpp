/*
Given an array of size N, rotate it by D elements. 

https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0/?track=placement
*/

#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	while(t--){
	    int n,d;
	    cin >> n;
	    int arr[n];
	    cin >> d;
	    for(int i=0;i<n;i++){
	        cin >> arr[i];
	    }
	    //on rotation by d places
	    for(int i=(d%n);i<n;i++){
	        cout<<arr[i]<<" ";
	    }
	    for(int i=0;i<d;i++){
	        cout<<arr[i]<<" ";
	    }
	    cout<<endl;
	}
	return 0;
}
