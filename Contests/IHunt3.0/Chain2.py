
# Amitrajit Bose
#this passed all test cases
t=int(input())
for _ in range(t):
    #test cases
    old=(str(input()))
    if(old[0]!='*'):
        print("Not Strong")
    else:
        new=old.replace("-*","")
        #print(new)
        while(new!=old):
            old=new
            new=old.replace("-*","")
            #print(new)
        if(len(new)==1 and new[0]=='*'):
            print("Strong")
        else:
            print("Not Strong")
