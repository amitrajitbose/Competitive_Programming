/*
Without any obstacles, total number of ways to go from top left to
bottom right.
*/
public static int numOfPathsRecurse(int m, int n){
	if (m == 0 && n == 0){ return 0; }
	if (m == 0 || n == 0){ return 1; }
	return numOfPathsRecurse(m-1, n) + numOfPathsRecurse(m, n-1);
}

public static int numOfPathsDP(int m, int n){
	int dp[m][n] = new int[m][n];
	int i,j;
	dp[0][0] = 0;
	for(i=1; i<m; i++)
		dp[i][0] = 1;
	for(j=1; j<n; j++)
		dp[0][j] = 1;
	for(i=1; i<m; i++)
		for(j=1; j<n; j++)
			dp[i][j] = dp[i-1][j] + dp[i][j-1];
	return dp[m-1][n-1];
}
/*
This time you are given a 2D matrix which has zeroes and ones.
Ones indicate blocked roads. Zeroes are open roads.
Find the total ways of going from top left to bottom right.

For example:
0 0 0
0 1 0
0 0 0
Has two possible paths
*/
public static int numOfPathsWithObstacles(int[][] arr){
	// inplace operation on dp
	int[][] dp = new int[arr.length][arr[0].length];
	int i,j;
	if(arr[0][0] == 0)
		dp[0][0] = 1; // start point
	for(i=1; i<m; i++){
		if(arr[i][0] == 0)
			dp[i][0] = dp[i-1][0]; // no obstacle
	}
	for(j=1; j<n; j++){
		if(arr[0][j] == 0)
			dp[0][j] = dp[0][j-1]; // no obstacle
	}
	for(i=1; i<m; i++)
		for(j=1; j<n; j++)
			if(arr[i][j] == 0)
				dp[i][j] = dp[i-1][j] + dp[i][j-1]; //no obstacle
	return dp[arr.length-1][arr[0].length-1];
}

/*
If diagonal movement is allowed, remember to also add dp[i-1][j-1] in
each movement
*/

