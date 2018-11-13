# Author: @amitrajitbose
from fractions import Fraction as F
inp=[int(x) for x in input().strip().split()]
t=inp[0]
table=[0,0.5,0.25]
for i in range(3,30):
  if(i%2):
    x=table[i-1]+(1/(2**i))
  else:
    x=table[i-2]+(1/(2**i))
  table.append(x)
  #print(i,x)

for _ in range(t-1):
  n=inp[_+1]
  x=F(table[n]).numerator
  y=F(table[n]).denominator
  #print(F(table[n]))
  print(x,end=" ")
  print(y,end=" ")
n=inp[-1]
x=F(table[n]).numerator
y=F(table[n]).denominator
#print(F(table[n]))
print(x,end=" ")
print(y)

