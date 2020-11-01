'''
This problem was asked by Amazon.

At a popular bar, each customer has a set of favorite drinks, and will happily accept any drink among this set. For example, in the following situation, customer 0 will be satisfied with drinks 0, 1, 3, or 6.

preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
A lazy bartender working at this bar is trying to reduce his effort by limiting the drink recipes he must memorize. Given a dictionary input such as the one above, return the fewest number of drinks he must learn in order to satisfy all customers.

For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.

Author: @amitrajitbose
'''

from collections import defaultdict

def minDrinks(preferences):
    totalCust = len(preferences)
    drinkToCust = defaultdict(set)
    for c in preferences:
        for d in preferences[c]:
            drinkToCust[d].add(c)
    minDrinks = []
    satisfiedCustomers = set([])
    while len(satisfiedCustomers) < totalCust:
        sortedDtc = list({k: v for k, v in sorted(drinkToCust.items(), key=lambda item: len(item[1]), reverse=True)})
        drink = sortedDtc[0] # alternatively pop(0)
        minDrinks.append(drink)
        satisfiedCustomers.update(drinkToCust[drink])
        drinkToCust[drink] = set([]) # same as deleting the key
        for d in drinkToCust:
            drinkToCust[d] = drinkToCust[d].difference(satisfiedCustomers)
        # print(sortedDtc[0], '->', satisfiedCustomers, drinkToCust,end="\n\n")
    print(minDrinks)
    return(minDrinks)


preferences1 = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
assert minDrinks(preferences1) == [5,1]


preferences2 = {
    1: [5, 7, 8],
    2: [5, 6, 9],
    3: [7, 8, 9]
}
assert minDrinks(preferences2) == [5,7]


