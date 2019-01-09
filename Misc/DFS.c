#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include <stdbool.h>

char stack[20];
int top=-1, n;
char arr[20];
char dfs(int );
char ajMat[20][20];
char b[20];
void display();
int p=0;
int i,j;

int main()
{
    char v;
    int l=0;
    printf("Enter the number of nodes in a graph");
    scanf("%d",&n);
    printf("Enter the value of node of graph");
    for(i=0;i<n;i++)
    {
        scanf("%s",&b[i]);
    }
    char k=b[0];
    printf("Enter the value in adjancency matrix in from of 'Y' or 'N'\n");
    printf("\nIf there is an edge between the two vertices then enter 'Y' or 'N'\n");
    for(i=0; i<n; i++)
        printf(" %c ",b[i]);
    for(i=0;i<n; i++)
    {
         printf("\n%c ",b[i]);
         for(j=0; j<n; j++)
         {
              printf("%c ",v=getch());
              ajMat[i][j]=v;
         }
         printf("\n\n");
    }
    for(i=0;i<n;i++)
    {
         l=0;
         while(k!=b[l])
         l++;
         k=dfs(l);
    }
    display();
    getch();
}

void display()
{
     printf(" DFS of Graph : ");
     for(i=0; i<n; i++)
     printf("%c ",arr[i]);
}
void push(char val)
{
     top=top+1;
     stack[top]=val;
}
char pop()
{
     return stack[top];
}

bool unVisit(char val)
{
      for(i=0; i<p; i++)
      if(val==arr[i])
        return false;
      for(i=0; i<=top; i++)
        if(val==stack[top])
            return false;
        return true;
}

char dfs(int i)
{
     int k;
     char m;
     if(top==-1)
     {
          push(b[i]);
     }
     m=pop();
     top--;
     arr[p]=m;
     p++;
     for(j=0; j<n; j++)
     {
          if(ajMat[i][j]=='y')
          {
               if(unVisit(b[j]))
               {
                     push(b[j]);
               }
          }
     }
    return stack[top];
}
