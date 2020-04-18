# cook your dish here
for _ in range(int(input())):
    x, k = map(int, input().strip().split())
    divisors = 0
    i = 2
    while i**2 <= x:
        if (x%i):
            i += 1
        else:
            while not (x%i):
                #print (x, i)
                divisors += 1
                x //= i
    if x > 1:
        divisors += 1 # because 1 is divisor for any number
    res = 1 if divisors >= k else 0
    print(res)
    #print(res, divisors)

