# https://www.hackerrank.com/contests/game-of-codes-3-0/challenges/help-dory
# https://www.hackerrank.com/rest/contests/game-of-codes-3-0/challenges/help-dory/download_pdf?language=English

def removeAlternate(n): 
    if (n == 1): 
        return 1

    if (n % 2 == 0): 
        return 2 * removeAlternate(n / 2) - 1
    else: 
        return 2 * removeAlternate(((n - 1) / 2)) + 1

  
# Driver code 

for _ in range(int(input())):
    n=int(input())
    print(removeAlternate(n))