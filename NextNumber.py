def next_number(n):
    binary = list(bin(int(n))[2:])
    onecount = binary.count('1')
    zerocount = binary.count('0')
    if(n==1):
        return 2
    elif(zerocount==0):
        res = '1'+'0'+('1'*(onecount-1))
        return int(res,2)
