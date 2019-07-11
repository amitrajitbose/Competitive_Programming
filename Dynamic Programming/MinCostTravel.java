/*
There are N stations in a route, from 0 to N-1. A train moves from
first station 0 to last station N-1, in only forward direction. The
cost of ticket between any two station is given. Find the
min cost to travel from station 0 to station N-1

cost[4][4] = {
    {0,10,75,94},
    {-1,0,35,50},
    {-1,-1,0,80},
    {-1,-1,-1,0}
};
*/


class Main {
  public static int findMinCost(int s, int d, int memo[][], int cost[][]){
    if (s==d)
      return 0; //nowhere to move
    if (s==d-1)
      return cost[s][d]; //take obvious path
    if (memo[s][d]!=0)
      return memo[s][d]; //memoized previously
    else{
      int mincost = cost[s][d];
      for(int i=s+1;i<d;i++)
      {
        //cost of going from s to i directly
        //then from i to d directly
        int temp = findMinCost(s,i,memo, cost) + findMinCost(i, d, memo, cost);

        mincost = Math.min(mincost, temp);
      }
      memo[s][d] = mincost;
      return memo[s][d];
    }
  }
  public static void main(String[] args) {
    int n = 4;
    int src = 0;
    int dest = 3;
    int[][] cost = {
      {0,10,75,94},
      {-1,0,35,50},
      {-1,-1,0,80},
      {-1,-1,-1,0}};
    int[][] memo = new int[4][4]; //cache
    int res = findMinCost(src, dest, memo, cost);
    System.out.println("\nMIN COST FROM "+src+" TO "+dest+" = "+res);
    System.out.println("---------------------------------------");
    dest = 2;
    res = findMinCost(src, dest, memo, cost);
    System.out.println("\nMIN COST FROM "+src+" TO "+dest+" = "+res);
    System.out.println("---------------------------------------");
  }
}