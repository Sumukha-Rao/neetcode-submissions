class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxCapacity=0
        while left<right:
            capacity=(right-left)*min(heights[left],heights[right])
            maxCapacity=max(capacity,maxCapacity)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxCapacity
        