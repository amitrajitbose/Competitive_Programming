// https://www.geeksforgeeks.org/find-the-missing-number/
#include <iostream>
using namespace std;
int findMissingNumber(int a[],int n){
	int i,t;
	t=(n+1)*(n+2)/2; //considering the missing number in total
	for(i=0;i<n;i++){
		t-=a[i];
	}
	return t;
}
int main(){
	int n;
	cout<<"Enter Size(W/O counting missing number): ";
	cin>>n;
	cout<<"Enter The Numbers: ";
	int a[n];
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	cout<<findMissingNumber(a,n)<<" Is Missing"<<endl;
	cin.get();
	cin.get();
	return 0;
}
