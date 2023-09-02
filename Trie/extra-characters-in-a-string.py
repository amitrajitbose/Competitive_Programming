#LC 2707: https://leetcode.com/problems/extra-characters-in-a-string/description/
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

def buildTrie(dictionary):
    root = TrieNode()
    for w in dictionary:
        node = root
        for ch in w:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True
    return root

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Amazon Delivery: +918061914444 - 9328
        root = buildTrie(dictionary)
        n = len(s)
        dp = [float('inf')] * (n+1)
        dp[-1] = 0

        for start in reversed(range(n)):
            dp[start] = dp[start + 1] + 1
            node = root
            for end in range(start, n):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.end == True:
                    dp[start] = min(dp[start], dp[end+1])

        return dp[0]
