// https://www.codechef.com/problems/CIELRCPT
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
  int test;
  cin >> test;
  while(test--)
  {
    ll n, prev;
    ll c=0;
    cin >> n;
    while(n>0)
    {
      prev = pow(2, floor(log(n)/log(2)));
      if(prev > 2048)
        prev=2048;
      n-=prev;
      c++;
    }
    cout << c << endl;
  }
}