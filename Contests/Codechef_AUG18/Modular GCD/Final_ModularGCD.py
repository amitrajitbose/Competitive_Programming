def gcd(a, b): 
    if(a==0):
        return b
    return gcd(b%a,a)
  
T=int(input())    
for i in range(0,T):
    inp = list(map(int,input().split()))
    a=inp[0]
    b=inp[1]
    n=inp[2]
    diff=0
    if(a>b):
        diff=a-b
    else:
        diff=b-a
    if(a==b):
        print((pow(a,n,1000000007)+pow(b,n,1000000007))%1000000007)
    elif(n>=2):
        print(gcd(((pow(a,2)+pow(b,2))),diff))
    elif(n==1):
        print(gcd((a+b),diff))