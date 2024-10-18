from idlelib.tree import TreeNode
from typing import Optional, List
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []

        def internal_function(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            internal_function(node.left)
            result.append(node.val)
            internal_function(node.right)

        internal_function(root)
        return result


if __name__ == '__main__':
    s = Solution()
    s.inorderTraversal([1, None, 2, 3])

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Explanation:
#
# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,2,6,5,7,1,3,9,8]
#
# Example 3:
# Input: root = []
# Output: []
#
# Example 4:
# Input: root = [1]
# Output: [1]
