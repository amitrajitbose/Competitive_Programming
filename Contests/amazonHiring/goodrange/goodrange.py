from bisect import insort
n,m = [int(x) for x in input().strip().split()]
pre = [(0,0) for i in range(n+1)]
sortedkeys = []
res = [] # Stores all the results
previous_sum = 0
for _ in range(m):
    print(pre)
    x = int(input())
    insort(sortedkeys, x)
    if(len(sortedkeys)<=1):
        previous_sum += (1+n)
        pre[x] = (1,n)
        res.append(previous_sum)
    elif(len(sortedkeys)==2):
        if(sortedkeys.index(x)==0):
            # Inserted in first position
            previous_sum -= sum(pre[sortedkeys[1]])
            pre[x] = (1, sortedkeys[1]-1)
            pre[sortedkeys[1]] = (x+1, n)
            previous_sum += sum(pre[x]) + sum(pre[sortedkeys[1]])
            res.append(previous_sum)
        else:
            # Inserted in second position
            previous_sum -= sum(pre[sortedkeys[0]])
            pre[sortedkeys[0]] = (1, x-1)
            pre[x] = (sortedkeys[0]+1, n)
            previous_sum += sum(pre[x]) + sum(pre[sortedkeys[0]])
            res.append(previous_sum)
    else:
        # 3 or more elements
        indx = sortedkeys.index(x)
        if(indx == 0):
            # Inserted in first position
            previous_sum -= sum(pre[sortedkeys[1]])
            pre[x] = (1, sortedkeys[1]-1)
            pre[sortedkeys[1]] = (x+1, sortedkeys[2]-1)
            previous_sum += sum(pre[x]) + sum(pre[sortedkeys[1]])
            res.append(previous_sum)
        elif(indx == len(sortedkeys)-1):
            # Inserted at last position
            previous_sum -= sum(pre[sortedkeys[-2]])
            pre[x] = (sortedkeys[-2]+1, n)
            pre[sortedkeys[-2]] = (sortedkeys[-3]+1, x-1)
            previous_sum += sum(pre[x]) + sum(pre[sortedkeys[-2]])
            res.append(previous_sum)
        else:
            # Anywhere in between, modify both left and right
            previous_sum -= sum(pre[sortedkeys[indx-1]]) + sum(pre[sortedkeys[indx+1]])
            pre[x] = (sortedkeys[indx-1]+1, sortedkeys[indx+1]-1)
            leftofleft = pre[sortedkeys[indx-1]][0]
            rightofright = pre[sortedkeys[indx+1]][1]
            rightofleft = x-1
            leftofright = x+1
            pre[sortedkeys[indx-1]] = (leftofleft, rightofleft)
            pre[sortedkeys[indx+1]] = (leftofright, rightofright)
            previous_sum += sum(pre[x]) + sum(pre[sortedkeys[indx-1]]) + sum(pre[sortedkeys[indx+1]])
            res.append(previous_sum)
print(pre)
print(res)