// @amitrajitbose

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll validPosition(ll mid, ll arr[], ll n, ll c)
{
  ll prev=arr[0]; // assuming leftmost stall will always be taken by a cow
  ll count=1;
  for(ll i=1;i<n;i++){
    if(arr[i]-prev >= mid)
    {
      count+=1;
      prev=arr[i];
    }
  }
  if(count<c)
    return 0;
  else
    return 1;
}

ll largestMinGap(ll arr[], ll n, ll c)
{
  ll low=0;
  ll high=1000000007; // as per question, masimum value
  ll mid,x;
  while(low <= high)
  {
    mid = (low+high)/2;
    if(validPosition(mid, arr, n, c)==1)
    {
      low=mid+1;
      x=mid;
    }
    else
      high=mid-1; //reducing the array size
  }
  return x;
}

int main() {
  ll test;
  cin >> test;
  while(test--)
  {
    ll n,c,ans;
    ll *arr = new ll[100007]; //constructor
    cin >> n >> c;
    for(ll i=0;i<n;i++)
    {
      cin >> arr[i];
    }
    sort(arr,arr+n);
    ans = largestMinGap(arr,n,c);
    delete [] arr; //destructor
    cout << ans << endl;
  }  
  return 0;
}