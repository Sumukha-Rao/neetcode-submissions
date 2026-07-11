class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import heapq,math
        heap=[-x for x in gifts]
        heapq.heapify(heap)
        for _ in range(k):
           k=heapq.heappop(heap)
           k=-(math.sqrt(-k)//1)
           heapq.heappush(heap,k)
        return -int(sum(heap))