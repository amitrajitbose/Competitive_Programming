def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if n == 1:
            print(arr[0])
        else:
            n += 1
            arr.append(1001)
            left, right = 0, 1
            res = ''
            while left <= right and right < n and left < n:
                #print(left,right)
                if arr[right]-arr[left] == right-left:
                    right += 1
                else:
                    if right-left >= 3:
                        res += str(arr[left])+'...'+str(arr[right-1])+','
                    else:
                        for i in range(left, right):
                            res += str(arr[i])+','
                    left = right
            print(res.strip(','))
main()
