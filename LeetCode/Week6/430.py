"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        stack=[]
        temp=head
        while temp:
            if temp.child:
                if temp.next:
                    stack.append(temp.next)
                temp.next=temp.child
                temp.next.prev=temp
                temp.child=None
                
            elif not temp.next and len(stack)!=0:
                temp.next=stack.pop()
                temp.next.prev=temp
                
            temp=temp.next
        
        return head