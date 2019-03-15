for testcase in range(int(input())):
  n,p = list(map(int, input().strip().split()))
  i = 0
  i = (n//2)+1
  x = n%i
  count = 0
  if(n==p):
    for j in range(x+1,p+1):
      y = x%j
      for k in range(y+1,p+1):
        count += 1
        #print((i,j,k),(n%i%j%k%n))
    print(count)
  elif(p>n):
    oldi = i
    count = 0

    for j in range(x+1,p+1):
      y = x%j
      for k in range(y+1,p+1):
        count += 1
        print((i,j,k),(n%i%j%k%n))
    #print("x")
    for i in (n+1,p):
      x=n%i
      for j in range(x+1,p+1):
        k = (n//2)+1
        count+=1
        print((i,j,k),(n%i%j%k%n))
    for i in (n+1,p):
      x=n%i
      for k in range(x+1,p+1):
        j = (n//2)+1
        count+=1
        print((i,j,k),(n%i%j%k%n))
    print(count)
  #print("------------")