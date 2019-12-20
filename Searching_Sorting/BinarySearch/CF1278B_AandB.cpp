// https://codeforces.com/contest/1278/problem/B
// Author : @amitrajitbose
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define e1e9 1000000000

int main()
{
	ll tc;
	cin >> tc;
	while(tc--)
	{
		// take inputs for each test case
		ll a,b,diff;
		cin >> a >> b;
		diff = abs(a-b);

		if (diff == 0){
			cout << 0 << endl;
			continue;
		}

		// apply binary search
		ll low = 0;
		ll high = e1e9;
		ll ans = e1e9;
		ll mid, val;
		while (low <= high)
		{
			mid = low + ((high - low)/2);
            //cout << "Mid = " << mid << endl;
            val = (mid * (mid+1))/2;
			if (val >= diff){
				ans = mid; // minimize this
				high = mid-1;
			}
			else {
				low = mid+1;
			}
		}
        //cout << ans << ",";
        // find upper limit that is having even difference with sum - (a-b)
        val = (ans * (ans + 1)) / 2;
        while ((val - diff)%2 == 1){
            ans += 1;
            val = (ans * (ans + 1)) / 2;
        }
		cout << ans << endl;
	}
}
