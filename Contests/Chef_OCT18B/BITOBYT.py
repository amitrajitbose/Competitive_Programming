'''
Author : @amitrajitbose
'''

def bytelandpopulation(n):
  n=n-1
  x=(n//26)
  remaining=n-(26*x)
  if(remaining>=10):
    p=[0,0,2**x]
  elif(remaining>=2):
    p=[0,2**x,0]
  else:
    p=[2**x,0,0]
  print(*p)

def main():
  t=int(input())
  for _ in range(t):
    num=int(input())
    bytelandpopulation(num)

if __name__=='__main__':
	main()
