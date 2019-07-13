/*
Given a two dimensional matrix cost[][] of order M*N were
cost[i][j] represents the cost of passing through cell (i,j).
Total cost to reach a particular cell is the sum of costs of all
the cells in that path (including the starting and final cell). We
can only move either downward or rightward i.e if currently at (i,j)
we can go to (i,j+1) or (i+1,j)
Write a function to return the minimum cost of moving from the
top-left cell to the bottom right cell of the matrix.
*/

class Main {
  public static int mincostpath(int cost[][], int m, int n, int memo[][]){
    if (memo[m][n] != 0)
      return memo[m][n]; // cached result
    if (m==0 && n==0)
      memo[m][n] = cost[0][0];
    else if(m==0)
      memo[m][n] = mincostpath(cost, m, n-1, memo) + cost[0][n];
    else if(n==0)
      memo[m][n] = mincostpath(cost, m-1, n, memo) + cost[m][0];
    else
    {
      int x = mincostpath(cost, m-1, n, memo);
      int y = mincostpath(cost, m, n-1, memo);
      memo[m][n] = Math.min(x,y) + cost[m][n];
    }
    return memo[m][n];
  }
  public static void main(String[] args) {
    int m = 3;
    int n = 4;
    int[][] cost = {
      {1,3,5,8},
      {4,2,1,7},
      {4,3,2,3}
    };
    int [][] memo = new int[m][n];
    System.out.println("\nMinimum Path Cost="+mincostpath(cost, m-1, n-1, memo));
  }
}
/*
Time = O(n^2) [But many more functional calls]
Space = O(n^2)
*/