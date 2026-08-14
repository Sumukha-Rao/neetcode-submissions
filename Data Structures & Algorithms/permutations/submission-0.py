class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(current,used):
            if len(current)==len(nums):
                res.append(current.copy())
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True
                current.append(nums[i])
                backtrack(current,used)
                current.pop()
                used[i]=False
        backtrack([],[False]*len(nums))
        return res