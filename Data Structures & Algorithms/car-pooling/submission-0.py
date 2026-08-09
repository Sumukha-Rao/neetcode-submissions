class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes=[0]*1000
        for passengers,start,end in trips:
            changes[start]+=passengers
            changes[end]-=passengers
        current=0
        for i in changes:
            current+=i
            if current>capacity:
                return False
        return True

