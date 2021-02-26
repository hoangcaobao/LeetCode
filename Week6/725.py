# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        count=0
        temp=bienchay=ListNode(0)
        current1=current2=current3=root
        while current1:
            count+=1
            current1=current1.next
        result=[]
        if count==0:
            for i in range(0,k):
                result.append(current2)
        
        elif count<=k:
            while current2:
                temp.next=ListNode(current2.val,None)
                
                
                
                
                result.append(temp.next)
                current2=current2.next
                
            
            if count<k:
                for i in range(0,k-count):
                    result.append(current2)
                    
        else:
            dic={}
            dic[count//k+1]=count-count//k*k
            dic[count//k]=k-(count-count//k*k)
            count1=0
            while current2 and dic[count//k+1]>0:
                if count1==count//k+1:
                    bienchay.next=None
                    result.append(temp.next)
                    temp=bienchay=ListNode(0)
                    count1=0
                    dic[count//k+1]-=1
                bienchay.next=ListNode(current2.val,None)
                count1+=1
                current2=current2.next
                bienchay=bienchay.next
      
            while current2 and dic[count//k]>0:
                if count1==count//k:
                    bienchay.next=None
                    result.append(temp.next)
                    temp=bienchay=ListNode(0)
                    count1=0
                    dic[count//k]-=1
                
                bienchay.next=ListNode(current2.val,None)
                count1+=1
                current2=current2.next
                bienchay=bienchay.next
                
            bienchay.next=None
            result.append(temp.next)
            
        return result