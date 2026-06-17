class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)  
        n=len(nums)
        solutions=[]
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=-nums[i]
            left=i+1
            right=n-1
            while left<right:
                val=nums[left]+nums[right]
                if val==target:
                    solutions.append([-target,nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif val>target:
                    right-=1
                else:
                    left+=1
        return solutions
                            



        