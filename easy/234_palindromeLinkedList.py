from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp_list = []

        head_copy = head

        while head_copy:
            temp_list.append(head_copy.val)
            if head_copy.next:
                head_copy = head_copy.next
            else:
                break

        while head:
            if not head.val == temp_list.pop():
                return False
            head = head.next

        return True


if __name__ == "__main__":
    s = Solution()
    s.isPalindrome([1, 2, 2, 1])
    s.isPalindrome([1, 2])

# Given the head of a singly linked list, return true if it is a
# palindrome
#  or false otherwise.
#
# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false
#
# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
