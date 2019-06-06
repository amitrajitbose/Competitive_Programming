from collections import deque, defaultdict

n,e = [int(x) for x in input().split()]

E = defaultdict(list)

for _ in range(e):
    x,y,c = [int(x) for x in input().split()]
    x -= 1
    y -= 1
    E[x].append((y, c%10))
    E[y].append((x,-c%10))

visited = [False]*n
colored = [[False]*n for _ in range(10)]
ways = [0]*10

for i in range(n):
    if visited[i]: continue
    visited[i] = True
    cluster = {i}

    # Explore cluster
    Q = deque()
    Q.append((i,0))
    while Q:
        cur,color = Q.pop()
        if colored[color][cur]:
            continue
        colored[color][cur] = True
        visited[cur] = True
        cluster.add(cur)

        for neigh,weight in E[cur]:
            newcolor = (weight + color)%10
            Q.append((neigh, newcolor))

    # Handle cluster
    if colored[1][i]:
        # 1 cycle
        cycle = 1
        
        # Everything reachable!
        nreachable = len(cluster)*(len(cluster) - 1)
        for d in range(10):
            ways[d] += nreachable
        continue
    elif colored[2][i]:
        # 2 Cycle
        cycle = 2
    elif colored[5][i]:
        # 5 cycle
        cycle = 5
    else:
        # no cycles
        cycle = 0
        
    # Nodes with some distance to root
    rootdist = [set() for _ in range(10)]
    for node in cluster:
        for d in range(10):
            if colored[d][node]:
                rootdist[d].add(node)
                break

    # Combine and conquer
    dig = [0]*10
    for a in range(10):
        for b in range(10):
            if a != b:
                dig[(b-a)%10] += len(rootdist[a])*len(rootdist[b])
            else:
                dig[0] += len(rootdist[a])*(len(rootdist[a])-1)

    if cycle == 2:
        even = sum(dig[0::2])
        odd  = sum(dig[1::2])
        for d in [0,2,4,6,8]:
            ways[d] += even
        for d in [1,3,5,7,9]:
            ways[d] += odd
    elif cycle == 5:
        sigma = [dig[0]+dig[5],
                 dig[1]+dig[6],
                 dig[2]+dig[7],
                 dig[3]+dig[8],
                 dig[4]+dig[9]]
        for d in range(10):
            ways[d] += sigma[d%5]
    elif cycle == 0:
        # no cycles
        for d in range(10):
            ways[d] += dig[d]
for d in range(10):
    print(ways[d])