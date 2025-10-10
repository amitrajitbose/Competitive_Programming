#include <bits/stdc++.h>
using namespace std;
#define int long long
signed  main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int a, b;
    cin>>a>>b;
    int ans=0;
    while(a&&b){
        if(a>b){
            ans+=a/b;
            a%=b; 
        }else{
            ans+=b/a; 
            b%=a;
        }
    }
    cout<<ans<<"\n";
}
