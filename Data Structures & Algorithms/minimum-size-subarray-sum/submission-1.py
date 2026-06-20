class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        currsum=0
        minlen=float("inf")
        for right in range(len(nums)):
            currsum+=nums[right]
            while currsum>=target:
                minlen=min(minlen,right-left+1)
                currsum-=nums[left]
                left+=1
        return 0 if minlen==float("inf") else minlen




        