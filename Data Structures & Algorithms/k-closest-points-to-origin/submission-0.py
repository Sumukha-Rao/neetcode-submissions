class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap=[]
        for i in points:
            dist=-math.sqrt(i[0]*i[0]+i[1]*i[1])
            heapq.heappush(heap,(dist,i))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res
            

