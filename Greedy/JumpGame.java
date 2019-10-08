/*
Author : Amitrajit Bose
LCM55
*/
class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        int i = 0;
        int mx = 0;
        while (i < n && mx < n-1){
            mx = Math.max(mx, i + nums[i]);
            i++;
            if(i > mx) return false;
        }
        if (mx >= n-1) return true;
        return false;
    }
}
