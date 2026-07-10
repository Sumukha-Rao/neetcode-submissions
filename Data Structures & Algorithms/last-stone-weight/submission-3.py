import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            val1=heapq.heappop(heap)
            val2=heapq.heappop(heap)
            if val1==val2:
                continue
            heapq.heappush(heap,val1-val2)
        return -heap[0] if heap else 0
