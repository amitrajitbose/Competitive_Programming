#include <iostream>
using namespace std;
typedef long long LL;
#define MOD 1000000007
int main()
{
	LL n;
	cin >> n;
	LL home=1;
	LL away=0;
	LL tmphome, tmpaway;
	for(LL i=1;i<=n;i++)
	{
		tmphome=(3*away)%MOD; //if I reach D, that means I was at A,B or C
		tmpaway=((2*away)+home)%MOD; //if I reach A(suppose), then I was at B,C or D(home)
		home=tmphome;
		away=tmpaway;
	}
	cout << home <<endl;
}