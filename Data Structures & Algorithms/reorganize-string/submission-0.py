from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        heap=[[-v,k] for k,v in count.items()]
        heapq.heapify(heap)  
        prev=""
        result=""
        while heap:
            cnt,char=heapq.heappop(heap)
            if char==prev:
                if not heap:
                    return ""
                cnt2,char2=heapq.heappop(heap)
                result+=char2
                cnt2+=1
                if cnt2<0:
                    heapq.heappush(heap,[cnt2,char2])
                prev=char2
                heapq.heappush(heap,[cnt,char])
            else:
                result+=char
                prev=char
                cnt+=1
                if cnt<0:
                    heapq.heappush(heap,[cnt,char])
        return result

    
