/*
 * Approach: Segmented Tree
 * Range Sum Query (RSQ)
 */

#include <bits/stdc++.h>
using namespace std;

// build the binary tree - O(N)
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
		//internal nodes will have SUM of both the left and right child, because it is RSQ
		tree[node] = tree[2*node] + tree[(2*node)+1];
	}
}

// to update an element - O(log N)
// look at the interval in which the element is present
// recurse to the left or right accordingly
// here we are updating value at index 'id' by 'val'
void update(int node, int start, int end, int id, int val, int tree[], int A[])
{
	if(start == end){
		// indicating leaf node
		//A[id] += val;
		A[id] = val;
		//tree[node] += val; //when updating means adding to
		tree[node] = val; //if updating means changing/overwriting
	}
	else{
		int mid = (start+end)/2;
		if(start <= id and id <= mid){
			// so the element to be updated is in the left
			// recursively go down again
			update(2*node, start, mid, id, val, tree, A);
		}
		else{
			// so the element to be updated is in the right
			// recursively go down again
			update((2*node)+1, mid+1, end, id, val, tree, A);
		}
		// internal nodes will have SUM of both the left and right child, because it is RSQ
        tree[node] = tree[2*node] + tree[(2*node)+1];
	}
}

// to query a range, there are some conditions
/*
1) Range represented by a node is completely outside the given range
2) Range represented by a node is completely inside the given range
3) Range represented by a node is partially inside and partially outside the given range
*/

// in case of this problem RSQ, our query is to find the SUM of a range
int query(int node, int start, int end, int l, int r, int tree[])
{
	if(r<start or l>end){
		//query type 1
		/*
		{__query array__}.....[___seg tree___]
		or
		[___seg tree___].....{__query array__}
		*/
		return 0;
	}
	else if(l<=start and r>=end){
		//query type 2
		/*
		..{____query___[__seg tree__]___range___}..
		*/
		return tree[node];
	}
	else{
		//query type 3
		/*
		..{__[__}__]..
		or
		..[__{__]__}..
		*/
		int mid = (start+end)/2;
		int sidea = query(2*node, start, mid, l, r, tree);
		int sideb = query((2*node)+1, mid+1, end, l, r, tree);
		return (sidea + sideb);
	}
}

int main()
{
	int n,q;
	cin >> n >> q;
	int arr[n];
	for(int i=1; i<=n; i++){
		cin >> arr[i];
	}
	int tree[(2*n)+10]; // extra just to be safe
	// build the tree
	build(1, 1, n, tree, arr);
	while(q--){
		char type;
		int x,y;
		cin >> type >> x >> y;
		if(type=='q'){
			int z = query(1,1,n,x,y,tree);
			cout << z << endl;
		}
		else if(type=='u'){
			update(1,1,n,x,y,tree,arr);
		}
	}
	return 0;
}
/*
Author: Amitrajit Bose
*/
