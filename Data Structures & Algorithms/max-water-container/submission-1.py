class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        n=len(heights)
        right=n-1
        maxcap=0
        while left<right:
            capacity=(right-left)*min(heights[left],heights[right])
            maxcap=max(capacity,maxcap)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxcap
        