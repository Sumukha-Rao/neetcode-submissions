class Solution:
    def trap(self, height: List[int]) -> int:
        left=1
        right=len(height)-2
        lmax=height[0]
        rmax=height[right+1]
        res=0
        while left<=right:
            if lmax<=rmax:
                res+=max(0,lmax-height[left])
                lmax=max(height[left],lmax)
                left+=1
            else:
                res+=max(0,rmax-height[right])
                rmax=max(height[right],rmax)
                right-=1
        return res