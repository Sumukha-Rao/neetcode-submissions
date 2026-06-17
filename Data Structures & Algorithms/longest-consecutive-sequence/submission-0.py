class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numlist=set(nums)
        maxlength=1
        length=1
        for i in nums:
            if (i-1) not in numlist:
                length=1
                current=i
                while (current+1) in numlist:
                    length+=1
                    current+=1
                maxlength=max(length,maxlength) 
        return maxlength
        