"""
Given two strings X and Y of same length of lowercase english letters.
You want to change X to Y.
Changing ith character of X to ith char of Y costs abs(X[i] - Y[i]), i.e
the absolute difference between the ascii values

You are also given a total cost of K
Determine the maximum length of a substring of X that can be changed
to the corresponding substring Y within the given cost.

Example:

Input

6
abcdek
bcdefx
3
4
5
20

Output

4
5
6
"""

def max_length_subarray(arr: list, k: int) -> int:
    # return the maximum length subarray of sum <= k
    start, end = 0, 0
    currsum, maxlen = 0, 0
    for i in arr:
        currsum += i
        end += 1
        while currsum > k:
            currsum -= arr[start]
            start += 1
        if currsum <= k:
            maxlen = max(maxlen, end-start)
    return maxlen

def solve(X,Y,N,K):
    diff = []
    for i in range(N):
        diff.append(abs(ord(X[i]) - ord(Y[i])))
    return max_length_subarray(diff, K)

def main():
    N = int(input())
    X = input()
    Y = input()
    T = int(input())
    for i in range(T):
        K = int(input())
        res = solve(X,Y,N,K)
        print(res)
main()