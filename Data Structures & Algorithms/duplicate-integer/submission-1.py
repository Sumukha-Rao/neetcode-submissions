class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        d={}
        for i in nums:
            cnt=0
            for j in nums:
                if i==j:
                    cnt+=1
                    if cnt>1:
                        return True
        return False
           