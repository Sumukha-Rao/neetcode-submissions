class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                if nums[right]>=target:
                    left=mid+1
                else:
                    right=right-1
            elif nums[mid]>target:
                if nums[left]<=target:
                    right=mid-1
                else:
                    left=left+1
        return -1

        