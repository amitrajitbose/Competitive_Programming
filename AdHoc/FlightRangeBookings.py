# LC 1109
class Solution:
    # @param bookings : list of list of integers
    # @param n : integer
    # @return a list of integers
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        mem = [0]*(n+2) 
        # first 0 will be ignored, because 1 based index, last 0 will be needed
        for item in bookings:
            mem[item[0]] += item[2]
            mem[item[1]+1] -= item[2]
        for i in range(2,n+1):
            mem[i] += mem[i-1]
        return mem[1:-1]

