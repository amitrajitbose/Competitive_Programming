class Solution:
    def trap(self, height: List[int]) -> int:
        return self.trap2(height)
        
    def trap1(self, height: List[int]) -> int:
        # TWO TRAVERSALS
        if len(height) == 0:
            return 0
        left = [height[0]]
        for i in range(1, len(height)):
            left.append(max(left[-1], height[i]))
        right = [height[-1]]
        for i in range(len(height)-2, -1, -1):
            right.insert(0, max(right[0], height[i]))
        ans = 0
        for i in range(len(height)):
            ans += min(left[i], right[i]) - height[i]
        return ans
    
    def trap2(self, height: List[int]) -> int:
        # ONE TRAVERSAL - TWO POINTERS
        ans = 0
        left = 0
        right = len(height)-1
        leftmax = rightmax = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftmax:
                    leftmax = height[left]
                else:
                    ans += leftmax - height[left]
                left += 1
            else:
                if height[right] >= rightmax:
                    rightmax = height[right]
                else:
                    ans += rightmax - height[right]
                right -= 1
        return ans
