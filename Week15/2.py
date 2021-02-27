### DO NOT REMOVE THIS
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
### DO NOT REMOVE THIS
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a1=0
        a2=0
        current=l1
        i=0
        while current:
            a1+=current.val*(10**i)
            current=current.next
            i+=1
        j=0
        current=l2
        while current:
            a2+=current.val*(10**j)
            current=current.next
            j+=1
        
      
        result=a1+a2
        link=ListNode(0)
        current=link
        if result==0:
            return link
        while result>0:
            current.next=ListNode(result%10)
            result=result//10
            current=current.next
        return link.next
