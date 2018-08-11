#include <bits/stdc++.h>
using namespace std;

int main()
{
	double principal = 0.0,rate = 0.0,emi=0.0;
	int n1,n2,t1,tenure;
	double principal1 = 0.0,principal2=0.0;

	cin>>principal;
	cin>>tenure;
	cin>>n1;


	for(int i=0;i<n1;i++)
	{
		cin>>t1>>rate;
		/*
		rate=rate/(12*100);
		emi=(principal*rate*pow(1+rate,t1))/(pow(1+rate,t1)-1);
		principal1 += emi;*/
		emi+=(principal*rate)/(1-1/(pow((1+rate),(t1*12))));


	}

	principal1+=emi;
	cin>>n2;
	emi=0.0;

	for(int i=0;i<n2;i++)
	{
		cin>>t1>>rate;
		/*rate=rate/(12*100);
		emi=(principal*rate*pow(1+rate,t1))/(pow(1+rate,t1)-1);
		principal2+= emi;*/
		emi+=(principal*rate)/(1-1/(pow((1+rate),(t1*12))));
	}

	principal2+=emi;

	if(principal1>principal2)
	{
		cout<<"Bank B"<<endl;
	}
	else
	{
		cout<<"Bank A"<<endl;
	}
	return 0;
}