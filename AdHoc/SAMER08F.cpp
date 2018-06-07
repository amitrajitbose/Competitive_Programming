// http://www.spoj.com/problems/SAMER08F/

/*
This is the classical Feymann squares problem.
Let N be the size of the length of one side of square

For N=1,
One 1x1 square = 1

For N=2,
One 2x2 + Four 1x1 = 1+4 = 5

For N=3,
One 3x3 + Four 2x2 + Nine 1x1 = 1+4+9 = 14

For N=n
One nxn + Four (n-1)x(n-1) + ..... (n^2) (1x1)

So this follows n*(n+1)*(2n+1)/6
*/

#include <iostream>
using namespace std;
int feymannsquare(int n){
	return (n*(n+1)*((2*n)+1))/6;
}
int main(){
	int inp;
	cin>>inp;
	while(inp!=0){
		cout<<feymannsquare(inp)<<endl;
		cin>>inp;
	}
	return 0;
}