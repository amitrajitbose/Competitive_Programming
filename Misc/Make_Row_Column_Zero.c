#include <stdlib.h>
#define N 3
#include <stdio.h>
#include <conio.h>
typedef struct index{
    int i;
    int j;
}index;
int main(){
    int i,j,k; //for loop variables
    int arr[N][N]={{1,2,3},{0,5,6},{7,8,0}};
    //Array before operation
    for(i=0;i<N;i++){
        for(j=0;j<N;j++){
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    //Array of struct
    index positions[N];
    k=0;
    for(i=0;i<N;i++){
        for(j=0;j<N;j++){
            if(arr[i][j]==0){
                positions[k].i=i;
                positions[k].j=j;
                k+=1;
            }
        }
    }
    for(i=0;i<k;i++){
        for(j=0;j<N;j++){
            arr[positions[i].i][j]=0;
            arr[j][positions[i].j]=0;
        }
    }
    printf("\n");
    //Array after operation
    for(i=0;i<N;i++){
        for(j=0;j<N;j++){
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    getch();
    return 0;
}
