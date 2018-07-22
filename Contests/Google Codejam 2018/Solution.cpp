#include <iostream>
#include <string>
#include <algorithm>

long long find_d (std::string s) {
	long long ans = 0,c = 1;
	for (int i=0;i<s.size();i++) {
		if (s[i] == 'C') 
			c *= 2;
		else
			ans += c;
	}
	return ans;
}

int main () {
	int test;
	std::cin>>test;
	for (int t=1;t<=test;t++) {
		long long d,ans = 0,count_s = 0;
		std::string s;
		std::cin>>d>>s;
		long long n = s.size(),req = find_d(s);
		
		if (req <= d) {
			std::cout<<"Case #"<<t<<": 0\n";
			continue;
		}
		
		for (int i=0;i<n;i++) 
			count_s += (s[i] == 'S');
			
		if (count_s > d) {
			std::cout<<"Case #"<<t<<": IMPOSSIBLE\n";
			continue;
		}
		
		while (1) {
			for (int i=n-1;i>=1;i--) {
				if (s[i] == 'S' && s[i-1] == 'C') {
					std::swap(s[i],s[i-1]);
					ans++;
					break;
				}
			}
			if (find_d(s) <= d) {
				std::cout<<"Case #"<<t<<": "<<ans<<"\n";
				break;
			}
		}
	}
}