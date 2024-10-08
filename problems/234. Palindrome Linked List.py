from typing import Optional, cast


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            prev, cast(ListNode, prev).next, slow = (
                slow,
                prev,
                cast(ListNode, slow).next,
            )

        if fast:
            slow = cast(ListNode, slow).next

        while prev:
            assert isinstance(slow, ListNode)
            if slow.val != prev.val:
                return False
            slow, prev = slow.next, prev.next

        return True
