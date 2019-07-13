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

/*
Follow Up
---------
What if we are also allowed to move in diagonally lower right direction
as well?
*/

class Main {
  public static int mincostpath(int cost[][], int m, int n){
    int [][] dp = new int [m+1][n+1];
    dp[0][0] = cost[0][0];
    // Top Row
    for(int j=1; j<=n; j++)
      dp[0][j] = dp[0][j-1] + cost[0][j];
    // Leftmost Column
    for(int i=1; i<=m; i++)
      dp[i][0] = dp[i-1][0] + cost[i][0];
    // Other cells
    for(int i=1; i<=m; i++)
      for(int j=1; j<=n; j++)
        dp[i][j] = Math.min(dp[i-1][j-1], Math.min(dp[i][j-1], dp[i-1][j])) + cost[i][j];
    
    return dp[m][n];
  }
  public static void main(String[] args) {
    int m = 3;
    int n = 4;
    int[][] cost = {
      {1,3,5,8},
      {4,2,1,7},
      {4,3,2,3}
    };
    System.out.println("\nMinimum Path Cost="+mincostpath(cost, m-1, n-1));
  }
}
/*
Time = O(n^2)
Space = O(n^2)
*/