class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        fast=prices[0]
        slow=prices[0]
        maxprofit=0
        for i in prices:
            fast=i
            if fast>slow:
                profit=fast-slow
                maxprofit+=profit
            slow=fast
        return maxprofit
        