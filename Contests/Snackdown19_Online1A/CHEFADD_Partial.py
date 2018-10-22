#include <iostream>
using namespace std;
int main() 
{ 
    long t;
    cin>>t;
    while(t--)
    {
       long a,b,c;
       cin>>a>>b>>c;
       int ac=__builtin_popcount(a),bc=__builtin_popcount(b),ans=0;
       for(int i=1;i<=c/2;i++)
       {
           int ic=__builtin_popcount(i);
           int cic=__builtin_popcount(c-i);
           int ipcic=__builtin_popcount(i+(c/2));
           int cipcic=__builtin_popcount(c-(i+(c/2)));
           if(ic==ac && cic==bc)
                ans++;
            if(ipcic==ac && cipcic==bc)
                ans++;
        }
        cout<<ans<<endl;
    }
   return 0; 
}
