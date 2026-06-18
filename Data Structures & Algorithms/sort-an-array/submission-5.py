class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import random
        def partition(left, right):
            pivot_idx = random.randint(left, right)
            nums[left], nums[pivot_idx] = nums[pivot_idx], nums[left]  # add this line
            start = left
            pivot = nums[left]
            left += 1
            while left <= right:
                while left <= right and nums[left] <= pivot:
                    left += 1
                while left <= right and nums[right] > pivot:
                    right -= 1
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
            nums[start], nums[right] = nums[right], nums[start]
            return right
        def quick(left,right):
            if left<right:
                j=partition(left,right)
                quick(left,j-1)
                quick(j+1,right)
        quick(0,len(nums)-1)
        return nums
                  



