class OrderedStream:

    def __init__(self, n: int):
        self.contain=[0 for i in range(n)]
        self.pointer=0

    def insert(self, idKey: int, value: str) -> List[str]:
        result=[]
        self.contain[idKey-1]=value
        while(self.pointer<len(self.contain) and self.contain[self.pointer]!=0):
            result.append(self.contain[self.pointer])
            self.pointer+=1
        
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)