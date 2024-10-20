from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def prepare_linked_list(a_list: List):
        for i in range(len(a_list) - 1):
            pass

    def print_linked_list(self) -> None:
        new_head = self
        print(new_head.val)
        while new_head.next is not None:
            print(new_head.next.val)
            new_head = new_head.next



class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head.print_linked_list()
        new_head = head

        while new_head.next is not None:
            min_val = min(new_head.val, new_head.next.val)
            max_val = max(new_head.val, new_head.next.val)
            for j in range(min_val, 0, -1):
                if min_val % j == 0 and max_val % j == 0:
                    min_divider = j
                    break

            temp_next = new_head.next
            new_head.next = ListNode(min_divider, temp_next)
            new_head = temp_next

        return head


if __name__ == "__main__":
    linked_list = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))
    # linked_list.print_linked_list()
    s = Solution()
    print(s.insertGreatestCommonDivisors(linked_list).print_linked_list())  # [18,6,6,2,10,1,3]

# Given the head of a linked list head, in which each node contains an integer value.
#
# Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.
#
# Return the linked list after insertion.
#
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
#
#
#
# Example 1:
# Input: head = [18,6,10,3]
# Output: [18,6,6,2,10,1,3]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after
# inserting the new nodes (nodes in blue are the inserted nodes).
# - We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
# - We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
# - We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
# There are no more adjacent nodes, so we return the linked list.

# Example 2:
# Input: head = [7]
# Output: [7]
# Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after
# inserting the new nodes.
# There are no pairs of adjacent nodes, so we return the initial linked list.
#
# Constraints:
# The number of nodes in the list is in the range [1, 5000].
# 1 <= Node.val <= 1000
