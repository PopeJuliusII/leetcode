from list_node import ListNode
from typing import Optional


def solution_1(head: Optional[ListNode]) -> bool:
    node_set = set()
    while head is not None:
        if head in node_set:
            return True
        node_set.add(head)
        head = head.next
    return False


def solution_2(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False
