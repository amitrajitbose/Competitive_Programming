/* Read input from STDIN. Print your output to STDOUT*/
#include <iostream>
using namespace std;
typedef long long ll;

ll go(ll, ll , ll);

int main()
{
    ll x,y,n;
    ll i;
    cin>>x;
    cin>>y;
    cin>>n;
    int arr[n];
    for(i=0;i<n;i++)
    {
      cin >> arr[i];
    }
    ll t=0;
    for(i=0;i<n;i++)
    {
      t+=go(arr[i],x,y);;
    }
    cout<<t<<endl;
    return 0;
}

ll go(ll height,ll x,ll y)
{
  if(x >= height)    
  	return 1;
  ll j = height/(x-y);
  ll climbed = j*(x-y);
  if(climbed+y<height)    
  	return j+1;
  climbed -= x-y;
  while(y+climbed >= height){
    j -= 1;
    climbed -= x-y;
  }
  if(j==0)    
    return 1;
  return j;
}