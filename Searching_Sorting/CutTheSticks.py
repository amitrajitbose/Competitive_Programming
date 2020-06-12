def cutTheSticks(arr):
    arr.sort(reverse = True)
    res = []
    while arr:
        res.append(len(arr))
        for i in range(len(arr)):
            arr[i] -= arr[-1]
        while len(arr) and arr[-1] <= 0:
            arr.pop(-1)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

