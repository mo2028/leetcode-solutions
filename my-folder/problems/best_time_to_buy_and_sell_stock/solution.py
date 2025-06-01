class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowSoFar = float('inf')
        for i in range(len(prices)):
            lowSoFar = min(prices[i], lowSoFar)
            maxProfit = max(maxProfit, prices[i] - lowSoFar)
            print(maxProfit)

        return maxProfit


            
                