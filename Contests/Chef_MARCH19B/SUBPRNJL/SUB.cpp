#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
using namespace std;
typedef long long ll;

ll* onehotencode(ll arr[], ll n)
{
	//ll len = *max_element(arr, arr+n);
	ll* onehot = new ll[2001];
	ll* ptr = onehot;
	for(ll i=0; i<n; i++)
	{
		onehot[arr[i]] += 1;
	}
	return ptr;
}

int main()
{
	ll tc;
	cin >> tc;
	while(tc--)
	{
		ll counter=0;
		ll n, k;
		cin >> n >> k;
		ll arr[n];
		for(ll i=0; i<n; i++)
		{
			cin >> arr[i];
		}
		
		//Core
		for(ll i=0; i<n; i++)
		{
			for(ll j=i; j<n; j++)
			{
				ll m = int(ceil(k/((j-i)+1)));
				ll S[j-i+1];
				ll X,F;
				for(ll p=i; p<=j ; p++)
				{
					S[p-i] = arr[p];
				}
				ll *freq = onehotencode(S, j-i+1);
				
				for(ll index=0; index<2001; index++)
				{
					freq[index] = freq[index] * m;
				}
				ll lsum = 0;
				for(ll val = 0; val<2001; val++)
				{
					if(lsum<k)
						lsum += freq[val];
					else
					{
						X = val-1;
						break;
					}
				}

				F = int(freq[X]/m);
				if(int(freq[F]/m) >= 1)
					counter += 0;

				delete freq;
				
			}
		}
		cout << counter << endl;
	}
	return 0;
}