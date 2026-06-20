class MyStack:

    def __init__(self):
        self.stack=[]
        self.pointer=-1
        self.maxlen=-1        

    def push(self, x: int) -> None:
        self.pointer+=1
        if self.pointer>self.maxlen:
            self.stack.append(0) 
        self.stack[self.pointer]=x       

    def pop(self) -> int:
        self.pointer-=1
        return self.stack[self.pointer+1]
        
    def top(self) -> int:
        return self.stack[self.pointer]        

    def empty(self) -> bool:
        if self.pointer>-1:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()