class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            another_num=target-num
            if another_num in seen:
                return [seen[another_num],i]
            else:
                seen[num]=i
            
