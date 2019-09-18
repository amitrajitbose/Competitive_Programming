#LCM309
class Solution:
    def maxProfit_LinearSpace(self, prices: List[int]) -> int:
        # LINEAR SPACE, LINEAR TIME
        # initialise the arrays for buy and sell to be used for bottom up DP
        n = len(prices)
        if n<2:
            return 0

        buy, sell = [0]*n, [0]*n
        buy[0], sell[0] = -prices[0], 0 # base cases: can buy stock on first day, but cannot sell
        for i in range(1, n):
            # either do not buy on ith day, thus buy remains same as day i-1
            # or buy today, only possible if you have sold a day before yesterday, due to cooldown in b/w
            if i>1:
                buy[i] = max(buy[i-1], sell[i-2]-prices[i])
            else:
                buy[i] = max(buy[i-1], 0-prices[i]) # there is no i-2 when i=1, thus sell is 0 for that
            
            # either do not sell today, sell remains the best sell as the previous day
            # or sell today, thus which has been bought previously (even we can sell what we have bought
            # just the day before that is i-1) thus prices[i] is added to total profit
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        return sell[-1]
    
    def maxProfit(self, prices: List[int]) -> int:
        # CONSTANT SPACE, LINEAR TIME
        # initialise the arrays for buy and sell to be used for bottom up DP
        n = len(prices)
        if n<2:
            return 0
        
        buy_0, sell_0, buy_1, sell_1, sell_2 = 0, 0, 0, 0, 0
        buy_1 = -prices[0] # base cases: can buy stock on first day, but cannot sell
        for i in range(1, n):
            # either do not buy on ith day, thus buy remains same as day i-1
            # or buy today, only possible if you have sold a day before yesterday, due to cooldown in b/w
            if i>1:
                buy_0 = max(buy_1, sell_2-prices[i])
            else:
                buy_0 = max(buy_1, -prices[i]) # there is no i-2 when i=1, thus sell is 0 for that
            
            # either do not sell today, sell remains the best sell as the previous day
            # or sell today, thus which has been bought previously (even we can sell what we have bought
            # just the day before that is i-1) thus prices[i] is added to total profit
            sell_0 = max(sell_1, buy_1 + prices[i])
            
            # space optimization
            sell_2 = sell_1
            sell_1 = sell_0
            buy_1 = buy_0
        return sell_0
