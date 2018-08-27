/*
* Author: Amitrajit Bose
*
* Problem: N Queens Problem To Find All Possible Solutions
*
* Approach:
* Create a DDA, we call it 'board' and initialize it will 0 [NQSolve()]. We then put a 
* queen at position 0,0 and then continue putting one queen after the other in the 
* consecutive columns, such that all queens being placed are safe, and they cannot 
* be attacked by any other previously placed queens [isSafe()]. We keep doing the
* following recursively [solver()], until we find that we are unable to place all queens
* when we backtrack. So, in this case we are not applying a stack. Rather, we recursively
* backtrack for wrong placements.
*
* P.S: I have kept the algorithm clean from unnecessary inputs. I have declared inputs,
* using macro. You may modify the function for custom inputs.
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define N 8
int k=0;
int isSafe(int board[N][N], int row, int col)
{
    int i,j;
    for(i=0;i<col;i++){
        if(board[row][i])
            return 0; //same row thus not safe
    }
    for(i=row,j=col;i>=0 && j>=0;i--,j--){
        if(board[i][j])
            return 0; //upper left diagonal, thus not safe
    }
    for(i=row,j=col;i<N && j>=0;i++,j--){
        if(board[i][j])
            return 0; //lower left diagonal, thus not safe
    }
    //no need to check on the right side diagonal-wise
    //why? because we are proceeding column-wise: left to right
    return 1;
}
int print(int board[N][N],int k){
    printf("Solution %d-\n", k+1);
    int i,j;
    for (i = 0; i < N; i++)
    {
        for (j = 0; j < N; j++){
            printf(" %d ", board[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    return k+1;
}
bool solver(int board[N][N], int col){
    if(col>=N){
        //so all queens are already placed
        k=print(board,k);
        return 1; //job done
    }
    int i;
    bool flag=false;
    for(i=0;i<N;i++){
        if(isSafe(board,i,col)){
            board[i][col]=1;
            flag=solver(board,col+1) || flag;
            board[i][col] = 0; //backtracking because I am not getting other solutions
        }
    }
    return flag;
}

void NQSolve(){
    int board[N][N];
    int i,j;
    for(i=0;i<N;i++){
        for(j=0;j<N;j++){
            board[i][j]=0; //initializing the matrix
        }
    }
    if(solver(board,0)==false){
        printf("solutions Do Not Exist");
        return;
    }
    return;
}
int main()
{
    NQSolve();
    return 0;
}
