class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pre = [0] * (n + 1) # prefix sum
        for i,j,k in bookings:
            pre[i-1] += k
            pre[j] -= k
        for i in range(1, n+1):
            pre[i] += pre[i-1]
        pre.pop(-1)
        return pre
