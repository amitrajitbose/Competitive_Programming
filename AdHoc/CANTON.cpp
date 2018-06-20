/*
Author: Amitrajit Bose
Problem: https://www.spoj.com/problems/CANTON/
Approach: There are basically four elementary types of movements

Move A: Move horizontally right one time (j++) when i=1
Move B: Move diagonally downwards repeat:(i++,j--) until j=1
Move C: Move vertically down one time (i++) when j=1
Move D: Move diagonally upwards repeat:(i--,j++) until i=1

We keep repeating the moves until we reach the target element
*/

#include <iostream>
#define test ll t; cin>>t; while(t--)
typedef long long ll;
using namespace std;
int main()
{
	test
	{
		ll targetterm;
		ll term=1;
		ll i=1;
		ll j=1;
		cin>>targetterm;
		while(term<targetterm)
		{
			//Move A
			j++;
			term++;
			//cout<<i<<"A/"<<j<<endl;
			if(term==targetterm){
				break;
			}

			//Move B
			while(j>1 && term<targetterm){
				i++;
				j--;
				term++;
				//cout<<i<<"B/"<<j<<endl;
			}
			if(term==targetterm){
				break;
			}

			//Move C
			i++;
			term++;
			//cout<<i<<"C/"<<j<<endl;
			if(term==targetterm){
				break;
			}

			//Move D
			while(i>1 && term<targetterm){
				j++;
				i--;
				term++;
				//cout<<i<<"D/"<<j<<endl;
			}
			if(term==targetterm){
				break;
			}
		}
		cout<<"TERM "<<targetterm<<" IS "<<i<<"/"<<j<<endl;
	}
	return 0;
}