import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic=collections.defaultdict(int)
        dic[0]=1
        sumend=0
        result=0
        
        for i in range(0,len(nums)):
            sumend+=nums[i]
            sumstart=sumend-k
            if sumstart in dic:
                result += dic[sumstart]
            dic[sumend]+=1        
        return result