class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, = 0, 0
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
#                 update the max_profit
                max_profit = max(profit, max_profit)
            else:
#         update the left pointer to be the right pointer( which is lower than the left [new lowest to buy the stock])
                l = r
            r += 1
        
       
                    
        return max_profit