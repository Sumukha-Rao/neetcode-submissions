class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        x=0
        for num in nums:
            x|=num
        return x*(2**(len(nums)-1))
        