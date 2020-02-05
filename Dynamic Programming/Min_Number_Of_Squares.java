//package com.ib;

public class MinNumberOfSquares {
    public int countMinSquares(int A) {
        if (A <= 3) return A;
        int[] dp = new int[A+1];
        for (int i=0; i<=3; i++){
            dp[i] = i;
        }
        for(int i=4; i<=A; i++){
            dp[i] = i; // only with 1+1+1+...i times
            for(int j=1; j <= Math.ceil(Math.sqrt(i)); j++){
                int temp = j * j;
                if (temp > i) break;
                else {
                    dp[i] = Math.min(dp[i], 1 + dp[i-temp]);
                }
            }
        }
        return dp[A];
    }
}

