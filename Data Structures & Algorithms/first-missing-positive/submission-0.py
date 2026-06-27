class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        larg=max(nums)
        leastpresent=1
        setofpositive=set()
        for i in nums:
            if i <=0:
                continue
            if  i==leastpresent:
                leastpresent+=1
            else:
                setofpositive.add(i)
        if not setofpositive:return leastpresent
        while leastpresent in setofpositive:
            leastpresent+=1
        return leastpresent

        