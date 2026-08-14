class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def backtrack(i,current):
            res.append(current.copy())
            for j in range(i,len(nums)):
                if j>i and nums[j-1]==nums[j]:
                    continue
                current.append(nums[j])
                backtrack(j+1,current)
                current.pop()
        backtrack(0,[])
        return res
