#www.spoj.com/problems/WILLITST
n=int(input())
bin=str(bin(n))[2:]
ones=bin.count('1')
if(bin[0]=='1'  and ones==1):
    print("TAK")
else:
    print("NIE")