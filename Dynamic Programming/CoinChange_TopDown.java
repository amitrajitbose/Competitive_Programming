//Coin Change Problem 
//Using Dynamic Programming Top Down
class Main {
  static int mc(int c)
    {
      int dp[] = new int[c+1];
      for(int i=1;i<=c;i++)
      {
        dp[i]=-1; //initialise all dp elements
      }
      // dp[0] left uninitialized to 0
      //because we need 0 coins to make 0 change
      return mc(c, dp);
    }
    static int mc(int c, int[] dp){
      if(dp[c]>=0)
        return dp[c]; //already precomputed
      int minCoin = Integer.MAX_VALUE;
      int coins[] = {10,6,1};
      //System.out.println(minCoin); //debug
      for (int i : coins){
        if(c-i >= 0){
          int currMinCoin = mc(c-i, dp);
          if(currMinCoin < minCoin){
            minCoin=currMinCoin;
          }
        }
      }
      dp[c] = minCoin+1;
      return dp[c];
    }
  public static void main(String args[]) {
    //taking a static currency array
    System.out.println(mc(18000));
  }
}