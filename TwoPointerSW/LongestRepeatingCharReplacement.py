class Solution:
	# @amitrajitbose
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0]*26
        zeroes = 26
        left = 0
        right = 0
        maxlen = 0
        sumfreq = 0
        maxfreq = 0
        n = len(s)
        while(right < n):
            ascil = ord(s[left])-65
            ascir = ord(s[right])-65
            if(freq[ascir]==0):
                zeroes -= 1
            freq[ascir] += 1
            sumfreq += 1 #adding to freq
            maxfreq = max(maxfreq,freq[ascir]) #max value of freq map
            if zeroes < 26-k-1 or sumfreq-maxfreq > k:
                if freq[ascil] == 1:
                    zeroes += 1
                freq[ascil] -= 1
                sumfreq -= 1 #adding to freq
                maxfreq = max(maxfreq,freq[ascil]) #max value of freq map
                left += 1
            else:
                maxlen = max(maxlen, right-left+1)
            right += 1
        return maxlen

