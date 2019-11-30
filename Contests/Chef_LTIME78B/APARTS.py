for _ in range(int(input())):
    n,m = [int(x) for x in input().strip().split()]
    mat = []
    clean = []
    
    for i in range(n):
        row = [int(x) for x in input().strip().split()]
        clean.append([0]*m)
        mat.append(row)

    # top windows will never get dirty due to other windows
    clean[0] = [1] * m
    for i in range(1,n):
        for j in range(m):
            # water can trickle into (i,j) only from the following 3 windows
            upleft = 0 if j-1 < 0 else mat[i-1][j-1]
            upper = mat[i-1][j]
            upright = 0 if j+1 >= m else mat[i-1][j+1]
            # now, if the top 3 windows were cleaned before
            # cleaning this current window then this window
            # will be clean
            if mat[i][j] > max(upleft, upper, upright):
                clean[i][j] = 1
            else:
                # this water is dirty water will go in the next row window
                # coz, there is a trickle effect and a window from upper row
                # was cleaned latest
                mat[i][j] = max(upleft, upper, upright)
            
    for i in range(n):
        print(*clean[i], sep='')