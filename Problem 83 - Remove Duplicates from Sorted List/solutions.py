from list_node import ListNode
from typing import Optional


def solution_1(head: Optional[ListNode] = None) -> list[int]:
    ret_node = head
    while head and head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return ret_node
