class Solution {
    public int maxSubArray(int[] nums) {
        // Kadane Algorithm
        int n = nums.length;
        int maxsum = Integer.MIN_VALUE;
        int local = 0;
        for(int i=0; i<n; i++)
        {
            local = Math.max(local+nums[i], nums[i]);
            maxsum = Math.max(maxsum, local);
        }
        return maxsum;
    }
}
