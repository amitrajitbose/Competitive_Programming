#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main()
{
	ll tc;
	cin >> tc;
	while(tc--)
	{
		ll counter = 0;
		ll n,k,i,j;
		cin >> n >> k;
		ll *arr = new ll[n];
		for(i=0;i<n;i++)
		{
			cin >> arr[i];
		}
		///////////////////
		for(i=0;i<n;i++)
		{
			for(j=i;j<n;j++)
			{
				ll m,x,f;
				m = int(ceil(k/((j-i)+1)));
				ll lenS = (j-i)+1;
				ll *S = new ll[lenS];
				//subarray
				for(ll p=i;p<=j;p++)
				{
					S[p-i] = arr[p];
				}
				sort(S, S+lenS);
				ll ind = int(ceil(k/m));
				x = S[ind-1];
				cout << "X"<<x <<endl;
				f=0;
				for(ll p=0; p<lenS; p++)
				{
					cout << S[p] << ",";
					if(S[p]==x)
						f++;
				}
				cout << endl;
				cout << "f"<<f <<endl;
				ll flag= 0;
				for(ll p=0; p<lenS; p++)
				{
					if(S[p]==f){
						flag=1;
						break;
					}
				}
				cout << flag <<endl;
				if(flag)
					counter++;
			}
		}
		cout << counter << "\n";
	}
	return 0;
}