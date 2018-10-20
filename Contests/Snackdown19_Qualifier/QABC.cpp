// @author: @amitrajitbose

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main()
{
	ll t;
	cin >> t;
	while(t--)
	{
		ll n;
		cin >> n;
    ll A[n];
    ll B[n];
    ll i,m;
    int f=1; //flag says TAK TAKA TAK
    for(i=0;i<n;i++)
      cin>>A[i];
    for(i=0;i<n;i++)
      cin>>B[i];
    for(i=0;i<n-2;i++)
    {
      m=B[i]-A[i];
      B[i]=B[i]-(1*m);
		  B[i+1]=B[i+1]-(2*m);
		  B[i+2]=B[i+2]-(3*m);
		  if(B[i+1]<A[i+1] or B[i+2]<A[i+2])
      {
        f=0; //NIE
        break;
      }
    }
    if(B[n-2]!=A[n-2] or B[n-1]!=A[n-1])
    {
      f=0; //NIE
    }
    if(f==1)
      cout<<"TAK"<<endl;
    else
      cout<<"NIE"<<endl;
	}
	return 0;
}
