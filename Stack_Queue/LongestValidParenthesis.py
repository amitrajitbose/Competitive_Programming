class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]
        maxlen = 0
        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            else:
                st.pop(-1)
                if not st:
                    st.append(i)
                else:
                    maxlen = max(maxlen, i-st[-1])
        return maxlen
