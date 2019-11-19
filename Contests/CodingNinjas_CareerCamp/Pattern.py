'''
1234
1  4
1  4
1234
'''

#Write your code here
n = int(input())
for i in range(1,n+1):
    print(i,end="")
print("")
for i in range(2,n):
    print(1,end="")
    print(" "*(n-2),end="")
    print(n)
for i in range(1,n+1):
    print(i,end="")
print("")
