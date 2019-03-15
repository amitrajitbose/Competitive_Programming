from math import ceil

def insertionSort(alist):
		for index in range(1,len(alist)):
		
				currentvalue = alist[index]
				position = index
				
				while position>0 and alist[position-1]>currentvalue:
						alist[position]=alist[position-1]
						position = position-1
				
				alist[position]=currentvalue
		return alist

def partition(lst, low, high):
    i = low - 1
    pivot = lst[high]
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1


def quick_sort(lst, low, high):
    if low < high:
        pi = partition(lst, low, high)
        quick_sort(lst, low, pi - 1)
        quick_sort(lst, pi + 1, high)
    return lst


for _ in range(int(input())):
	cnt = 0
	n, k = [int(x) for x in input().strip().split()]
	arr = [int(x) for x in input().strip().split()]
	for i in range(n):
		for j in range(i,n):
			m = ceil(k/((j-i)+1))
			subseq = arr[i:j+1]
			subseq = quick_sort(subseq, 0, len(subseq)-1)
			tmp=ceil(k/m)
			X = subseq[tmp-1]
			F = subseq.count(X)
			if(F in subseq):
				cnt+=1
	print(cnt)
