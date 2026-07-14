class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter,deque
        import heapq
        freq=Counter(tasks)
        heap=[-x for x in freq.values()]
        heapq.heapify(heap)
        q=deque()
        time=0
        while q or heap:
            time+=1
            if heap:
                freq=heapq.heappop(heap)+1
                if freq!=0:
                    q.append((freq,time+n))
            while q and q[0][1]==time:
                heapq.heappush(heap,q.popleft()[0])
        return time