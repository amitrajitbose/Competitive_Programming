//http://www.spoj.com/problems/EIGHTS/

#include <iostream>
using namespace std;
 
int main() {
        long long int t;
        cin>>t;
        while(t--)
        {
        	long long int k;
        long long int out;
        	cin>>k;
        	if(k==1)
        	out=192;
        	else
        	out=192+((k-1)*250);

        	cout<<out<<endl;
        }
        return 0;
}  