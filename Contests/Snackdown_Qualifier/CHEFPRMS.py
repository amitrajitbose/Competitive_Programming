import math
def square(n):
    tmp=round(math.sqrt(n))
    if tmp*tmp==n:
        return False
    else:
        return True
def semprime(n): 
    ch = 0
    if square(n)==False:
        return False
    for i in range(2, int(math.sqrt(n)) + 1): 
        while n%i==0: 
            n//=i 
            ch+=1
        if ch >= 2:  
            break
    if(n > 1): 
        ch += 1
    return ch == 2
def check(n): 
    if semprime(n) == True: 
        return True
    else: 
        return False
for _ in range(int(input())):
    n=int(input())
    flag=0
    for i in range(2,n//2+1):
        if check(i)==True and check(n-i)==True:
            #print(i,n-i,square(i),square(n-i),"Yes")
            print("YES")
            flag=1
            break
    if flag==0:
        #print(i,n-i,square(i),square(n-i),"No")
        print("NO")
