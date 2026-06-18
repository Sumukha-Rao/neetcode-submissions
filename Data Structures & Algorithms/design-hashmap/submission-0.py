class Hash:
    def __init__(self,key:int,value:int):
        self.key=key
        self.value=value 
class MyHashMap:

    def __init__(self):
        self.hashmap=[]
    def put(self, key: int, value: int) -> None:
        for i in self.hashmap:
            if i.key==key:
                i.value=value
                return
        newData=Hash(key,value)
        self.hashmap.append(newData)
                             
    def get(self, key: int) -> int:
        for i in self.hashmap:
            if i.key==key:
                return i.value
        return -1
        

    def remove(self, key: int) -> None:
        for i in self.hashmap:
            if i.key==key:
                self.hashmap.remove(i)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)