/*
 * Given an array of only three possible elements - 0,1,2. Sort the array. Use minimal possible time and operations.
 * Approach: Hash
 * Author: Amitrajit Bose
 */

#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	while(t--){
	    int n;
	    cin >> n;
	    int b[3]={0,0,0};
	    int num;
	    for(int i=0;i<n;i++){
	        cin >> num;
	        b[num%3]+=1;
	    }
	    for(int i=0;i<3;i++){
	        //cout << b[i];
	        while(b[i]!=0){
	            cout << i << " ";
	            b[i]-=1;
	        }
	    }
	    cout<<endl;
	}
	return 0;
}
