# LC 556 - M
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = [int(x) for x in list(str(n))]
        ln = len(digits)
        A = -1
        for i in range(ln-2, -1, -1):
            if digits[i] < digits[i+1]:
                A  = i
                break
        if A == -1:
            return A

        for i in range(ln-1, A, -1):
            if digits[i] > digits[A]:
                B = i
                break
        digits[A], digits[B] = digits[B], digits[A] # swap
        left = digits[: A + 1]
        right = sorted(digits[A + 1 :])
        digits = left + right
        str_digits = [str(x) for x in digits]
        m = int(''.join(str_digits))
        if m >= -(2**31) and m < (2**31)-1:
            return m
        else:
            return -1


