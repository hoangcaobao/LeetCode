class UndergroundSystem:

    def __init__(self):
        self.graph={
        }
        self.time_and_station={
            
        }

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.time_and_station[id]=[t,stationName]
       
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if (self.time_and_station[id][1], stationName) not in self.graph:
            self.graph[(self.time_and_station[id][1], stationName)]=[]
        self.graph[(self.time_and_station[id][1], stationName)].append(t-self.time_and_station[id][0]) 

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.graph[(startStation, endStation)])/len(self.graph[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)