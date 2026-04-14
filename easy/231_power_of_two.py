"""
231. Power of Two (Easy)

Topics
premium lock icon
Companies
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false

Constraints:

-231 <= n <= 231 - 1
"""

# Runtime 0ms
# Beats 100.00%
# Memory 19.13MB
# Beats 89.78%

# O(log n)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        elif n == 1:
            return True
        elif n % 2 != 0:
            return False

        return self.isPowerOfTwo(n // 2)


s = Solution()
print(s.isPowerOfTwo(8))
print(s.isPowerOfTwo(32))
print(s.isPowerOfTwo(14))
print(s.isPowerOfTwo(6))
