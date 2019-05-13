# https://leetcode.com/problems/number-of-atoms/solution/

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        freq = {}
        numstack = []
        elemsymbol = ''
        numprod = 0
        nummark = 0
        elemcount = 1 #minimum number of times an element is present
        formula = formula[::-1]
        for ch in formula:
            if ch.isdigit():
                #numstack.append(ch)
                numprod += int(ch) * (10 ** nummark) #in case an element is more than 9 val
                nummark += 1
            elif ch == ')':
                numstack.append(numprod)
                nummark = 0
                elemcount *= numprod
                numprod = 0
            elif ch == '(':
                elemcount = elemcount // numstack.pop(-1)
                numprod = 0
                nummark = 0 #debug
            elif ch.islower():
                # part of the element
                elemsymbol += ch
            elif ch.isupper():
                elemsymbol += ch
                elemsymbol = elemsymbol[::-1] #reversing to original order
                if(elemsymbol in freq):
                    freq[elemsymbol] += max(numprod, 1) * elemcount
                else:
                    freq[elemsymbol] = max(numprod, 1) * elemcount
                elemsymbol = ''
                numprod = 0
                 nummark = 0
        ans = ''
        #print(freq)
        for i,c in sorted(freq.items()):
            if c>1:
                ans += i+str(c)
            else:
                ans += i
        return ans
