class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result=[]
        people.sort(key= lambda x:(-x[0],x[1]))
        for i in range(0,len(people)):
            result.insert(people[i][1],people[i])
        return result