/*
SPOJ - Horrible - https://www.spoj.com/problems/HORRIBLE/
Author : @amitrajitbose
*/
#include <bits/stdc++.h>
using namespace std;
//#define LARGENUMBER 999999
typedef long long ll;

void updateLazy(ll segmentTree[], ll lazyTree[], ll start, ll end, ll delta, ll low, ll high, ll pos)
{
	// check whether any past update is left on the lazy-tree
	// if not zero, thus update is pending
	// thus update tree at the position and propagate the value to its
	// child nodes in the lazy tree
	if(lazyTree[pos] != 0){
		segmentTree[pos] += lazyTree[pos]*(high-low+1); //updating by adding the old value
		//check if it is NOT a leaf node
		if(low != high){
			lazyTree[(2*pos)] += lazyTree[pos];
			lazyTree[(2*pos)+1] += lazyTree[pos];
			// thus the lazy value is propagated to its children now
		}
		lazyTree[pos] = 0;
	}

	// check overlap condition before updating
  if(low>high){
		return;
	}
	// if NO OVERLAP
	if(start>high or end<low){
		return;
	}

	// if COMPLETE OVERLAP
	if(start<=low and end>=high){
		segmentTree[pos] += delta*(high-low+1); // updating
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
	segmentTree[pos] = (segmentTree[(2*pos)] + segmentTree[(2*pos)+1]);
}


ll query(ll segmentTree[], ll lazyTree[], ll queryLow, ll queryHigh, ll low, ll high, ll pos)
{
	// check if all propagation are done, same as above
	if(lazyTree[pos] != 0){
		segmentTree[pos] += lazyTree[pos]*(high-low+1);
		if(low!=high){
			// non leaf node
			lazyTree[(2*pos)] += lazyTree[pos];
			lazyTree[(2*pos)+1] += lazyTree[pos];
		}
		lazyTree[pos] = 0;
	}

	// now check overlap conditons
	// if NO OVERLAP
	if((queryLow>high or queryHigh<low) or (low>high)){
		return 0;
	}

	// if COMPLETE OVERLAP
	if(queryLow<=low and queryHigh>=high){
		// current range is completely overlapped by query range
		return segmentTree[pos];
	}

	// else PARTIAL OVERLAP
	ll mid = (low+high)/2;
	//ll sidea = query(segmentTree, lazyTree, queryLow, queryHigh, low, mid, (2*pos));
	//ll sideb = query(segmentTree, lazyTree, queryLow, queryHigh, mid+1, high, ((2*pos)+1));
	return (query(segmentTree, lazyTree, queryLow, queryHigh, low, mid, (2*pos)) + query(segmentTree, lazyTree, queryLow, queryHigh, mid+1, high, ((2*pos)+1)));
}

// build the binary segment tree - O(N)
void build(ll node, ll start, ll end, ll tree[], ll A[])
{
    if(start == end){
        tree[node]=A[start];
        return;
    }
    else{
        ll mid = (start+end)/2;
        //starting recursing down to the left child
        build(2*node, start, mid, tree, A);
        //once done, now recurse down the right child
        build((2*node)+1, mid+1, end, tree, A);
        //leaf nodes will be the element themselves, or you can say unit sized range
        //internal nodes will have min of both the left and right child, because it is RSQ
        tree[node] = (tree[2*node] + tree[(2*node)+1]);
    }
}

int main()
{
	ll t;
	cin >> t;
	while(t--)
	{
	    ll n,q; //array values and queries
	    cin >> n >> q;
	    ll arr[1000000]; //since one based indexing
      fill(arr,arr+1000000,0); //fill with zero
      arr[0]=-999; // since one based indexing, should not use this place
		  ll lazy[2*(1000000)];
		  memset(lazy, 0, sizeof(lazy)); //initializing with zeroes
		//accepting values
	    
	    ll tree[2*(1000000)]; // extra just to be safe
	    
		// build the tree
	    build(1, 1, n, tree, arr);
		
	    while(q--){
	        ll type;
	        ll x,y;
	        cin >> type >> x >> y;
	        if(type==1){
				      ll z = query(tree, lazy, x, y, 1, n, 1);
	            cout << z << endl;
	        }
	        else if(type==0){
              ll del;
              cin >> del;
	            updateLazy(tree, lazy, x, y, del, 1, n, 1);
	        }
	    }
	}
  return 0;
}