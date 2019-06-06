def weightedUniformStrings(s, queries):
    wts = set()
    prev = -1
    length = 0
    for c in s:
        wt = ord(c) - 96
        wts.add(wt)
        if prev == c:
            length += 1
            wts.add(length * wt)
        else:
            prev = c
            length = 1
     
    rval = []
    for q in queries:
        if q in wts:
            rval.append("Yes")
        else:
            rval.append("No")
    return rval