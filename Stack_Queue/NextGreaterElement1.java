class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        if (nums1.length<=0 || nums2.length <= 0){
            return new int[0];
        }
        Deque<Integer> st = new ArrayDeque<>(); //stack
        Map<Integer, Integer> map = new HashMap<>(); //solution set
        st.push(0); // first index
        
        for (int i=1; i<nums2.length; i++){
            while(!st.isEmpty() && nums2[st.peek()] < nums2[i]){
                int popped = st.pop();
                map.put(nums2[popped], nums2[i]);
            }
            st.push(i);
        }
        while(!st.isEmpty()){
            int popped = st.pop();
            map.put(nums2[popped],-1);
        }
        for(int i=0; i<nums1.length; i++){
            nums1[i] = map.get(nums1[i]);
        }
        return nums1;
    }
}
// LC 496 - M
