# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        array=[]
        stack=[]
        while head:
            array.append(head.val)
            head=head.next
        
        if len(array)%2!=0:
            array.pop(len(array)//2)
            
        while array:
            if not stack:
                stack.append(array[-1])
                array.pop()
            else:
                if stack[-1]==array[-1]:
                    stack.pop()
                    array.pop()
                else:
                    stack.append(array[-1])
                    array.pop()
        
        
        return len(stack)==0