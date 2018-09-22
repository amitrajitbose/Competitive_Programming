n=int(input())
male=[0]*400
female=[0]*400
maxim=0
for i in range(n):
    a,b,c=[x for x in input().strip().split()]
    b=int(b)
    c=int(c)
    if a=='M':
        for j in range(b,c+1):
            male[j]+=1
    else:
        for j in range(b,c+1):
            female[j]+=1
for i in range(0,400):
    maxim=max(maxim,min(male[i],female[i]))

print(maxim)