class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l, r = 0, 1
        # maxP = 0
        # while r < len(prices):
        #     if prices[r] > prices[l]:
        #         profit = prices[r] - prices[l]
        #         maxP = max(profit, maxP)
        #     else:
        #         l = r
        #     r += 1
        # if maxP < 0:
        #     return 0
        # return maxP
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
            
        return max_profit

