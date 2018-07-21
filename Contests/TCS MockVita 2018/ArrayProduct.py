import functools
import operator
import itertools

def product(seq):
    """Product of a sequence."""
    return functools.reduce(operator.mul, seq, 1)

def checkConjugate(n,i,k):
	if(k==2):
		return ()

n,k=[int(x) for x in input().strip().split()]
arr=[int(x) for x in input().strip().split()]
factors=[1]
p=1
for i in arr:
	p=p*i

for i in range(2,p+1):
	if(p%i==0):
		factors.append(i)

cnt=0

