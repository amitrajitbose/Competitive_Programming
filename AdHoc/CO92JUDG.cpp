// @Amitrajit Bose
// https://www.codechef.com/problems/CO92JUDG
#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin >> t;
	while(t--){
		int n;
		cin >> n;
		int a[n],b[n];
		
		for(int i=0;i<n;i++){
			cin >> a[i];
		}
 
		for(int i=0;i<n;i++){
			cin >> b[i];
		}
		int maxa=a[0];
		int suma=a[0];
		int maxb=b[0];
		int sumb=b[0];
 
		for(int i=1;i<n;i++){
		    suma+=a[i];
		    sumb+=b[i];
			if(maxa<a[i]){
				maxa=a[i];
			}
			if(maxb<b[i]){
				maxb=b[i];
			}
		}
	    
		suma=suma-maxa;
		sumb=sumb-maxb;
		//cout<<suma<<" "<<maxa<<endl<<sumb<<" "<<maxb<<endl;
		if(suma<sumb)
			cout<<"Alice"<<endl;
		else if(sumb<suma)
			cout<<"Bob"<<endl;
		else if(suma==sumb)
			cout<<"Draw"<<endl;
	}
	return 0;
}