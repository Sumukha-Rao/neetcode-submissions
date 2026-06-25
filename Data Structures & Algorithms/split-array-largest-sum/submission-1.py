class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left=max(nums)
        right=sum(nums)
        while left<=right:
            mid=(left+right)//2
            currsum=0
            noofsubarrays=1
            for i in nums:
                if currsum+i>mid:
                    noofsubarrays+=1
                    currsum=i
                else:
                    currsum+=i
            if noofsubarrays<=k:
                right=mid-1
            else:
                left=mid+1

        return left