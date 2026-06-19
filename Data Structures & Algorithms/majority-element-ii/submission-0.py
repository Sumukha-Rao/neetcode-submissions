class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        n=len(nums)/3
        res=[]
        for i in nums:
            count[i]=count.get(i,0)+1
        for i in count:
            if count[i]>n:
                res.append(i)
        return res