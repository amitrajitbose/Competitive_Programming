// https://leetcode.com/problems/subarray-product-less-than-k/
// import java.util.*;
class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int count = 0;
        int left = 0;
        int curr_prod = 1;
        for (int i=0; i<nums.length; i++)
        {
            //System.out.println(curr_prod+","+count);
            curr_prod *= nums[i];
            while (curr_prod >= k)
            {
                curr_prod /= nums[left];
                left += 1;
            }
            count += i - left + 1;
        }
        return count;
    }
}
