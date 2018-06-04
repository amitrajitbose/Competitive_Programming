print ("Hello")
n=input("Press")
print (n)
'''# https://practice.geeksforgeeks.org/problems/geeks-sum/0
#Fibo Seq Generator
def fibonacci(n):
    Fib=[]
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        Fib.append(0)
        return Fib
    elif n == 1:
        Fib.append(0)
        Fib.append(1)
        return Fib
    else:
        Fib.append(0)
        Fib.append(1)
        for i in range(2,n):
            c = a + b
            Fib.append(c)
            a = b
            b = c
        return Fib
        
primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
sum=0

t=int(input())
for _ in range(t):
    n=int(input())
    fiboarray=fibonacci(n)
    l=len(fiboarray)
    s=0
    for i in range(l):
        if(i in primes):
            s+=fiboarray[i]
    print(*fiboarray)
    print(s)'''