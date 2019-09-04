"""
In the previous program, if all the characters in a string A are different from those
in string B, then do we still need the 2D matrix?

ANS = NO

Suggest a O(n+m) time algorithm that takes constant O(1) extra memory and gives the
right result for this particular case
"""

class Solution:
    def isInterleave(self, l1: str, l2: str, l3: str) -> bool:
        l1, l2, l3 = map(list, [l1, l2, l3])
        while(True):
            if len(l1) == 0 and len(l2) == 0 and len(l3) == 0:
                return True
            if len(l3) == 0:
                return False
            if len(l1) == 0 and len(l2) == 0:
                return False
            #print(l1, l2, l3)
            if len(l1) and len(l2) and len(l3) and l1[0] == l3[0] and l2[0] == l3[0]:
                # remove from longer list
                if(len(l1) >= len(l2)):
                    l1.pop(0)
                elif(len(l1) < len(l2)):
                    l2.pop(0)
                l3.pop(0)
            elif len(l1) and len(l3) and l1[0] == l3[0]:
                l1.pop(0)
                l3.pop(0)
            elif len(l2) and len(l3) and l2[0] == l3[0]:
                l2.pop(0)
                l3.pop(0)
            else:
                return False
