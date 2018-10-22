def gettime(x):
    ans=2
    for i in range(1,len(x)):
        if x[i]=='j' or x[i]=='k':
            if x[i-1]=='d' or x[i-1]=='f':
                ans+=2
            else:
                ans+=4
        else:
            if x[i-1]=='j' or x[i-1]=='k':
                ans+=2
            else:
                ans+=4
    return ans
for _ in range(int(input())):
    ar=[]
    count=[]
    n=int(input())
    for i in range(n):
        x=input()
        if x in ar:
            count[ar.index(x)]+=1
        else:
            ar.append(x)
            count.append(1)
    #print(ar)
    #print(count)
    total=0
    for i in range(len(ar)):
        ans=gettime(ar[i])
        #print(ans)
        c=((count[i]-1)/2)+1
        total+=ans*c
    print(int(total))
