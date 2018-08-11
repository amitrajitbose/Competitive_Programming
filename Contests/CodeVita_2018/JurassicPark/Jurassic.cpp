#include <bits/stdc++.h>
using namespace std;
#define ll long long int
int main(){
	ll r,c,i,j;
	cin >> r >> c;
	int park[r][c];
	ll g1,g2,g3,g4,g5,g6,c1,c2;
	char inp;
	/*
	Grass=0
	Mountain=1
	Water=2
	*/

	cin>>g1>>g2>>g3>>g4>>g5>>g6>>c1>>c2;
	g1-=1;
	g2-=1;
	g3-=1;
	g4-=1;
	g5-=1;
	g6-=1;
	c1-=1;
	c2-=1;
	//Now they are zero based index

	for(i=0;i<r;i++){
		for(j=0;j<c;j++){
			cin>>inp;
			if(inp=='G')
				park[i][j]=0;
			else if(inp=='M')
				park[i][j]=1;
			else if(inp=='W')
				park[i][j]=2;
		}
	}
	
	/*
	If safe mark 3 , if danger mark 4 else leave*/
	ll safe=0;
	for(i=0;i<r;i++){
		for(j=0;j<c;j++){
			if(park[i][j]==2)
				park[i][j]=3;
			else if()




	for(i=0;i<r;i++){
		for(j=0;j<c;j++){
			cout<<park[i][j]<<" ";
		}
		cout<<endl;
	}

	return 0;
}
