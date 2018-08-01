// Program to display the n-th non-fibonacci number
#include <bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cin>>n;
	int a,b,c,tmp;
	a=0;
	b=1;
	c=n;
	/*
	a,b are for generating the fibonacci sequence
	c stores a copy of n
	tmp is used for temporary purpose
	*/
	while(b-a-1<c){
		if(b-a>1)
			c-=(b-a-1);
		tmp=a;
		a=b;
		b=tmp+b;
	}
	cout<<(a+c)<<endl;
	return 0;
}