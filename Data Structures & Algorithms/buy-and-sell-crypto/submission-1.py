class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_profit = 0

        while i < j and j<len(prices):
            curr_profit = prices[j]-prices[i]
            max_profit = max(max_profit, prices[j]-prices[i])

            if curr_profit < 0:
                i=j
                j+=1
            else:
                j+=1

        return max_profit

