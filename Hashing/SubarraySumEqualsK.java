import java.util.*;
class Solution {
    public int subarraySum(int[] arr, int k) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        int cnt = 0;
        int cs = 0; //current sum
        
        for (int i=0; i<arr.length; i++)
        {
            cs += arr[i];
            if (cs == k)
            {
                cnt += 1;
            }
            if (hm.containsKey(cs-k))
            {
                cnt += hm.get(cs-k);
            }
            if (hm.containsKey(cs))
            {
                hm.put(cs, hm.get(cs)+1);
            }
            else
            {
                hm.put(cs, 1);
            }
        }
        return cnt;
    }
}

