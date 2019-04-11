/*
 * Author: Amitrajit Bose 
 * Problem Name: Connectivity Problem
 * Approach: DFS Traversal
 */

#include <bits/stdc++.h>
#include <iostream>

using namespace std;
typedef long long ll;
#define FOR(i,m,n) for(__typeof(n) i = m; i<(n); i++)
#define test ll t; cin >> t; while(t--)

const int N = 1e6+3;
vector<int> graph[N];

void dfs(int u, bool vis[])
{
	vis[u] = true;
	for(int v: graph[u])
	{
		if(vis[v])
			continue;
		else
			dfs(v,vis);
	}
}

int main()
{
	freopen("in_connectivity.txt", "r", stdin);
	int n; //nodes
	int m; //edges
	int q; //queries
	int u,v; //start, end = u---v
	cin >> n >> m;

	while(m--)
	{
		cin >> u >> v;
		graph[u].push_back(v);
		graph[v].push_back(u); //because undirected
	}
	cin >> q;
	while(q--)
	{
		cin >> u >> v;
		bool vis[N];
		dfs(u, vis);
		if(vis[v])
			cout << "Connected: " << u << " & " << v << endl;
		else
			cout << "Not Connected: " << u << " & " << v << endl;
	}
	return 0;
}

