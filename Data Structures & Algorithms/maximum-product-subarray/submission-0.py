class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result=nums[0]
        currmax=1
        currmin=1
        for i in nums:
            oldmax=currmax
            oldmin=currmin
            currmax=max(i,i*oldmax,i*oldmin)
            currmin=min(i,i*oldmax,i*oldmin)
            result=max(result,currmax)
        return result