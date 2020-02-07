public class Solution {
    public boolean check(int A, int B, int[] C, int x){
        int segments = 1;
        int segmentSum = 0;
        for(int a: C){
            segmentSum += a;
            if(segmentSum > x){
                segments++;
                segmentSum = a;
            }
        }
        return (segments > A);
    }
    public int solve(int A, int B, int[] C) {
        if(C.length == 0) return 0;
        int low = Arrays.stream(C).max().getAsInt(); // min() of array
        int high = Arrays.stream(C).sum(); // sum of array
        int mid;
        while (low < high){
            mid = low + ((high-low)/2);
            if(check(A,B,C,mid)) low = mid+1; // maximising
            else high = mid; // overshot!
        }
        //return (low*B);
        return (int)((long)low*(long)B%10000003);
    }
    public int paint(int A, int B, int[] C) {
        return solve(A, B, C);
    }
}

