# LC 735
class Solution:
    def collide(self, a: int, b:int) -> int:
        if abs(a) == abs(b):
            return None
        res = max(abs(a),abs(b))
        if abs(a) < abs(b):
            res *= (b // abs(b))
        else:
            res *= (a // abs(a))
        return res

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not len(asteroids):
            return asteroids
        stack = []
        for i in asteroids:
            if not stack:
                stack.append(i)
            else:
                if stack[-1] ^ i > 0:
                    stack.append(i) # no collision
                else:
                    curr = i
                    while stack and stack[-1] ^ curr < 0:
                        if stack[-1] < curr:
                            break
                        curr = self.collide(i, stack.pop(-1))
                        if not curr:
                            break
                    if curr:
                        stack.append(curr)
        return stack
        
