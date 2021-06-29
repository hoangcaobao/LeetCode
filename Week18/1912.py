from sortedcontainers import SortedList
class MovieRentingSystem:
    
    def __init__(self, n: int, entries: List[List[int]]):
        self.rented={}
        self.find_price={}
        self.unrented={}
        for i in entries:
            self.find_price[(i[0],i[1])]=i[2]
            if i[1] not in self.unrented:
               
                self.unrented[i[1]]=SortedList(key = lambda x:(x[1],x[0]))
                self.rented[i[1]]=SortedList(key = lambda x:(x[1],x[0]))
            self.unrented[i[1]].add([i[0],i[2]])
        self.for_report=SortedList(key= lambda x:(x[2],x[0],x[1]))
        
    def search(self, movie: int) -> List[int]:
     
        if movie in self.unrented:
            result=self.unrented[movie]
            result1=[]
            for i in range(len(result)):
                if(i==5):
                    break
                result1.append(result[i][0])
            return result1
        else:
            return []
    def rent(self, shop: int, movie: int) -> None:
        price = self.find_price[(shop,movie)]
        self.unrented[movie].remove([shop,price])
        self.rented[movie].add([shop,price])
        self.for_report.add([shop, movie, price])
                

    def drop(self, shop: int, movie: int) -> None:
        price = self.find_price[(shop,movie)]
        self.rented[movie].remove([shop,price])
        self.unrented[movie].add([shop, price])
        self.for_report.discard([shop, movie, price])
                
        

    def report(self) -> List[List[int]]:
        
        result=self.for_report
        result1=[]
        for i in range(len(result)):
            if i==5:
                break
            result1.append([result[i][0],result[i][1]])
       
        return result1

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()