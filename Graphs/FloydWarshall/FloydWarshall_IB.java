public class Solution {
    public int[][] solve(int[][] A) {
        int i, j, k, n=A.length;
        final int INF = 999999;
        int B[][] = new int[n][n];
        for (i=0;i<n; i++){
            for (j=0;j<n;j++){
                if (A[i][j] == -1){
                    B[i][j] = INF;
                }
                else{
                    B[i][j] = A[i][j];
                }
            }
        }
        for (k=0;k<n;k++){
            for (i=0;i<n;i++){
                for (j=0;j<n;j++){
                    B[i][j] = Math.min(B[i][j], B[i][k] + B[k][j]);
                }
            }
        }
        for (i=0;i<n; i++){
            for (j=0;j<n;j++){
                if (B[i][j] == INF){
                    B[i][j] = -1;
                }
            }
        }
        return B;
    }
}

