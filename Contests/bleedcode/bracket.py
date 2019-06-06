def maxDepth(S): 
    current_max = 0
    max = 0
    n = len(S) 
  
    # Traverse the input string 
    for i in range(n): 
        if S[i] == '(': 
            current_max += 1

            if current_max > max: 
                max = current_max 
                
        elif S[i] == ')': 
            if current_max > 0: 
                current_max -= 1
            else: 
                return -1
  
    # finally check for unbalanced string 
    if current_max != 0: 
        return -1
  
    return max

def checkOperatorValidation(s):
    l = len(s)
    
    if (s[0] ==  '+' or s[0] ==  '-' or s[0] ==  '*' or s[0] ==  '/'):
        return False
        
    for i in range(1, l):
        if (s[i] ==  '+' or s[i] ==  '-' or s[i] ==  '*' or s[i] ==  '/') and (s[i-1] == '(' or (i+1 < l and s[i+1] == ')')):
            return False
        if (s[i] ==  '+' or s[i] ==  '-' or s[i] ==  '*' or s[i] ==  '/') and ((s[i-1] ==  '+' or s[i-1] ==  '-' or s[i-1] ==  '*' or s[i-1] ==  '/') or (i+1 < l and  (s[i+1] ==  '+' or s[i+1] ==  '-' or s[i+1] ==  '*' or s[i+1] ==  '/'))):
            return False
        if i == l-1 and (s[i] ==  '+' or s[i] ==  '-' or s[i] ==  '*' or s[i] ==  '/'):
            return False
        
    return True

for _ in range(int(input())):
    s = str(input())
    if checkOperatorValidation(s):
        print(maxDepth(s))
    else:
        print('-1')