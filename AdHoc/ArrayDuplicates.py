# LC 442
class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        reps = []
        n = len(arr)
        for i in range(n):
            if arr[abs(arr[i])%n] > 0:
                arr[abs(arr[i])%n] = arr[abs(arr[i])%n] * -1
            else:
                reps.append(abs(arr[i]))
        return sorted(reps)

