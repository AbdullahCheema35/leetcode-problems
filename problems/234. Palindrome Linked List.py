from typing import Optional, assert_type, cast


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
            prev, prev.next, slow = slow, prev, slow.next

        if fast:
            slow = cast(ListNode, slow).next

        while prev:
            if slow.val != prev.val:
                return False
            slow, prev = slow.next, prev.next

        return True
