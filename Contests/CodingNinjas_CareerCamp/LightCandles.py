n,d = [int(x) for x in input().strip().split()]
arr = [int(x) for x in input().strip().split()]
i = 0
cnt = 0
last = 0
while i < n:
    if arr[i] == 1:
        last = i
    if i-last==d:
        cnt += 1
        last=i
    i += 1
        
print(cnt)

"""
There are N candle stands placed in a room, from left to right and one next to each other.
Some stands have candles on them, whereas some stands are empty. All the candles are burning and have flame on them.
Flames of candles are covered in such a way that flame can spread brightness only in right direction.
Light emitted from flame of a candle can brighten the area of at most D-1 stands.
What is the minimal amount of new and burning candles to be placed on the empty stands so that all the empty candle stands are brightened?
Note: The first candle stand would always have a burning candle.

----------------

4 1
1 0 1 1
= 1

----------------

5 2
1 0 0 0 1
= 1

----------------

"""