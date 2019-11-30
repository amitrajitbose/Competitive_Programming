def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        arr.sort()
        pos = set(arr)
        plant = 0
        for i in range(n):
            if not (arr[i]-1 in pos or arr[i]+1 in pos):
                pos.add(arr[i]+1)
                plant += 1
        #print(pos)
        print(plant)
main()