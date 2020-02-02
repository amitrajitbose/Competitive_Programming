package com.ib;

public class MinStepsToReachEnd {
    public int solve(int[] A){
        if(A.length <= 1){
            return 0;
        }
        int ladder = A[0], stairs = A[0], jumps = 1;
        for(int level = 1; level < A.length; level++){
            if(level == A.length-1){
                return jumps;
            }
            if(level + A[level] > ladder){
                ladder = level + A[level]; // build up the ladder
            }
            stairs--; // move up the ladder
            if(stairs == 0) {
                jumps++;
                stairs = ladder - level;
            }
        }
        return jumps;
    }
}
