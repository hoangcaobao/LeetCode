class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=0
        i=0
        while i<len(prices):
            while i<len(prices)-1 and prices[i]>prices[i+1]:
                i+=1
            if i>=len(prices):
                break
            benhat=prices[i]
            i+=1
            while i<len(prices)-1 and prices[i]<prices[i+1]:
                i+=1
            if i >=len(prices):
                break
            lonnhat=prices[i]
            result+=lonnhat-benhat
        return result