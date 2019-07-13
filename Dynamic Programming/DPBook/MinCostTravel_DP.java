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
  public static int findMinCost(int s, int d, int cost[][]){
    // Bottom Up DP
    int mincost[] = new int[d+1];
    mincost[s] = 0; //source to source
    mincost[s+1] = cost[s][s+1]; 
    for(int i=s+2; i<=d; i++)
    {
      mincost[i] = cost[0][i];
      for(int j=0; j<i; j++)
      {
        // intermediate station
        if(mincost[i] > mincost[j] + cost[j][i])
          mincost[i] = mincost[j] + cost[j][i];
      }
    }
    return mincost[d];
  }
  public static void main(String[] args) {
    int src = 0;
    int dest = 3;
    int[][] cost = {
      {0,10,75,94},
      {-1,0,35,50},
      {-1,-1,0,80},
      {-1,-1,-1,0}};
    int res = findMinCost(src, dest, cost);
    System.out.println("\nMIN COST FROM "+src+" TO "+dest+" = "+res);
    System.out.println("---------------------------------------");
    dest = 2;
    res = findMinCost(src, dest, cost);
    System.out.println("\nMIN COST FROM "+src+" TO "+dest+" = "+res);
    System.out.println("---------------------------------------");
  }
}

/*
Time = O(n^2)
Space = O(n)
*/