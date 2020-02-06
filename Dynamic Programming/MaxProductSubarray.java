public class Solution {
    // DO NOT MODIFY THE ARGUMENTS WITH "final" PREFIX. IT IS READ ONLY
    public int maxProduct(final int[] A) {
        int gmax = 0;
        int lmax = 0, lmin = 0;
        int n = A.length;
        if(n == 0){
            return 0;
        }
        if(n == 1){
            return Math.max(0, A[0]);
        }
        
        for(int i: A){
            //System.out.println(lmax + "," + lmin + "," + gmax);
            int lmax_copy = lmax;
            lmax = Math.max(i, Math.max(i*lmax, i*lmin));
            lmin = Math.min(i, Math.min(i*lmax_copy, i*lmin));
            gmax = Math.max(gmax, Math.max(lmax, lmin));
        }
        return gmax;
    }
}

/*
 * We need to take care of local max and local min because there can be negative numbers as well. When there is a negative 
 * number, it might be multiplied with local min to get an even larger positive number. So we need to maintain both the
 * maximum and minimum local variables.
 */
