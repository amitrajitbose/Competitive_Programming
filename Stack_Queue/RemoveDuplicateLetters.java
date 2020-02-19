/*
 * Given a string A consisting of lowercase English alphabets. Find and return lexicographically smallest string B after removing duplicate letters from A so that every letter appears once and only once.
 */

public class Solution {
    public String solve(String A) {
        int n = A.length();
        
        Stack<Character> st = new Stack<>();
        HashMap<Character, Integer> rindex = new HashMap<>();
        
        for(int i=0; i<n; i++){
            rindex.put(A.charAt(i), i);
        }
        
        for(int i=0; i<n; i++){
            char c = A.charAt(i);
            if(st.search(c) == -1){
                // not in the stack presently
                while(!st.isEmpty() && st.peek() > c && rindex.get(st.peek()) > i){
                    st.pop();
                }
                st.push(c);
            }
        }
        //System.out.println(st);
        StringBuffer res = new StringBuffer("");
        while (!st.isEmpty()){
            res.insert(0, st.pop());
        }
        return res.toString();
    }
}

