a0 = '376782365465497859'
a0 = '87489543528930998385608359876385765806784785670487869469874896789457064'
b0 = '87567948756746869874'
b0 = '8578493780570495789469548699569346098358063345873895380949288945445403584'
a = list(a0)
b = list(b0)

if(len(a)!=len(b)):
    padding = len(a)-len(b)
    if(padding > 0):
        #a is longer
        pad = [0]*padding
        b = pad + b
    elif(padding <0):
        #b is longer
        pad = [0]*(abs(padding))
        a = pad + a

c = []
carry = 0
for i in range(len(a)-1,-1,-1):
    val = int(a[i]) + int(b[i]) + carry
    carry = 0
    if(val > 9):
        c.append(str(val%10))
        carry = val//10
    else:
        c.append(str(val))
c.append(str(carry))
c.reverse()
output = ''.join(c)
print(output.lstrip('0'))

#print(int(a0)+int(b0))