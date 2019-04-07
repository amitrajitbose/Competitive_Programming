lights = {
    0 : [0,1,2,3,4,5],
    1 : [1,2],
    2 : [0,1,3,4,6],
    3 : [0,1,2,3,6],
    4 : [1,2,5,6],
    5 : [0,2,3,5,6],
    6 : [0,2,3,4,5,6],
    7 : [0,1,2],
    8 : [0,1,2,3,4,5,6],
    9 : [0,1,2,3,5,6]
}

for _ in range(int(input())):
    maxfilter = [1]*7 #count maximum dead
    tested = [0]*7 #initially none are test
    maxalive = 7
    invalid = False
    for q in range(int(input())):
        digit, segs = map(int, input().strip().split())
        if(segs > len(lights[digit])):
            print("invalid")
            invalid = True
            break
        act = lights[digit]
        pred = lights[digit][:segs]
        #print(act,pred)
        maxalive = min(maxalive, 7-(len(act)-len(pred)))
        not_working = list(set(act)-set(pred))
        for i in not_working:
            maxfilter[i] = 0 #marking it dead
    if(not invalid):
        #print(maxalive, sum(maxfilter))
        print(7-maxalive, 8-sum(maxfilter))