import numpy
for _ in range(int(input())):
    n=int(input())
    ar=[]
    for i in range(n):
        x=list(map(int,input().split()))
        ar.append(x)
    det = numpy.linalg.det(ar)
    print(int(det))