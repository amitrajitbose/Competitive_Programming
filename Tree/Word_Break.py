'''
DCP #22

This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. 
If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and 
the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string 
"bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

Similar Problem : https://leetcode.com/problems/word-break/description/
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        Author : @amitrajitbose
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        """CREATING THE TRIE CLASS"""
        output = []
        class TrieNode(object):
            
            def __init__(self):
                self.children = [] #will be of size = 26
                self.isLead = False
            
            def getNode(self):
                p = TrieNode() #new trie node
                p.children = []
                for i in range(26):
                    p.children.append(None)
                p.isLeaf = False
                return p
            
            def insert(self, root, key):
                key = str(key)
                pCrawl = root
                for i in key:
                    index = ord(i)-97
                    if(pCrawl.children[index] == None):
                        # node has to be initialised
                        pCrawl.children[index] = self.getNode()
                    pCrawl = pCrawl.children[index]
                pCrawl.isLeaf = True #marking end of word
            
            def search(self, root, key):
                #print("Searching %s" %key) #DEBUG
                pCrawl = root
                for i in key:
                    index = ord(i)-97
                    if(pCrawl.children[index] == None):
                        return False
                    pCrawl = pCrawl.children[index]
                if(pCrawl and pCrawl.isLeaf):
                    return True
        
        def checkWordBreak(strr, root):
            n = len(strr)
            if(n == 0):
                return True
            for i in range(1,n+1):
                if(root.search(root, strr[:i]) and checkWordBreak(strr[i:], root)):
                    output.append(strr[:i])
                    return True
            return False
        
        """IMPLEMENT SOLUTION"""
        root = TrieNode().getNode()
        for w in wordDict:
            root.insert(root, w)
        checkWordBreak(s, root)
        return output[::-1]


print(Solution().wordBreak("thequickbrownfox", ["the", "quick", "fox", "brown"]))
print(Solution().wordBreak("bedbathandbeyond", ["bed", "bath", "bedbath", "and", "beyond"]))
print(Solution().wordBreak("bedbathandbeyond", ["teddy", "bath", "bedbath", "and", "beyond"]))
print(Solution().wordBreak("bedbathandbeyond", ["bed", "bath", "bedbath", "and", "away"]))
