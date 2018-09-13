
/*
 * Author: Amitrajit Bose
 * Problem Link: https://www.spoj.com/problems/HISTOGRA/ 
 * Approach: In a empty stack keep adding all indices of increasing bars,
  if bar is smaller than bar at top of stack, then keep popping from stack
  while TOS is greater. Calculate area with the removed bar as smallest
  bar. In this case, the formula varies of stack is empty. After 
  traversing entire histogram, keep popping the stack and calcalate
  area to check if a larger rectangle can be found.
 */

#include<bits/stdc++.h>
#include <iostream>
#include<ctype.h>
#include<climits>
using namespace std;
typedef long long ll;

#define rep(i,m,n) for(i=m; i<(n); i++)
#define test ll t; cin>>t; while(t--)

ll maxArea(ll hist[], ll n)
{
	stack<ll> st;
	st.push(0); //push first index to stack
	ll maxm=0; //maximum area
	ll i,area,p;
	rep(i,1,n)
	{
		if(st.empty() or hist[i]>=hist[st.top()])
			st.push(i);
		else
		{
			//the bar is now sloping down
			while(!st.empty() and hist[i]<hist[st.top()])
			{
				p = st.top(); //kept the topmost item of stack in hand and pop
				st.pop();
				if(st.empty())
					area = hist[p]*i;
				else
					area = hist[p]*(i-st.top()-1);
				maxm=max(maxm,area);
			}
			st.push(i);//taken into consideration now
		}
	}
	// traversed the entire histogram
	// now pop the stack and recalculate for higher area, if any
	while(!st.empty())
	{
		p=st.top();
		st.pop();
		if(st.empty())
			area=hist[p]*i;
		else
			area=hist[p]*(i-st.top()-1);
		maxm=max(maxm,area);
	}
	//cout << maxm << endl;
	return maxm;
}

int main()
{
	ll n,i;
	cin >> n; //first n
	while(n!=0)
	{
		ll arr[n];
		rep(i,0,n)
			cin >> arr[i];
		// inputs taken
		cout << maxArea(arr, n) << endl;
		cin >> n; //next n
	}
	return 0;
}
