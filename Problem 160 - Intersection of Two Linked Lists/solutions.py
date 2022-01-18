from list_node import ListNode
from typing import Optional


def solution_1(headA: Optional[ListNode] = None, headB: Optional[ListNode] = None) -> Optional[ListNode]:
    if not headA or not headB:
        return None
    count_a, len_a, count_b, len_b = headA, 0, headB, 0
    while count_a.next:
        len_a += 1
        count_a = count_a.next
    while count_b.next:
        len_b += 1
        count_b = count_b.next
    while len_a < len_b:
        headB = headB.next
        len_b -= 1
    while len_b < len_a:
        headA = headA.next
        len_a -= 1
    while headA is not headB:
        headA, headB = headA.next, headB.next
    return headA


def solution_2(headA: Optional[ListNode] = None, headB: Optional[ListNode] = None) -> Optional[ListNode]:
    final_node = headB
    while final_node.next is not None:
        final_node = final_node.next
    final_node.next = headB
    tortoise = hare = headA
    while tortoise is not None and hare is not None and hare.next is not None:
        tortoise, hare = tortoise.next, hare.next.next
        if tortoise is hare:
            while headA is not tortoise:
                headA, tortoise = headA.next, tortoise.next
            final_node.next = None
            return headA
    final_node.next = None
