# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        array1=[]
        array2=[]
        current=l1
        if l1.val==0 and l2.val==0:
            return ListNode(0)
        while current:
            array1.append(current.val)
            current=current.next
        current=l2
        while current:
            array2.append(current.val)
            current=current.next
        tong=0
        for i in range(len(array1)-1,-1,-1):
            tong+=(array1[i]*(10**(len(array1)-1-i)))
        for i in range(len(array2)-1,-1,-1):
            tong+=(array2[i]*(10**(len(array2)-1-i)))
        
        result=res=ListNode(0)
        array3=[]
        while tong>0:
            array3.append(tong%10)
            tong=tong//10
        array4=[]
        for i in range(len(array3)-1,-1,-1):
            array4.append(array3[i])
        for i in range(0,len(array4)):
            j=ListNode(array4[i])
            res.next=j
            res=res.next
        
        return result.next