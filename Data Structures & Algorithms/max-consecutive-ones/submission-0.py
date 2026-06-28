class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxones=0
        count=0
        for i in nums:
            if i==1:
                count+=1
                maxones=max(maxones,count)
            else:
                count=0
        return maxones
        