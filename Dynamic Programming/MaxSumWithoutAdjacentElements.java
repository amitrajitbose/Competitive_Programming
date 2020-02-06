public class Solution {
    public int adjacent(int[][] A) {
        ArrayList<Integer> arr = new ArrayList<>();
        // *** Problem Conversion Concept ***
        // We'll never pick the lower value for corresponding location, we want to maximise
        // Because as we pick one we will not be able to pick its neighbours
        for(int i=0; i<A[0].length; i++){
            arr.add(Math.max(A[0][i], A[1][i]));
        }
        int n = arr.size();
        int[] dp = new int[n + 1];
        // This part below would be same as Stickler Thief problem.
        if(n == 0) return 0;
        if(n == 1) return arr.get(0);
        if(n == 2) return Math.max(arr.get(0), arr.get(1));
        
        dp[0] = arr.get(0);
        dp[1] = Math.max(arr.get(0), arr.get(1));
        
        for(int i=2; i<n; i++){
            dp[i] += Math.max(dp[i-2] + arr.get(i), dp[i-1]);
        }
        return dp[n-1];
    }
}

