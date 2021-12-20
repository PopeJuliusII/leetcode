from list_node import ListNode
from typing import Optional


def solution_1(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is not None and list2 is not None:
        if list1.val > list2.val:
            list1, list2 = list2, list1
        list1.next = solution_1(list1.next, list2)
    return list1 or list2


def solution_2(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None or list2 is None:
        return list1 or list2
    if list1.val > list2.val:
        list1, list2 = list2, list1
    return_node = list1
    while list2:
        if list1.next is None:
            list1.next = list2
            break
        if list2.val < list1.next.val:
            temp = list2
            list2 = list2.next
            temp.next = list1.next
            list1.next = temp
        list1 = list1.next
    return return_node
