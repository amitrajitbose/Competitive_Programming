/*
SPOJ-PALIN
Problem Name: The Next Palindrome

Approach: Mirroring of left hand side of the number.  Number is considered as a string.

@Interview Tags: Amazon, Yahoo

*/

#include <bits/stdc++.h>
using namespace std;

//This function is used to print any array
void printer(int a[],int n){
	for(int i=0;i<n;i++){
		cout<<a[i];
	}
}

//Function to check if all digits are character nine in a given range
int checkAllNine(int *num,int n){
	for (int i=0;i<n;i++){
		if(num[i]!=9)
			return 0;
	}
	return 1;
}

void nextPalin (int num[], int n )
{
    // find the index of mid digit
    int mid = n/2;
 
    // A bool variable to check if copy of left side to right is sufficient or not
    bool leftcopyenable = false;
 
    // end of left side is always 'mid -1'
    int i = mid - 1;
 
    // j will be pointing based on length of digit is even or odd
    int j = (n % 2 == 0)? mid : mid+1 ;
 
    while (i >= 0 && num[i] == num[j])
        i--,j++;
 
    if ( i < 0 || num[i] < num[j])
        leftcopyenable = true;
 
    while (i >= 0)
    {
        num[j] = num[i];
        j++;
        i--;
    }
 
    if (leftcopyenable == true)
    {
        int carry = 1;
        i = mid - 1;
 
        if (n%2 == 1)
        {
            num[mid] += carry;
            carry = num[mid] / 10;
            num[mid] %= 10;
            j = mid + 1;
        }
        else
            j = mid;

        while (i >= 0)
        {
            num[i] += carry;
            carry = num[i] / 10;
            num[i] %= 10;
            num[j++] = num[i--]; //left mirroring to right
        }
    }
}
 
// prints next palindrome of a given number num[] with n length.
void generateNextPalin( int num[], int n )
{
    int i;
    //When all the digits are 9, simply o/p 1
    // followed by n-1 0's followed by 1.
    if( checkAllNine( num, n ) )
    {
        printf( "1");
        for( i = 1; i < n; i++ )
            printf( "0" );
        printf( "1" );
    }
    else
    {
        nextPalin ( num, n );
 
        // print the result
        printer (num, n);
    }
}
int main() {
	int t;
	cin>>t;
	while(t--){
		int num[1000000];
		char input[1000000];
		scanf("%s",input);
		int n=strlen(input);
		//Converting string to number array
		for(int i=0;i<n;i++){
			num[i]=((int)input[i])-48;
		}
		generateNextPalin(num,n);
		cout<<endl;
	}
	return 0;
}