"""
206. Reverse Linked List (Easy)

Given the head of a singly linked list, reverse the list, and return the reversed list.

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


# current.val = 1
# current.next.val = 2


def build_linked_list(l: List) -> ListNode:
    head = first = ListNode(l[0])

    for i in range(1, len(l)):
        head.next = ListNode(l[i])
        head = head.next

    return first


def print_linked_list(head: ListNode):
    current = head
    result = []
    if current:
        result.append(current.val)

    while current.next:
        result.append(current.next.val)
        current = current.next

    print(result)


# Runtime 0ms
# Beats 100.00%
# Memory 20.60MB
# Beats 38.96%

# O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        # None -> 1 -> 2 -> 3 -> 4 -> 5
        # prev = None
        # current = 1
        # next = 2


        while current:
            # current = 1
            next = current.next # 2
            current.next = prev # None - revert link
            prev = current
            current = next

        return prev # because current made the last step 5 -> None





s = Solution()
linked_list = build_linked_list([1,2,3,4,5])
print_linked_list(linked_list)
print_linked_list(s.reverseList(linked_list))
