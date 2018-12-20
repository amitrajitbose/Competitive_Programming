'''
DCP #13
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''

author= '@amitrajitbose'
def uniqueCount(s):
	return len(set(list(s)))
def isValid(arr,k):
	uniqueCount = len(arr)-arr.count(0)
	return uniqueCount<=k
def longest(s,k):
	s=s.lower() #convert to lower case
	u=uniqueCount(s)
	if(u<k):
		print ("ERROR")
	else:
		#parameters for the sliding window
		low=0 #start point of sliding window
		high=0 #end point of sliding window
		maxWindow=1 #max length of sliding window
		maxStart=0 #start point of maximum length sliding window
		count=[0]*26 #hash map to store frequency of characters, 26 characters

		#put first character inside window
		count[ord(s[0])-97]+=1
		for i in range(1,len(s)):
			count[ord(s[i])-97]+=1
			high+=1
			while(not isValid(count,k)):
				#remove the first element from the window
				count[ord(s[low])-97]-=1
				low+=1
			if(high-low+1 > maxWindow):
				maxWindow = high-low+1
				maxStart = low
		print("LONGEST SUBSTRING WITH {0} DISTINCT CHARACTERS IS {1} OF LENGTH {2}".format(k,s[maxStart:maxStart+maxWindow],maxWindow))

longest('aabacbebebe',3)
longest('abcba',2)
longest('helloworld',2)
longest('ababacaaa',2)
longest('xyaabbwzaaabbpqaaabbbfg',2)