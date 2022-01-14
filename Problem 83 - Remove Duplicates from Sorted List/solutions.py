from list_node import ListNode
from typing import Optional


def solution_1(head: Optional[ListNode] = None) -> Optional[ListNode]:
    ret_node = head
    while head and head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return ret_node


def solution_2(head: Optional[ListNode] = None, parent: Optional[int] = None) -> Optional[ListNode]:
    if head is None:
        return head
    if head.val == parent:
        return solution_2(head.next, head.val)
    head.next = solution_2(head.next, head.val)
    return head
