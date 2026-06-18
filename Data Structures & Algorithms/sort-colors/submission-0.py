class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(left,right):
            start=left
            pivot=nums[left]
            left+=1
            while left<=right:
                while  left<=right and nums[left]<=pivot:
                    left+=1
                while left<=right and nums[right]>pivot :
                    right-=1
                if left<right:
                    nums[left],nums[right]=nums[right],nums[left]
            
            nums[start],nums[right]=nums[right],nums[start]  
            return right
        def quick(left,right):
            if left<right:
                j=partition(left,right)
                quick(left,j-1)
                quick(j+1,right)
        quick(0,len(nums)-1)
        
            
            
        