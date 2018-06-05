//http://www.spoj.com/problems/NSTEPS/
/*
We see that there are basically two pattern series.
0 1 4 5 8 9 12 13 16 17 so on = n where n=n+1 and n+4 for every alternate step

2 3 6 7 10 11 14 15 18 19 so on = same as above starts from n=2

It is also evident that for every value the pair (x,y) are either both even or both odd.

So,

if both even, n=x+y
if both odd, n=(x+y)-1
else if one even one odd, n= not possible =No Number
*/
#include <bits/stdc++.h>
using namespace std;
int find(int x,int y){
	int a=x%2;
	int b=y%2;
	if(x==y){
		if(a==0){
			return (x+y);
		}
		else if(a==1 && b==1){
			return (x+y)-1;
		}
	}
	else if(x==y+2){
		if(a==0)
		  return (x+y);
		else
		  return (x+y-1);	
	}
	else
	{
		return -1;
	}
}
int main()
{
	int test;
	cin>>test;
	while(test--){
		int x,y;
		cin>>x>>y;
		if(find(x,y)==-1){
			cout<<"No Number"<<endl;
		}
		else
		{
			cout<<find(x,y)<<endl;
		}
	}
return 0;
}
