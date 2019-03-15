n,m = list(map(int, input().strip().split()))
narr = list(map(int, input().strip().split()))
marr = list(map(int, input().strip().split()))

index = 0
na,ma = [], []
for i in narr:
	na.append((i,index))
	index += 1
index = 0
for i in marr:
	ma.append((i,index))
	index += 1
del narr,marr,index
sorted(na)
sorted(ma)
if(len(na)>1 and len(ma)>1):
  for i in na:
    print('{0} {1}'.format(i[1],ma[0][1]))
    print(i[0]+ma[0][0])

  for i in ma[:0:-1]:
    print('{0} {1}'.format(na[-1][1],i[1]))
    print(i[0]+na[-1][0])
elif(len(na)==1 and len(ma)>1):
  for i in ma:
    print('{0} {1}'.format(0,i[1]))
elif(len(na)>1 and len(ma)==1):
  for i in na:
    print('{0} {1}'.format(i[1],0))
elif(len(na)==1 and len(ma)==1):
  print('0 0')