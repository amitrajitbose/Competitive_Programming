# LC 320

class Solution:
    """
    @param word: the given word
    @return: the generalized abbreviations of a word
    """
    def __init__(self):
        self.res = []
    def generateAbbreviations(self, word):
        self.helper("", word, 0, 0)
        return self.res
    def helper(self, curr, word, pos, cnt):
        # print(self.res)
        if pos == len(word):
            if cnt > 0:
                curr += str(cnt)
            self.res.append(curr)
        else:
            self.helper(curr, word, pos+1, cnt+1)
            if cnt > 0:
                self.helper(curr + str(cnt) + word[pos], word, pos+1, 0)
            else:
                self.helper(curr + word[pos], word, pos+1, 0)

