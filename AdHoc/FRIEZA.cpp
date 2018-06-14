//www.codechef.com/QUCO2018/problems/FRIEZA
#include <bits/stdc++.h>
#include <string.h>
using namespace std;
#define forloop(i,a,b) for(int i=a;i<b;i++)
#define MAX 1001001
bool isinfrieza(char ch){
	if(ch=='f' || ch=='r' || ch=='i' || ch=='e' || ch=='z' ||ch=='a'){
		return true;
	}
	return false;
}
char str[MAX];
int main(){
	int t;
	cin>>t;
	while(t--){
		scanf("%s",str);
		int len=strlen(str);
		if(isinfrieza(str[len-1])){str[len]='w';str[len+1]='\0';}
		else{str[len]='f';str[len+1]='\0';}
		len=strlen(str);
		int ans[len];
		int k=0;
		int count=1;
		//cout<<len<<endl;
		forloop(i,0,len-1){
			char ch=str[i];
			char nch=str[i+1];
			if(isinfrieza(ch) && isinfrieza(nch)){
				count++;
				//cout<<"ONE ";
			}
			else if(!isinfrieza(ch) && !isinfrieza(nch)){
				count++;
				//cout<<"TWO ";
			}
			else if((isinfrieza(ch) && !isinfrieza(nch))||(!isinfrieza(ch) && isinfrieza(nch))){
				ans[k]=count;
				k++;
				count=1;
				//cout<<"THREE ";
			}
		}
		//cout<<"k="<<k<<endl; //debug
		for(int i=0;i<k;i++){
			cout<<ans[i];
		}
		k=0;
		cout<<endl;
	}
	return 0;
}