class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return 0
        binary = bin(num)[3:]
        return len(binary) + binary.count('1') + 1
