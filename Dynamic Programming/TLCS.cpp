/* Codechef: https://www.codechef.com/problems/TLCS */
//Code is logically correct, but the question asks for top down approach which I am unable to do.
//I have computed bottom to up using two dimensional array to compare to sequences
#include<iostream>
#include<cstring>
#include<cstdlib>
#define MAX 1001
using namespace std;

void lcs( char *X, char *Y, int m, int n, int testcase )
{
int L[m+1][n+1];

for (int i=0; i<=m; i++)
{
	for (int j=0; j<=n; j++)
	{
	if (i == 0 || j == 0)
		L[i][j] = 0;
	else if (X[i-1] == Y[j-1])
		L[i][j] = L[i-1][j-1] + 1;
	else
		L[i][j] = max(L[i-1][j], L[i][j-1]);
	}
}

int index = L[m][n];
if(L[m][n]==1){
    cout<<"case "<<testcase<<" N"<<endl;
}
else{
    //Storing outputs in an array so that they are printed in reverse order
    //I'm finding the common sub-sequences from bottom to up
    char output[MAX][3];
    int outputi=0;
    cout<<"case "<<testcase<<" Y"<<endl<<L[m][n]<<endl;
    char lcs[index+1];
    lcs[index] = '\0'; // Set the terminating character
    
    // Start from the right-most-bottom-most corner and
    // one by one store characters in lcs[]
    int i = m, j = n;
    while (i > 0 && j > 0)
    {
    	// If current character in X[] and Y are same, then
    	// current character is part of LCS
    	if (X[i-1] == Y[j-1])
    	{
    		lcs[index-1] = X[i-1]; // Put current character in result
    		output[outputi][0]=X[i-1];
    		output[outputi][1]=char(i+48);
    		output[outputi][2]=char(j+48);
    		outputi++;
    		i--; j--; index--;	 // reduce values of i, j and index
    	}
    
    	// If not same, then find the larger of two and
    	// go in the direction of larger value
    	else if (L[i-1][j] > L[i][j-1])
    		i--;
    	else
    		j--;
    }
    
    for(i=outputi-1;i>=0;i--)
    {
        cout<<output[i][0]<<" "<<output[i][1]<<" "<<output[i][2]<<endl;
    }
    }
}

int main()
{
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++){
        char X[MAX];
        char Y[MAX];
        int m,n;
        cin>>m>>X;
        cin>>n>>Y;
        lcs(X, Y, m, n, tc);
    }
    return 0;
}
