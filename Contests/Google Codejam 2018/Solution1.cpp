#include <iostream>
#include <algorithm>
#include <vector>
typedef long long ll;

int main () {
	int test;
	std::cin>>test;
	for (int t=1;t<=test;t++) {
		ll n,l = 0,r = 0,ans,flag = 0;
		std::cin>>n;
		ll a[n];
		std::vector <ll> left,right,sorted_arr;
		for (int i=0;i<n;i++) {
			std::cin>>a[i];
			if (i % 2 == 0)
				left.push_back(a[i]);
			else
				right.push_back(a[i]);
		}
		
		std::sort(left.begin(),left.end());
		std::sort(right.begin(),right.end());
		
		for (int i=0;i<n;i++) {
			if (i % 2 == 0) 
				sorted_arr.push_back(left[l++]);
			else
				sorted_arr.push_back(right[r++]);
			//std::cout<<sorted_arr[i]<<" ";
		}
		//std::cout<<"\n";
		std::sort(a,a+n);
		
		for (int i=0;i<n;i++) {
			if (a[i] != sorted_arr[i]) {
				flag = 1;
				ans = i;
				break;
			}
		}
		
		if (flag)
			std::cout<<"Case #"<<t<<": "<<ans<<"\n";
		else 
			std::cout<<"Case #"<<t<<": "<<"OK\n";
	}
}