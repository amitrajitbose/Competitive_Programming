"""
We consider a string programmer string if some subset of its letters can be rearranged to form the word programmer.
They are anagrams.
Given a long string determine the number of indices within the string that are in between two programmer strings.
The character 'x' inside an anagram are considered redundant and not counted. But they are counted normally as characters outside
an anagram of programmer type substring.

This question came in Cognizant Mock Test 2019
"""

def  getVector(w):
    w = w.lower()
    fv = [0]*26
    for ch in w:
        fv[ord(ch)-97] += 1
    return fv

def getsVector(w):
    w = w.lower()
    fv = [0]*26
    for ch in w:
        fv[ord(ch)-97] += 1
    return stringifyWindow(fv)

def stringifyWindow(arr):
    arr[23] = 0
    fvs = [str(i) for i in arr]
    return ''.join(fvs)

def addToWindow(fv, ch):
    fv[ord(ch)-97] += 1
    return fv
def remFromWindow(fv, ch):
    fv[ord(ch)-97] -= 1
    return fv

def program(string, word):
    end1, start2 = 0, 0
    if len(string) < len(word):
        return -1
    n = len(string)
    found = 0
    targethashstr = getsVector(word)
    left = 0
    right = len(word)-1
    window = string[:len(word)]
    windowhash = getVector(window)
    while right < n:
        #print(left, right, string[left:right+1])
        # x is present
        while len(word) > sum(windowhash)-windowhash[23]:
            #print("Window Lengthening Due To Presence Of X")
            right += 1
            if right == n:
                right = n-1
                break
            windowhash = addToWindow(windowhash, string[right])
        #print(string[left:right+1])
        windowhashstr = stringifyWindow(windowhash)
        if windowhashstr == targethashstr and found == 0:
            found = 1
            while string[left] == 'x':
                left += 1
            #print("First ",left,right)
            end1 = right
        elif windowhashstr == targethashstr and found == 1:
            found = 2
            while string[left] == 'x':
                left += 1
            start2 = left
            #print("Second ",left,right, string[left: right+1])
            break
        else:
            #print("Sliding")
            left += 1
            right = left + len(word) - 1
            windowhash = getVector(string[left : right+1])
            continue

        left = right + 1
        right = left + len(word) - 1
        windowhash = getVector(string[left : right+1])
    if found == 2:
        return start2 - end1 - 1
    else:
        return -1

print(program('programmerrxprogxxermram','programmer'))
print(program('xprogrxammerprogrammer','programmer'))
print(program('rammerxprogrammer','programmer'))
print(program('progamemrrgramxprgom', 'programmer'))
print(program('progamemrrgramxprergom', 'programmer'))
print(program('progamemrrramxprergom', 'programmer'))