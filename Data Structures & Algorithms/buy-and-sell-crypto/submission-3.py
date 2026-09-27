class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        bestProfit = 0

        for _ in range(len(prices) - 1):
            profit = prices[r] - prices[l]
            if profit <= 0: 
                l = r
                r += 1
            else:
                if profit > bestProfit:
                    bestProfit = profit
                r += 1
                

        return bestProfit