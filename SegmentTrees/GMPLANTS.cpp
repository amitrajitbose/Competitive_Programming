
/*
 * Author: Amitrajit Bose
 * Problem Link: https://www.codechef.com/problems/IOPC1207 
 * Approach: Lazy Prop
 */

#include <bits/stdc++.h>
#include <iostream>
#include <ctype.h>
#include <climits>
using namespace std;
typedef long long ll;
#define FOR(i,m,n) for(__typeof(n) i = m; i<(n); i++)
#define test ll t; cin >> t; while(t--)

void updateLazy(ll segmentTree[], ll lazyTree[], ll start, ll end, ll delta, ll low, ll high, ll pos)
{
	if(low>high){
		return;
	}
	// check whether any past update is left on the lazy-tree
	// if not zero, thus update is pending
	// thus update tree at the position and propagate the value to its
	// child nodes in the lazy tree
	if(lazyTree[pos] != 0){
		segmentTree[pos] += lazyTree[pos]; //updating by adding the old value
		//check if it is NOT a leaf node
		if(low != high){
			lazyTree[(2*pos)] += lazyTree[pos];
			lazyTree[(2*pos)+1] += lazyTree[pos];
			// thus the lazy value is propagated to its children now
		}
		lazyTree[pos] = 0;
	}

	// check overlap condition before updating

	// if NO OVERLAP
	if(start>high or end<low){
		return;
	}

	// if COMPLETE OVERLAP
	if(start<=low and end>=high){
		segmentTree[pos] += delta; // updating
		if(low != high){
			lazyTree[(2*pos)] += delta;
			lazyTree[(2*pos)+1] += delta;
		}
		return;
	}

	// else PARTIAL OVERLAP
	// thus look both left and right side
	ll mid=(low+high)/2;
	updateLazy(segmentTree, lazyTree, start, end, delta, low, mid, (2*pos));
	updateLazy(segmentTree, lazyTree, start, end, delta, mid+1, high, (2*pos)+1);
	segmentTree[pos] = !segmentTree[pos];
}

ll query(ll segmentTree[], ll lazyTree[], ll queryLow, ll queryHigh, ll low, ll high, ll pos)
{
	if(low>high){
		return 0;
	}

	// check if all propagation are done, same as above
	if(lazyTree[pos] != 0){
		segmentTree[pos] += lazyTree[pos];
		if(low!=high){
			// non leaf node
			lazyTree[(2*pos)] += lazyTree[pos];
			lazyTree[(2*pos)+1] += lazyTree[pos];
		}
		lazyTree[pos] = 0;
	}

	// now check overlap conditons
	// if NO OVERLAP
	if(queryLow>high or queryHigh<low){
		return 0;
	}

	// if COMPLETE OVERLAP
	if(queryLow<=low and queryHigh>=high){
		// current range is completely overlapped by query range
		return segmentTree[pos];
	}

	// else PARTIAL OVERLAP
	ll mid = (low+high)/2;
	ll sidea = query(segmentTree, lazyTree, queryLow, queryHigh, low, mid, (2*pos));
	ll sideb = query(segmentTree, lazyTree, queryLow, queryHigh, mid+1, high, (2*pos)+1);
	return sidea + sideb;
}


int main()
{
	test
	{
		ll x,y,z,q;
		cin >> x >> y >> z >> q;
		//make the arrays
		ll *xarr, *yarr, *zarr, *xtree, *ytree, *ztree, *xlazy, *ylazy, *zlazy;
		xarr = new ll[x];
		xtree = new ll [2*x +10];
		xlazy = new ll [2*x +10];
		yarr = new ll[y];
		ytree = new ll [2*y +10];
		ylazy = new ll [2*y +10];
		zarr = new ll[z];
		ztree = new ll [2*z +10];
		zlazy = new ll [2*z +10];
		fill(xarr, xarr+x, 0);
		fill(yarr, yarr+y, 0);
		fill(zarr, zarr+z, 0);
		fill(xtree, xtree+x, 0);
		fill(ytree, ytree+y, 0);
		fill(ztree, ztree+z, 0);
		fill(xlazy, xlazy+x, 0);
		fill(ylazy, ylazy+y, 0);
		fill(zlazy, zlazy+z, 0);
		while(q--){
			ll type,i,j,x1,x2,y1,y2,z1,z2;
			cin >> type;
			if(type==0){
				cin >> i >> j;
				updateLazy(xtree, xlazy, i+1, j+1, 0, 1, x, 1);
			}
			else if(type==1){
				cin >> i >> j;
				updateLazy(ytree, ylazy, i+1, j+1, 0, 1, y, 1);
			}
			else if(type==2){
				cin >> i >> j;
				updateLazy(ztree, zlazy, i+1, j+1, 0, 1, z, 1);
			}
			else if(type==3){
				cin >> x1 >> y1 >> z1 >> x2 >> y2 >> z2;
				ll xred = query(xtree, xlazy, x1, x2+1, 1, x, 1);
				ll yred = query(ytree, ylazy, y1, y2+1, 1, y, 1);
				ll zred = query(ztree, zlazy, z1, z2+1, 1, z, 1);
				ll xgreen = x2-x1+1 - xred;
				ll ygreen = y2-y1+1 - yred;
				ll zgreen = z2-z1+1 - zred;
				//cout << "DEBUG: ";
				//cout << xred << "," << yred << "," << zred << endl;

				ll computedanswer = (xred*yred*zred)+(xred*ygreen*zgreen)+(xgreen*yred*zgreen)+(xgreen*ygreen*zred);
				cout << computedanswer << endl;
			}
		}
	}
	return 0;
}