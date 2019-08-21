"""
Given a string and a list of words. Find the total number of ways you can replace a word by its anagram from the given list of words/

Example:
Word list = the, bats, tabs, in, cat, act

Sentence 1 = cat the bats
Here you can replace cat with either of [cat, act] and you can replace bats with [bats,tabs] and the cannot be replaced.
Output 1 = 4

Sentence 2 = in the act
Output 2 = 2

Sentence 3 = act tabs in
Output 3 = 4

Source: Cognizant Mock Test 2019
"""

def gets_freq_vector(word):
    word = word.lower()
    fv = [0] * 26
    for ch in word:
        try:
            fv[ord(ch)-97] += 1
        except:
            pass
    fvs = [str(x) for x in fv]
    return ''.join(fvs)

def countSentences(wordSet, sentences):
    # Write your code here
    combinationsInVocab = dict()
    for w in wordSet:
        w = w.strip()
        fvs = gets_freq_vector(w)
        if fvs not in combinationsInVocab:
            combinationsInVocab[fvs] = 1
        else:
            combinationsInVocab[fvs] += 1
    vals = []
    for s in sentences:
        occuranceInSent = dict()
        for w in s.split():
            fvs = gets_freq_vector(w)
            if fvs not in occuranceInSent:
                occuranceInSent[fvs] = 1
            else:
                occuranceInSent[fvs] += 1
        s1 = set(list(combinationsInVocab.keys()))
        s2 = set(list(occuranceInSent.keys()))
        s3 = s1.intersection(s2)
        val = 1
        s3 = list(s3)
        for k in s3:
            val *= combinationsInVocab[k] ** occuranceInSent[k]
        vals.append(val)
    return vals

