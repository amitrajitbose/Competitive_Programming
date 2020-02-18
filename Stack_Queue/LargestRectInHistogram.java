public class Solution {
    public int largestRectangleArea(int[] A) {
        
        Stack<Integer> st = new Stack<>();
        int maxarea = 0;
        int n = A.length;
        int lastElementIdx;
        
        if(n == 0) return 0;
        if(n == 1) return A[0];
        
        for (int i=0; i<n; i++){
            // System.out.println(st);
            while (!st.isEmpty() && A[st.peek()] > A[i]){
                lastElementIdx = st.pop();
                maxarea = Math.max(maxarea, A[lastElementIdx]*(i-(st.isEmpty() ? -1 : st.peek())-1));
            }
            st.push(i);
        }
        // since all elements have been processed
        // checking if the stack is empty or any unprocessed element is left
        while(!st.isEmpty()){
            lastElementIdx = st.pop();
            maxarea = Math.max(maxarea, A[lastElementIdx]*(n-(st.isEmpty() ? -1 : st.peek())-1));
        }
        return maxarea;
    }
}

