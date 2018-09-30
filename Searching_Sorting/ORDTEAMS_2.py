'''
ACM ICPC 2017 Online Prelim - Ordering Teams
Solution By : @IAmRiddhi
'''
def isComparable(a,b):
    eq = 0
    g1 = 0
    g2 = 0
    for i in range(3):
        if a[i]==b[i]:
            eq += 1
        elif a[i]>b[i]:
            g1 += 1
        else:
            g2 += 1
    return (g1>g2 and g2==0) or (g2>g1 and g1==0)
    
for T in range(int(input())):
    s1 = list(map(int,input().split()))    
    s2 = list(map(int,input().split()))
    s3 = list(map(int,input().split()))
    
    if isComparable(s1,s2) and isComparable(s2,s3) and isComparable(s1,s3):
        print("yes")
    else:
        print("no")