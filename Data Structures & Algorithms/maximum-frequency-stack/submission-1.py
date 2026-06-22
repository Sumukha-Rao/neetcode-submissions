class FreqStack:

    def __init__(self):
        self.stack=[]
        self.count={}   
        self.group={}    
        self.maxvalue=0

    def push(self, val: int) -> None:
        self.count[val]=self.count.get(val,0)+1
        self.maxvalue=max(self.maxvalue,self.count[val])
        if self.count[val] not in self.group:
            self.group[self.count[val]]=[]
        self.group[self.count[val]].append(val)
    def pop(self) -> int:
        val=self.group[self.maxvalue].pop()
        if not self.group[self.maxvalue]:
            self.maxvalue-=1
        self.count[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()