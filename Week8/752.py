import queue
import collections
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q=queue.Queue()
        q.put("0000")
        visited=collections.defaultdict(bool)
        visited["0000"]=True
        count=0
        deadends=set(deadends)
        if "0000" in deadends:
            return -1
        while q.qsize()>0:
            count+=1
            
            for j in range(q.qsize()):
                u=q.get()
                for v in range(0,len(u)):
                    for i in [1,-1]:

                        value=u[:v]+str((int(u[v])+i)%10)+u[v+1:]

                        if value==target:
                            return count
                        if value in deadends or visited[value]==True:
                            continue
                        q.put(value)
                        visited[value]=True
        
        return -1