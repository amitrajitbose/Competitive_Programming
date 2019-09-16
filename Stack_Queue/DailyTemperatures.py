# LCM739
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        res = [0] * n
        st = [0]
        for i in range(1,n):
            while st and T[st[-1]] < T[i]:
                x = st.pop(-1)
                res[x] = i - x
            st.append(i)
        return res
