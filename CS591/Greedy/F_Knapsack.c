#include <stdio.h>
#include <stdlib.h>
#define MAX 100
typedef struct itemtype
{
	int p,w;
	double r;
}item;

int cmpFunc(const void *a, const void *b)
{
	return ((*(item *)a).r < (*(item *)b).r);
}

int main()
{
	int capacity=20;
	int n=3;
	int i;
	double fracs[MAX];
	for(i=0;i<n;i++)
	{
		fracs[i]=0.0;
	}
	int profits[]={25,24,15};
	int weights[]={18,15,10};
	item items[MAX];
	for(i=0;i<n;i++)
	{
		items[i].p=profits[i];
		items[i].w=weights[i];
		items[i].r=(profits[i]*1.0/weights[i]);
	}
	qsort(items,n,sizeof(item),cmpFunc);
  
	//calculation begins here
	double curr=0; //current total profit is stored here
	for(i=0;i<n;i++)
	{
		if(capacity==0)
			break;
		else if(items[i].w<=capacity)
		{
			capacity-=items[i].w;
			fracs[i]=1.0;
			curr+=items[i].p;
		}
		else
		{
			//fractional
			fracs[i]=(capacity*1.0)/items[i].w;
			curr+=(fracs[i]*items[i].p);
			capacity=0;
		}
	}
	printf("TOTAL PROFIT: %f\n",curr);
	printf("FRACTIONS:-\nWGT\tPFT\tFRAC\n");
	for(i=0;i<n;i++)
	printf("%d\t%d\t%.2f\n",items[i].w,items[i].p,fracs[i]);
	printf("\n");

	return 0;
}