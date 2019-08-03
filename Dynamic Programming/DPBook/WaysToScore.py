"""
Consider a game where a player can score 3,5 or 10 points in one move.
Given a total score of N, find the total number of unique ways to reach a
score of N.

Understanding:
Let f(n) be the number of ways to score n
Then f(n) = f(n-10) + f(n-5) + f(n-3)
f(n) = 0 when n<0
f(n) = 1 when n=1
"""

def waysToScore(n):
    if(n<0):
        return 0
    if(n==0):
        return 1
    else:
        return waysToScore(n-10) + waysToScore(n-5) + waysToScore(n-3)

print(waysToScore(13))
"""
The above code is exponential and solves one subproblem multiple time.
We can cache them, lets do it.
"""
def ways_To_Score(n):
    cache = [None]*(n+1)
    cache[0] = 1

    def waysToScore(n):
        if cache[n] != None:
            return cache[n]
        if(n<0):
            return 0
        if(n==0):
            return cache[0]
        else:
            x = waysToScore(n-3) + waysToScore(n-5) + waysToScore(n-10)
            cache[n] = x
            return cache[n]
    return waysToScore(n)

print(ways_To_Score(13))

"""
Now we will write the bottom up DP version
"""
def waysToScoreDP(n):
    cache = [0]*(n+1)
    cache[0] = 1
    for i in range(1, n+1):
        if i-3 >= 0:
            cache[i] += cache[i-3]
        if i-5 >= 0:
            cache[i] += cache[i-5]
        if i-10 >= 0:
            cache[i] += cache[i-10]
    return cache[n]

print(waysToScoreDP(13))