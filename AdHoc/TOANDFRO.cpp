// http://www.spoj.com/problems/TOANDFRO/
#include <iostream>
#include <string.h>
#include <cmath>
using namespace std;
int main()
{
	int input;
	cin>>input;
	while(input!=0)
	{
		int blocksize=input;
		int k=-1;
		//Accepting string
		char str[200];
		cin>>str;
		//cout<<str<<endl;
		int len=strlen(str);
		int p=0; //points each character in string
		k=k+blocksize;
		int rows=ceil(len/blocksize);
		char matrix [rows][blocksize];
		int i=0;
		while(i<rows){
			for(int j=0;j<=k;j++){
				matrix[i][j]=str[p];
				//cout<<i<<" "<<j<<endl;
				p++;
			}
			i++;
			if(i==rows)
			{
				break;
			}
			for(int j=k;j>=0;j--){
				matrix[i][j]=str[p];
				//cout<<i<<" "<<j<<endl;
				p++;
			}
			i++;
		}

		/*
		//Matrix Printing
		
		for(int i=0;i<rows;i++){
			for(int j=0;j<blocksize;j++){
				cout<<matrix[i][j]<<" ";
			}
			cout<<endl;
		}
		*/
		for(int j=0;j<blocksize;j++){
			for(int i=0;i<rows;i++){
				cout<<matrix[i][j];
			}
		}
		cout<<endl;
		cin>>input; //next string block size
	}
	return 0;
}