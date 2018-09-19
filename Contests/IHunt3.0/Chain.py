#this is partially correct
def check(s):
    l=len(s)
    #if it does not start with *
    if(s[0]!=42 or l<1):
        return 0
    #if contains only *
    if(l==1 and s[0]==42):
        return 1
    #if starts with **
    if(s[0]==42 and s[1]==42):
        return 0
    if(l>2):
        for i in range(0,l-2):
            #if contains a substring ***
            if(s[i]==42 and s[i+1]==42 and s[i+2]==42):
                return 0
        #if ends with --*
        if(s[-3]==45 and s[-2]==45 and s[-1]==42):
            return 0
        return 1
    else:
        return 1

t=int(input())
for _ in range(t):
    #test cases
    inp=list(str(input()))
    s=[ord(x) for x in inp]
    #print(s)
    #45 = -
    #42 = *
    stars=s.count(42)
    dashes=s.count(45)
    if(check(s) and dashes==stars-1):
        print("Strong")
    else:
        print("Not Strong")

'''
[42, 45, 42, 45, 42, 45, 42, 45, 42, 45, 42]
[42, 45, 45, 45, 42, 45, 45, 42, 42, 42]
[42, 42, 45, 42, 42, 45, 42, 45, 45, 45, 42, 42, 45, 42, 45, 45, 42, 45, 45, 42, 42]
[42, 45, 42, 42, 42, 42, 45, 42, 45, 42, 42, 45, 42, 45, 45, 42, 45, 42, 42, 45, 45, 42, 45, 42, 42, 45, 42, 45, 42, 45, 45, 42, 42, 42, 45, 42, 42, 45, 45, 42, 42, 42, 45, 45, 42, 42, 45, 42, 45, 42, 45, 42, 45, 42, 45, 45, 45, 42, 45, 42, 45, 42, 42, 45, 42]
[42, 45, 42, 45, 42, 42, 45, 45, 45, 45, 42, 45, 45, 45, 45, 45, 42, 45, 42, 45, 42, 45, 42, 45, 42, 45, 42, 42, 45, 42, 42, 45, 42, 42, 42, 45, 42, 45, 42, 45, 45, 42, 42, 42, 42, 45]
[42]
[42, 42]
[42, 45, 45, 42]
[42, 45, 42]
'''