class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length=len(nums)/2
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
            if freq[i]>length:
                return i

