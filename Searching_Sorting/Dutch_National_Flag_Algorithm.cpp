/*
 * Given an array A[] consisting 0s, 1s and 2s, write a function that sorts A[]. 
 * The functions should put all 0s first, then all 1s and all 2s in last.
 * Approach: Dutch National Flag Algorithm
 * Complexity: O(n)
 * Basically check the mid element of the array every time and place it/swap it with
 * element on the left half or right half. Thus, you have to only swap for two category
 * of colors only, for example swap only for 0 and 2. Thus 1 will automatically be sorted
 * and end up in the middle region of the sorted array.
 *
 * For More: http://users.monash.edu/~lloyd/tildeAlgDS/Sort/Flag/
 * 
 * Asked In: Adobe Amazon Hike MAQ Software Microsoft Morgan Stanley 
 * 	     Ola Cabs OYO Rooms Paytm SAP Labs Walmart Yatra.com
 */

#include <bits/stdc++.h>
using namespace std;
void swap(int *a, int *b){
    int temp=*a;
    *a=*b;
    *b=temp;
}
void dutchFlag(int arr[], int size){
    int low=0;
    int high=size-1;
    int mid=0;
    while(mid<=high){
        if(arr[mid]==0){
	    swap(&arr[low],&arr[mid]);
	    low++;
	    mid++;
	}
	else if(arr[mid]==2){
	    swap(&arr[mid],&arr[high]);
	    //mid++; what if 2 is swapped with 2 itself; thus dont move the mid ptr here.
	    high--;
	}
	else if(arr[mid]==1){
	    //no need to swap
	    mid++;
	}
    }
}
int main(){
	int a[]={0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1, 0, 2 ,2 ,1 ,0 ,2 ,1 };
	int n = sizeof(a)/sizeof(a[0]);
	dutchFlag(a,n);
	//dutchFlag(a,n);
	for(int i=0;i<n;i++){
	    cout<<a[i]<<" ";
	}
	cout<<endl;
	return 0;
}
