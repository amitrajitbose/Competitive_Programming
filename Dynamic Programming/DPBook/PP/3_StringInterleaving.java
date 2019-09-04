/*
String Interleaving Problem
DP Bottom Up Solution
O(n^2)
*/
class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int m = s1.length();
        int n = s2.length();
        if(s3.length() != m+n)
            return false;
        boolean[][] dp = new boolean[m+1][n+1];
        dp[0][0] = true;
        int i,j;
        //filling first row
        for(i=1;i<=m;i++){
            if(s1.charAt(i-1) != s3.charAt(i-1))
                dp[i][0] = false;
            else
                dp[i][0] = dp[i-1][0];
        }
        //filling first column
        for(j=1;j<=n;j++){
            if(s2.charAt(j-1) != s3.charAt(j-1))
                dp[0][j] = false;
            else
                dp[0][j] = dp[0][j-1];
        }
        //filling remaining
        for(i=1;i<=m;i++){
            for(j=1;j<=n;j++){
                //current char of s3 is as s1 but not s2
                if(s1.charAt(i-1)==s3.charAt(i+j-1) && s2.charAt(j-1)!=s3.charAt(i+j-1))
                    dp[i][j] = dp[i-1][j];
                //current char of s3 is as s2 but not s1
                else if(s1.charAt(i-1)!=s3.charAt(i+j-1) && s2.charAt(j-1)==s3.charAt(i+j-1))
                    dp[i][j] = dp[i][j-1];
                //current character of s3 is same as both
                else if(s1.charAt(i-1)==s3.charAt(i+j-1) && s2.charAt(j-1)==s3.charAt(i+j-1))
                    dp[i][j] = dp[i-1][j] || dp[i][j-1];
                else
                    dp[i][j] = false;
            }
        }
        return dp[m][n];
    }
}

/*
More Efficient Solution Below
Same Asymptotic Runtime As Above
*/

class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int m = s1.length();
        int n = s2.length();
        if(s3.length() != m+n)
            return false;
        boolean[][] dp = new boolean[m+1][n+1];
        dp[0][0] = true;
        int i,j;
        //filling first row
        for(i=1;i<=m;i++){
            if(s1.charAt(i-1) == s3.charAt(i-1) && dp[i-1][0])
                dp[i][0] = true;
        }
        //filling first column
        for(j=1;j<=n;j++){
            if(s2.charAt(j-1) == s3.charAt(j-1) && dp[0][j-1])
                dp[0][j] = true;
        }
        //filling remaining
        for(i=1;i<=m;i++){
            for(j=1;j<=n;j++){
                dp[i][j] = (dp[i-1][j] && s1.charAt(i-1) == s3.charAt(i+j-1)) || (dp[i][j-1] && s2.charAt(j-1) == s3.charAt(i+j-1));
            }
        }
        return dp[m][n];
    }
}
