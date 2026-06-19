class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        fast=0
        slow=prices[0]
        maxprofit=0
        for i in prices:
            fast=i
            profit=fast-slow
            maxprofit=max(maxprofit,profit)
            if fast<slow:
                slow=fast
        return maxprofit
        