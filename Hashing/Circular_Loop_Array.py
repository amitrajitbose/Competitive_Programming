class Solution:
    def getNext(self, arr, idx):
        return (idx + nums[idx]) % len(nums)
    
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = {}
        def visit(idx):
            if idx in visited and visited[idx] == 1 :
                return True
            elif idx in visited and visited[idx] == 2 :
                return False
            else:
                visited[idx] = 1 #visiting first time
                nidx = self.getNext(nums, idx)
                if(nums[idx]*nums[nidx]>0 and nidx!=idx and visit(nidx)):
                    return True
                visited[idx] = 2
                return False

        return any(visit(i) for i in range(len(nums)))