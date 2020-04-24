def main():
	for _ in range(int(input())):
		n = int(input().strip())
		if ((n//2)%2):
			print("NO")
		else:
			arr = [2*i for i in range(1,(n//2)+1)]
			accu = 0
			for i in range((n//2)-1):
				arr.append(arr[i]-1)
				accu += 1
			arr.append(arr[(n//2)-1] + accu)
			print("YES")
			last = arr.pop(-1)
			for i in arr:
				print(i, end=" ")
			print(last)
main()

