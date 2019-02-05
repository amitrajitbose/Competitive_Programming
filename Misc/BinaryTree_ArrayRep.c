//Binary Tree SKM Sir Homework
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main(){
  int level;
  int i=0;
  printf("ENTER LEVELS: ");
  scanf("%d",&level);
  int n=pow(2,level)-1;
  int *a=(int *)malloc(n*sizeof(int));
  printf("ENTER ROOT: ");
  scanf("%d",&a[0]);
  int l=0;
  int k;
  while(l<level-1){
    for(k=0;k<pow(2,l);k++){
      printf("ENTER LEFT CHILD OF %d: ",a[i]);
      int left=(2*i)+1;
      int right=left+1;
      scanf("%d",&a[left]);
      printf("ENTER RIGHT CHILD OF %d: ",a[i]);
      scanf("%d",&a[right]);
      i++;
    }
    l++; 
  }
  for(k=0;k<n;k++){
    printf("%d ",a[k]);
  }
  getch();
  return 0;
}
