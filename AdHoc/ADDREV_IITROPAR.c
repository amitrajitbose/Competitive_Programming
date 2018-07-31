#include <stdio.h>

int rev(int n){
	int sum=0;
	while(n>0){
		sum=(sum*10)+(n%10);
		n/=10;
	}
	return sum;
}
int main()
{
	/* code */
	int t;
	scanf("%d",&t);
	while(t--){
		int m,n,r;
		scanf("%d %d",&m,&n);
		r = rev(m) + rev(n);
		r = rev(r);
		printf("%d\n",r);
	}
	return 0;
}