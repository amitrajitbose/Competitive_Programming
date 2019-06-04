# LC 161
class Solution:
    def isOneEditDistance(self, a: str, b: str) -> bool:
        # Obviously DP approach will be costly, n square
        # So I will try to traverse the strings
        lena, lenb = len(a), len(b)
        if lena-lenb not in [-1,0,1]:
            return False
        ptra = ptrb = diff = 0
        while ((ptra < lena) and (ptrb < lenb)):
            if diff > 1:
                return False
            if a[ptra] != b[ptrb]:
                diff += 1
                if lena < lenb:
                    #edit on b
                    ptrb += 1
                elif lena > lenb:
                    # edit on a
                    ptra +=1
                else:
                    #edit on both
                    ptra += 1
                    ptrb += 1
            elif a[ptra] == b[ptrb]:
                # match
                ptra += 1
                ptrb += 1
        # for trailing extra characters in one string
        if(ptra <= lena-1) or (ptrb <= lenb-1):
            diff += 1
        return diff == 1
