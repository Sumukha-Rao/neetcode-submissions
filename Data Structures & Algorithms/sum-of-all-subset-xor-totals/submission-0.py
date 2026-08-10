class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i,xornum):
            if i==len(nums):
                return xornum
            withnum=dfs(i+1,xornum^nums[i])
            withoutnum=dfs(i+1,xornum)
            return withnum+withoutnum
        return dfs(0,0)