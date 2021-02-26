import collections
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic=collections.defaultdict(int)
        for i in range(0,len(arr)):
            dic[arr[i]]+=1
        array=[]
        for key in dic:
            array.append(dic[key])
        array.sort()
        count1=0
        count2=0
        for i in range(len(array)-1,-1,-1):
            count1+=1
            count2+=array[i]
            if count2>=len(arr)//2:
                return count1