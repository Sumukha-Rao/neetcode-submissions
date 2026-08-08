import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n=len(tasks)
        tasks=[[enqueue,process,i] for i ,(enqueue,process)in enumerate(tasks)]
        tasks.sort()
        heap=[]
        i=0
        time=0
        result=[]
        while i<n or heap:
            if not heap:
                time = max(time,tasks[i][0])
            while i<n and tasks[i][0]<=time:
                enqueue,process,index=tasks[i]
                heapq.heappush(heap,[process,index])
                i+=1

            process,index=heapq.heappop(heap)
            result.append(index)
            time+=process

        return result