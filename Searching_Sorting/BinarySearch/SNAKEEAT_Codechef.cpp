
/*
 * Author: Amitrajit Bose
 * Approach: Binary Search
 * Problem : https://www.codechef.com/problems/SNAKEEAT
 */

#include <bits/stdc++.h>
#include <iostream>
#include <ctype.h>
#include <climits>
using namespace std;
typedef long long ll;
#define rep(i,m,n) for(i = m; i < (n); i++)
#define test ll t; cin >> t; while(t--)

// a modified version of binary search
ll binarySearch(ll arr[], ll l, ll r, ll k)
{
	if(l>r) // if all the snakes are less than query length
		return r+1;
	else
	{
		ll m = (l+r)/2;
		if(arr[0]>k)
			return 0; // if all snakes are greater than query length
		if(((arr[m]>=k and arr[m-1]<k)))
			return m;
		else if(arr[m] > k)
			return binarySearch(arr,l,m-1,k);
		else
			return binarySearch(arr,m+1,r,k);
	}
}

int main()
{
	test
	{
		ll n,q,k,i,ans,breakpoint;
		ll low,high;
		cin >> n >> q;
		ll *arr = new ll[n];
		rep(i,0,n)
		{
			cin >> arr[i];
		}
		// need to sort
		sort(arr, arr+n);
	    //generate the prefix sum (decreasing)
	    ll j;
	    ll *prefixsum = new ll[n+1];
	    prefixsum[n]=0;
	    prefixsum[n-1]=arr[n-1];
	    for(j=n-2;j>=0;j--)
	    {
	      prefixsum[j]=prefixsum[j+1]+arr[j];
	    }
	    //now process queries
		rep(i,0,q)
		{
			cin >> k;
			ans=0;
			breakpoint = binarySearch(arr,0,n-1,k);
			if(breakpoint == 0)
				ans = n;
			else if(breakpoint>0)
			{
				ans=n-breakpoint; // the right side elements are already greater than x
				/*TLE*/
	        //binary search
	        low = 0;
	        high = breakpoint;
	        ll mid,len;
	        while(low<=high)
	        {
	          mid = low + (high-low)/2;
	          len = breakpoint-mid;
	          if((k*len)-(prefixsum[mid]-prefixsum[breakpoint]) < mid+1)
	            high=mid-1;
	          else
	            low=mid+1;
	        }
				ans += (breakpoint-low);
			}
			cout << ans << endl;
		}
		delete [] arr;
		arr = NULL;
    	delete [] prefixsum;
    	prefixsum = NULL;
	}
	return 0;
}

/*
//TLE: O(Q*N)
while(high > low){
					if(x-arr[high] > high-low)
						break;
					if(arr[high]+1 == x){
						high-=1;
					}
					low+=1;
				}
				if(arr[high] < x)
					high += 1;
*/
