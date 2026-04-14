"""
206. Reverse Linked List (Easy)

Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(l: List) -> ListNode | None:
    if not l:
        return None

    head = ListNode(l[0])
    current = head
    for i in range(1, len(l)):
        current.next = ListNode(l[i])
        current = current.next

    return head


def print_linked_list(head: ListNode) -> None:
    result = []
    result.append(head.val)
    current = head.next
    while current:
        result.append(current.val)
        current = current.next

    print(result)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        # None -> 1 -> 2 -> 3 -> 4 -> 5 -> None
        while current:
            next = current.next  # 1 -> 2
            current.next = prev  # None <- 1
            prev = current
            current = next

        return prev


s = Solution()
# print_linked_list(build_linked_list([1, 2, 3, 4, 5]))
print_linked_list(s.reverseList(build_linked_list([1, 2, 3, 4, 5])))
