//Problem: https://www.codechef.com/AUG18B/problems/SPELLBOB
#include <bits/stdc++.h>
using namespace std;
int main(){
	int t;
	cin>>t;
	while(t--){
		char up[3],down[3];
		int i,b=2,o=1;
		int keepaside=0;
		cin>>up;
		cin>>down;
		for(i=0;i<3;i++){
			if((up[i]=='o' && down[i]=='b') || (up[i]=='b' && down[i]=='o'))
				keepaside++;
			else if(up[i]=='b' || down[i]=='b')
				b--;
			else if(up[i]=='o' || down[i]=='o')
				o--;
		}
		int flag=0; //1 means yes
		/*
		//DEBUG:
		cout<<keepaside<<endl;
		cout<<b<<endl;
		cout<<o<<endl;*/
		if(keepaside==3)
			flag=1;
		else if(keepaside==2){
			if(b==1 || o==0)
				flag=1;
		}
		else if(keepaside==1){
			if(b==0)
				flag=1;
			else if(b==1 && o==0)
				flag=1;
			else if(o==-1)
				flag=0;
		}
		else if(keepaside==0){
			if(b==0 && o==0)
				flag=1;
		}
		else
			flag=0; //all NO


		if(flag)
			cout<<"yes"<<endl;
		else
			cout<<"no"<<endl;

	}
	return 0;
}