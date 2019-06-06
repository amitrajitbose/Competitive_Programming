#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
int compute(int i, int j)
{
  int temp;
  int count=0;
  temp=max(i,j);
  j=min(i,j);
  i=temp;
  while(j!=0)
  {
    if(i==1 or j==1)
    {
      count+=max(i,j);
      break;
    }
    else if(i==j)
    {
      count+=1;
      break;
    }
    else
    {
      count+=(int)(i/j);
      i=i%j;
      temp=max(i,j);
      j=min(i,j);
      i=temp;
    }
  }
  return count;
}
int main()
{
int m,n,p,q,a,b,i,j,tmp,ta;
cin>>m;
cin>>n;
cin>>p;
cin>>q;

int sheitotal=0;
for(i=m;i<=n;i++)
{
  for(j=p;j<=q;j++)
  {
    sheitotal+=compute(i,j);
  }
}
cout<<sheitotal<<endl;
return 0;
}