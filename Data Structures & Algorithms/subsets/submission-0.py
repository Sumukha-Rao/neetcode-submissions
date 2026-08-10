class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets=[]
        def dfs(i,subset):
            if i==len(nums):
                return [subset]
            without=dfs(i+1,subset)
            withnum=dfs(i+1,subset+[nums[i]])
            return withnum+without
        return dfs(0,[])
