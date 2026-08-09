class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects=sorted(zip(capital,profits))
        heap=[]
        import heapq
        i=0
        n=len(projects)
        for _ in range(k):
            while i<n and projects[i][0]<=w:
                cap,profit=projects[i]
                heapq.heappush(heap,-profit)
                i+=1
            if not heap:
                break
            w+=-heapq.heappop(heap)
        return w