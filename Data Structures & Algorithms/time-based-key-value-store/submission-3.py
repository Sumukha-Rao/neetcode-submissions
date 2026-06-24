class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.kp=defaultdict(list)
               

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kp[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kp:
            return ""
        left=0
        result=""
        right=len(self.kp[key])-1
        while left<=right:
            mid=(left+right)//2
            time,val=self.kp[key][mid]
            if time<=timestamp:
                result=val
                left=mid+1
            else:
                right=mid-1
        return result

        
