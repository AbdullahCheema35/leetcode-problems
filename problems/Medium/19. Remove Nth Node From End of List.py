from typing import Optional, cast

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tempHead: ListNode = ListNode(next=head)
        
        current: Optional[ListNode] = tempHead
        nth: Optional[ListNode] = tempHead

        for i in range(n):
            assert current is not None
            current = current.next
        
        assert current is not None

        while current.next is not None:
            current = current.next
            assert current is not None

            assert nth is not None
            nth = nth.next

        assert nth is not None and nth.next is not None
        nth.next = nth.next.next

        return tempHead.next