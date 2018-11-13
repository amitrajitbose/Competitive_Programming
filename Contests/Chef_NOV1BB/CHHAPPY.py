# Author: @amitrajitbose
for test in range(int(input())):
  n=int(input().strip())
  arr=[int(x) for x in input().strip().split()]
  visited={}
  for i in arr:
      visited[i]=[0,0]
  
  flag=0
  for i in arr:
    x=arr[arr[i-1]-1]
    if(not visited[x][0]):
      visited[x][0]=1 #impacted
      visited[x][1]=i #impacted by
    elif(visited[x][0] and visited[x][1]!=i):
      flag=1
      break
  
  if(flag):
    print("Truly Happy")
  else:
    print("Poor Chef")

