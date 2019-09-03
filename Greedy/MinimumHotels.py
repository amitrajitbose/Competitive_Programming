"""
Uh-oh! There’s been an emergency on Isla Unfortunata and we need to find accommodation for some customers who are stuck with nowhere to stay. Fortunately we have some (magical) partners who can open hotels right now, anywhere we need them to – but it’s a big effort so we need to be as efficient as possible. Can you help us make sure everyone has somewhere to stay?

There are N customers who are stranded on the island, which is spread on an x-axis. We have coordinates for each customer. Since they’re all really tired, they can’t walk more than K units. We’ve promised to accommodate all these customers, so we need you to find the minimum number of hotels that need to be setup to do so.

Input Format
------------
First line contains T, the number of test cases. Each test case has 3 lines of input: First line contains N, number of customers. Second line contains N space separated integers, where Ni indicates the coordinates of the ith customer. Third line contains value K.

Constraints
-----------
All input numbers are positive integers.
T ≤ 1000
N ≤ 104
K ≤ 2000
Ni ≤ 109

Output Format
-------------
Print one integer on each line corresponding to the testcase.

Sample Input 0
--------------
1
4
1 4 6 2
2
Sample Output 0
---------------
2
"""

def solve(customer, k):
    customer = list(set(customer)) # unique positions
    customer.sort()
    # set the first hotel k units from the first customer
    location = customer[0] + k
    hotels = 1
    # check each customer, if within k units ok, else set new hotel at max distance
    for i in customer:
        if abs(location - i) > k:
            hotels += 1
            location = i + k
    return hotels
