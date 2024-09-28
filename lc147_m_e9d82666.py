from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def Print(self):
        print("[", end=" ")
        if not self.head:
            print("]")
            return

        it = self.head
        while it:
            print(it.val, end=" ")
            it = it.next
        print("]")

    def Build(self, values: List[int]):
        tail: Optional[ListNode] = None
        for value in values:
            new_tail = ListNode(value)
            if not self.head:
                self.head = new_tail
            else:
                tail.next = new_tail
            tail = new_tail

    def InsertSort(self):
        if not self.head:
            return self.head
        
        it = self.head.next
        while it:
            jt = self.head
            while jt != it:
                if it.val < jt.val:
                    it.val, jt.val = jt.val, it.val
                jt = jt.next
            it = it.next

if __name__ == '__main__':
    head = SinglyLinkedList()
    head.Build([2, 1, 3, 4])
    head.Print()
    head.InsertSort()
    head.Print()
