class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        least=max(weights)
        highest=sum(weights)
        while least<=highest:
            mid=(least+highest)//2
            wsum=0
            ndays=1
            for i in weights:
                if wsum+i>mid:
                    wsum=i
                    ndays+=1
                else:
                    wsum+=i
            if ndays<=days:
                highest=mid-1
            else:
                least=mid+1
                
        return least
                
