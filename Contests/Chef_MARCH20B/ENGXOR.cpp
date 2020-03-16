#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll oddSetBits(ll n){
    if (n == 0) return 0;
    if (n%2 == 0) return (oddSetBits(floor(n/2)));
    if (n%2 == 1) return (1 - oddSetBits(floor(n/2)));
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll tc;
    cin >> tc;
    for(ll test=0; test<tc; test++){
        ll n,q;
        cin >> n >> q;
        ll arr[n];
        for(ll i=0; i<n; i++){
            cin >> arr[i];
        }
        for(ll qr=0; qr<q; qr++){
            ll elem;
            cin >> elem;
            ll odd = 0;
            ll even = 0;
            for(ll i=0; i<n; i++){
                if (oddSetBits(elem ^ arr[i])==1) odd++;
                else even++;
            }
            cout << even << " " << odd << "\n";
        }
    }
}