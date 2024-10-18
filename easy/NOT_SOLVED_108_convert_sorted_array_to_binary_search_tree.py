from typing import List, Optional
from unittest import result


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        middle_index = len(nums) // 2
        result = TreeNode(nums[len(nums) // 2])

        def helper(initial_array):
            if initial_array is None:
                return None

            middle_index = len(initial_array) // 2

            result.left = self.sortedArrayToBST(initial_array[:middle_index])
            result.right = self.sortedArrayToBST(initial_array[middle_index:])


        helper(nums)

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.sortedArrayToBST([-10, -3, 0, 5, 9]))

# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]

# Input: nums = [1,3]
# Output: [3,1]
