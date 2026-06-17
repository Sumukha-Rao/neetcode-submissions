class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        pointer=0
        volume=0
        while pointer < len(height) and height[pointer]==0:
            pointer+=1
        
        while pointer < len(height):
            # Find the next peak that is either >= current peak or the highest remaining peak
            best_next = -1
            max_h = -1
            for i in range(pointer + 1, len(height)):
                if height[i] >= height[pointer]:
                    best_next = i
                    break
                if height[i] > max_h:
                    max_h = height[i]
                    best_next = i
            
            if best_next == -1:
                break
            
            # Calculate water between pointer and best_next
            target_h = min(height[pointer], height[best_next])
            for i in range(pointer + 1, best_next):
                if target_h > height[i]:
                    volume += target_h - height[i]
            
            pointer = best_next
            
        return volume