from collections import defaultdict

n,m = list(map(int, input().strip().split()))
narr = list(map(int, input().strip().split()))
marr = list(map(int, input().strip().split()))

minm = min(marr)
minm_index = marr.index(minm)
maxn = max(narr)
maxn_index = narr.index(maxn)

register = defaultdict(int)

for i in range(n):
  val = minm + narr[i]
  if(register[val] == 0):
    register[val] += 1
    print('{0} {1}'.format(i,minm_index))
for i in range(m):
  val = maxn + marr[i]
  if(register[val] == 0):
    register[val] += 1
    print('{0} {1}'.format(maxn_index,i))
