
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
//Creating a two dimensional array of size n
createEmptyMap(int n){
    int **a;
    int i;
    a=(int **)calloc(n,sizeof(int*));
    for(i=0;i<n;i++){
        a[i]=(int *)calloc(n,sizeof(int));
    }
    return a;
}
//Print the two dimensional array
printMap(int **a,int n){
    int i,j;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }
}
//Modification of the map at epicentre (x,y) with intensity w
modify(int x,int y,int w,int **a,int n){
    int i,j,k;
    for(k=w-1;k>=0;k--){
        for(i=x-k;i<=x+k;i++){
            for(j=y-k;j<=y+k;j++){
                if(i>=0 && i<n && j>=0 && j<n){
                    a[i][j]+=1;
                }
            }
        }
    }
    return a;
}
//Return maximum value in the array
int max(int **a,int n){
    int max=a[0][0];
    int i,j;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(a[i][j]>max){
                max=a[i][j];
            }
        }
    }
    return max;
}
int main(){
    int n,m,mloop;
    int **a;
    scanf("%d",&n);
    a=createEmptyMap(n);
    printMap(a,n);
    scanf("%d",&m);//number of queries or number of active volcanoes
    for(mloop=0;mloop<m;mloop++){
        int x,y,w;
        scanf("%d %d %d",&x,&y,&w);
        a=modify(x,y,w,a,n);
        printMap(a,n);
    }
    printf("\n%d",max(a,n));
    getch();
    return 0;
}
