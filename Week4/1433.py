class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        order1=[]
        order2=[]
        for i in range(0,len(s1)):
            order1.append(ord(s1[i]))
        for i in range(0,len(s2)):
            order2.append(ord(s2[i]))
        order1.sort()
        order2.sort()
        if order1[0]>=order2[-1]:
            return True
        if order2[0]>=order1[-1]:
            return True
        count1=0
        for i in range(0,len(order1)):
            if order1[i]>=order2[i]:
                count1+=1
        count2=0
        for i in range(0,len(order2)):
            if order2[i]>=order1[i]:
                count2+=1
        if count1==len(order1) or count2==len(order1):
            return True
        return False
