'''
Author : @amitrajitbose
Problem : Codechef IPCTRAIN
Approach : Greedy
'''
t=int(input())
for _ in range(t):
  finalAnswer=0
  n,day=[int(x) for x in input().strip().split()]
  valf=[int(i) for i in range(day+1)]
  dt=[]
  si=[]
  for i in range(n):
    d,t,s=[int(x) for x in input().strip().split()]
    dt.append((d-1,t)) #day of arrival and lecture-plans
    si.append((s,i)) #sadnesses
  
  si=sorted(si) #sorting ascending, wrt day arrived

  for i in range(n-1,-1,-1):
    remaining=dt[si[i][1]][0]
    tmp=remaining

    j=0
    while(j<=day):
      if(tmp > valf[tmp]):
        j+=1
        tmp = valf[tmp]
      else:
        j=day+1
    
    j=0
    while(j<=day):
      if(tmp != valf[tmp]):
        j+=1
        tmp = valf[tmp]
      else:
        j=day+1
    
    training=dt[si[i][1]][1]
    while(day>tmp):
      training -= 1
      valf[tmp] = remaining
      tmp += 1
      if(training <= 0):
        break
      
      j=0
      while(j<=day):
        if(tmp > valf[tmp]):
          tmp=valf[tmp]
          j+=1
        else:
          j=day+1
      
      j=0
      while(j<=day):
        if(tmp != valf[tmp]):
          j+=1
          tmp = valf[tmp]
        else:
          j=day+1
    valf[remaining] = tmp
    finalAnswer += (training*si[i][0])
  print(finalAnswer)