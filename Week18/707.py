class MyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be
        the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked
        list, the node will be appended to the end of linked list. If index is greater than the length, the node will not
        be inserted.
        """
        if index > self.length:
            return
        current = self.head
        new_node = MyNode(val)
        if index <= 0:
            self.head=MyNode(val, self.head)
            
        else:
            for i in range(index - 1):
                current = current.next
            current.next=MyNode(val, current.next)
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length:
            return

        current = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next

        self.length -= 1
