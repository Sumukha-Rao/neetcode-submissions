class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        for i in range(k,len(nums)):
            nums.append(nums[0])
            del nums[0]

        