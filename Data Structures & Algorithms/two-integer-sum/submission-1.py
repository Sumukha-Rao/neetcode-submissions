class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            another_num=target-nums[i]
            rem_arr=nums[i+1:]
            if another_num in rem_arr:
                for j in range(len(rem_arr)):
                    if another_num==rem_arr[j]:
                        return[i,j+1+i]