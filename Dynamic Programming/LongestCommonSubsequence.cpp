//Explanation: https://www.geeksforgeeks.org/longest-common-subsequence/
/*
Youtube Tutorial: https://youtu.be/HgUOWB0StNE
Algorithm:
If characters match: LCS[i][j]=LCS[i-1][j-1]+1
If characters don't match: LCS[i][j]=max(LCS[i-1][j],LCS[i][j-1])

Complexity: O(m*n) where m and n are the lengths of the two strings/sequences
*/
#include <bits/stdc++.h>
using namespace std;
#define MAX 1000001
int lcs(char *A, char*B, int m, int n){
	int LCS[m+1][n+1];
	int i,j;
	//memset(LCS,0,sizeof(LCS)); //filling matrix with zeroes
	for(i=0;i<=m;i++){
		for(j=0;j<=n;j++){
		    if (i == 0 || j == 0)
                LCS[i][j] = 0;
			else if(A[i-1]==B[j-1]){
				LCS[i][j]=LCS[i-1][j-1]+1;
			}
			else
			{
				LCS[i][j]=max(LCS[i-1][j],LCS[i][j-1]);
			}
		}
	}
	return LCS[m][n];
}
int main(){
	char X[MAX];
	char Y[MAX];
	cin>>X;
	cin>>Y;
	cout<<lcs(X,Y,strlen(X),strlen(Y))<<endl;
	return 0;
}