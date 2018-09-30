'''
ACM ICPC 2017 Online Prelim - Ordering Teams
Algorithm:
1) Input
2) Sort them thrice based on each skill :: mysort()
3) check whether everything is sorted :: checksort()
4) check flags, whether each person is better than the other in atleast one skill :: checkflag()
5) If checksort()==True and checkflag()==True return Yes
'''
def mysort(arr):
  arr=sorted(arr, key=lambda x: x[0], reverse=True)
  arr=sorted(arr, key=lambda x: x[1], reverse=True)
  arr=sorted(arr, key=lambda x: x[2], reverse=True)
  return arr

def checksort(arr):
  flag=0
  for i in range(3):
    if((arr[0][i]>=arr[1][i]) and (arr[1][i]>=arr[2][i])):
      flag+=1
  if(flag==3):
    return True
  else:
    return False

def checkflag(arr):
  s1=sum(arr[0])
  s2=sum(arr[1])
  s3=sum(arr[2])
  if(s1==s2 or s2==s3):
    return False
  else:
    return True


def main():
  t=int(input())
  for _ in range(t):
    p1=[int(x) for x in input().strip().split()]
    p2=[int(x) for x in input().strip().split()]
    p3=[int(x) for x in input().strip().split()]
    team=[p1,p2,p3]
    team = mysort(team)
    if(checksort(team) and checkflag(team)):
      print("yes")
    else:
      print("no")


if __name__=='__main__':
  main()