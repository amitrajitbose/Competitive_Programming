def reValuation(num): 
	if (num >= 0 and num <= 9): 
		return chr(num + ord('0'))
	else: 
		return chr(num - 10 + ord('A'))


def convert(res, base, inputNum): 

	index = 0
	while (inputNum > 0): 
		res+= reValuation(inputNum % base)
		inputNum = int(inputNum / base)

	# Reverse the result 
	res = res[::-1]

	return res

# Driver Code 
for _ in range(int(input())):
	inputNum, base = [int(x) for x in input().strip().split()]
	res = ""
	print(convert(res, base, inputNum)); 

