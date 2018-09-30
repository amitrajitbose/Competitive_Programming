//Problem Link: https://www.codechef.com/AUG18B/problems/PROBLEMS
#include <bits/stdc++.h>
using namespace std;

#define for(i,a,b) for(i=a;i<=b;i++)

struct prob{
	int a,b;
};

bool comparer(prob one, prob two){
	return (one.a < two.a);
}

bool modifiedComparer(prob one, prob two){
	if(one.a != two.a)
		return (one.a < two.a);
	else
		return (one.b < two.b);
}

int main(){
	int p,s,i,j,pindex; //p=problem count, s=subtask count
	cin >> p >> s;
	prob arr1[p]; //for all problems
	prob arr2[s]; //for all subtasks of a single problem
	for(pindex,1,p){
		arr1[pindex-1].b=pindex;
		for(j,0,s-1){
			cin >> arr2[j].a; //denotes SC_j
		}
		for(j,0,s-1){
			cin >> arr2[j].b; //denotes NS_j
		}
		//now sort arr2 based on the scores SC
		sort(arr2,arr2+s,comparer);
		int count=0; //counts the constraint
		for(j,0,s-2){
			if(arr2[j].b > arr2[j+1].b)
				count++;
		}
		arr1[pindex-1].a=count;
	}
	sort(arr1,arr1+p,comparer);
	sort(arr1,arr1+p,modifiedComparer);
	for(i,0,p-1){
		cout << arr1[i].b << endl;
	}
	return 0;
}