public class Solution {
    public int longestValidParentheses(String A) {
        Deque<Integer> st = new ArrayDeque<>();
        st.push(-1);
        int n = A.length();
        int maxlen = 0;
        for(int i=0; i<n; i++){
            if(A.charAt(i)=='('){
                st.push(i);
            }
            else{
                st.pop();
                if(!st.isEmpty())
                    maxlen = Math.max(maxlen, i - st.peek());
                else
                    st.push(i);
            }
        }
        return maxlen;
    }
}

