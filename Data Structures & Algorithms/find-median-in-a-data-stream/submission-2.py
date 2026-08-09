import heapq
class MedianFinder:

    def __init__(self):
        self.iseven=True
        self.left=[]
        self.leftsize=0
        self.right=[]
        self.rightsize=0

    def addNum(self, num: int) -> None:
        self.iseven= not self.iseven
        if not self.right:
            heapq.heappush(self.right,num)
            self.rightsize+=1
            return
        if num<self.right[0]:
            if self.leftsize>self.rightsize:
                heapq.heappush(self.left,-num)
                num=-heapq.heappop(self.left)
                heapq.heappush(self.right,num)
                self.rightsize+=1
            else:
                heapq.heappush(self.left,-num)
                self.leftsize+=1
        else:
            if self.rightsize>self.leftsize:
                heapq.heappush(self.right,num)
                num=-heapq.heappop(self.right)
                heapq.heappush(self.left,num)
                self.leftsize+=1
            else:
                heapq.heappush(self.right,num)
                self.rightsize+=1
    def findMedian(self) -> float:
        if self.iseven:
            return (self.right[0]-self.left[0])/2
        else:
            if self.leftsize>self.rightsize:
                return -self.left[0]
            else:
                return self.right[0]
        
        