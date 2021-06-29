class MyCircularQueue:

    def __init__(self, k: int):
        self.queue=[-1 for i in range(k)]
        self.current=0
        self.length=k

    def enQueue(self, value: int) -> bool:
        if self.current<self.length:
            for i in range(self.current,0,-1):
                self.queue[i]=self.queue[i-1]
            self.current+=1
            self.queue[0]=value
            return True
        return False

    def deQueue(self) -> bool:
        if self.current>0:
            self.queue[self.current-1]=-1
            self.current-=1
            return True
        return False

    def Front(self) -> int:
        return self.queue[self.current-1]

    def Rear(self) -> int:
        return self.queue[0]

    def isEmpty(self) -> bool:
        return self.current==0

    def isFull(self) -> bool:
        return self.current==self.length


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()