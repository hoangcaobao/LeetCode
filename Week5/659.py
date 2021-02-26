import heapq
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        array=[]
        heapq.heapify(array)
        for i in nums:
            if len(array)==0 or array[0][0]==i:
                heapq.heappush(array,[i,1])
                continue
            
            while len(array)>0 and i!=array[0][0]+1:
                
                if array[0][1]<3:
                    return False
                heapq.heappop(array)
            
            if len(array)!=0:
                array[0][0]=i
                array[0][1]+=1
                heapq.heapify(array)
            else:
                heapq.heappush(array,[i,1])
        if len(array)==0: 
            return True
        for i in range(0,len(array)):
            if array[i][1]<3:
                return False
        return True