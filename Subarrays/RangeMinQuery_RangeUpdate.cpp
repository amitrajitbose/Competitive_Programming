/*
 * Problem: Range minimum query in a sequence of number, also update a range of numbers
 * Approach: Segment Tree with lazy propagation
 */

#include <bits/stdc++.h>
using namespace std;
#define LARGENUMBER 999999

void updateLazy(int segmentTree[], int lazyTree[], int start, int end, int delta, int low, int high, int pos)
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
			lazyTree[(2*pos)+1] += lazyTree[pos];
			lazyTree[(2*pos)+2] += lazyTree[pos];
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
			lazyTree[(2*pos)+1] += delta;
			lazyTree[(2*pos)+2] += delta;
		}
		return;
	}

	// else PARTIAL OVERLAP
	// thus look both left and right side
	int mid=(low+high)/2;
	updateLazy(segmentTree, lazyTree, start, end, delta, low, mid, (2*pos)+1);
	updateLazy(segmentTree, lazyTree, start, end, delta, mid+1, high, (2*pos)+2);
	segmentTree[pos] = min(segmentTree[(2*pos)+1], segmentTree[(2*pos)+2]);
}


int query(int segmentTree[], int lazyTree[], int queryLow, int queryHigh, int low, int high, int pos)
{
	if(low>high){
		return LARGENUMBER;
	}

	// check if all propagation are done, same as above
	if(lazyTree[pos] != 0){
		segmentTree[pos] += lazyTree[pos];
		if(low!=high){
			// non leaf node
			lazyTree[(2*pos)+1] += lazyTree[pos];
			lazyTree[(2*pos)+2] += lazyTree[pos];
		}
		lazyTree[pos] = 0;
	}

	// now check overlap conditons
	// if NO OVERLAP
	if(queryLow>high or queryHigh<low){
		return LARGENUMBER;
	}

	// if COMPLETE OVERLAP
	if(queryLow<=low and queryHigh>=high){
		// current range is completely overlapped by query range
		return segmentTree[pos];
	}

	// else PARTIAL OVERLAP
	int mid = (low+high)/2;
	int sidea = query(segmentTree, lazyTree, queryLow, queryHigh, low, mid, (2*pos)+1);
	int sideb = query(segmentTree, lazyTree, queryLow, queryHigh, mid+1, high, (2*pos)+2);
	return min(sidea, sideb);
}

// build the binary segment tree - O(N)
void build(int node, int start, int end, int tree[], int A[])
{
    if(start == end){
        tree[node]=A[start];
    }
    else{
        int mid = (start+end)/2;
        //starting recursing down to the left child
        build(2*node, start, mid, tree, A);
        //once done, now recurse down the right child
        build((2*node)+1, mid+1, end, tree, A);
        //leaf nodes will be the element themselves, or you can say unit sized range
        //internal nodes will have min of both the left and right child, because it is RSQ
        tree[node] = min(tree[2*node], tree[(2*node)+1]);
    }
}

int main()
{
    int n,q; //array values and queries
    cin >> n >> q;
    int arr[n];
	int lazy[2*n +10];
	memset(lazy, 0, sizeof(lazy)); //initializing with zeroes
	//accepting values
    for(int i=1; i<=n; i++){
        cin >> arr[i];
    }
    int tree[2*n +10]; // extra just to be safe
    
	// build the tree
    build(1, 1, n, tree, arr);
	
    while(q--){
        char type;
        int x,y;
        cin >> type >> x >> y;
        if(type=='q'){
			int z = query(tree, lazy, x, y, 1, n, 1);
            cout << z << endl;
        }
        else if(type=='u'){
			int del;
			cin >> del;
            updateLazy(tree, lazy, x, y, del, 1, n, 1);
        }
    }
    return 0;
}

/*
Author: Amitrajit Bose
*/
