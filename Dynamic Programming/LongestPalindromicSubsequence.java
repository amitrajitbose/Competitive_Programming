class Solution {
    public int longestPalindromeSubseq(String s) {
        if (s==null)
            return 0;
        
        final int n = s.length();
        
        if (n<=1)
            return n;
        
        int dp[][] = new int[n][n];
        
        for(int i=0; i<n; i++)
            dp[i][i] = 1; // single length strings are always palindrome
        
        for(int curr=2; curr<=n; curr++) //size of current window
        {
            for(int i=0; i<n-curr+1; i++)
            {
                int j = curr + i - 1;
                if(s.charAt(i) == s.charAt(j))
                    dp[i][j] = dp[i+1][j-1] + 2;
                else
                    dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1]);
            }
        }
        return dp[0][n-1];
    }
}

