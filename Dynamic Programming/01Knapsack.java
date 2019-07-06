/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    public static int knapsack(int n, int w, int val[], int wts[])
    {
        int dp[][] = new int[n+1][w+1]; //this will be our DP table
        for(int i=0; i<=n; i++)
        {
            for(int j=0; j<=w; j++)
            {
                if(j==0 || i==0)
                {
                    dp[i][j] = 0;
                }
                else if(wts[i-1]<=j)
                {
                    dp[i][j] = Math.max(dp[i-1][j-wts[i-1]]+val[i-1], dp[i-1][j]);
                }
                else
                {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        return dp[n][w];
    }
	public static void main (String[] args)throws IOException {
		//Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int tc = Integer.parseInt(br.readLine());
		//int tc = sc.nextInt();
		while(tc-- > 0)
		{
		    /*
		    // Scanner is slower than Buffered Reader ---- OMG!
		    int n,w;
		    n = sc.nextInt();
		    w = sc.nextInt();
		    int val[] = new int[n];
		    int wts[] = new int[n];
		    for(int i=0; i<n; i++)
		        val[i] = sc.nextInt();
		    for(int i=0; i<n; i++)
		        wts[i] = sc.nextInt();
		    System.out.println(knapsack(n,w,val,wts));
		    */
		    int n = Integer.parseInt(br.readLine().trim());
		    int capacity = Integer.parseInt(br.readLine().trim());
		    int[] p = new int[n], w = new int[n];
		    String[] a = br.readLine().trim().split(" ");
		    for(int i=0; i<n; i++) p[i] = Integer.parseInt(a[i]);
		    String[] b = br.readLine().trim().split(" ");
		    for(int i=0; i<n; i++) w[i] = Integer.parseInt(b[i]);
		    System.out.println(knapsack(n, capacity, p, w));
		}
	}
}
