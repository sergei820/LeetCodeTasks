"""
278. First Bad Version (Easy)

class Solution:
    def firstBadVersion(self, n: int) -> int:

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

Constraints:
1 <= bad <= n <= 231 - 1
"""

def isBadVersion(version: int):
    return version >= 4

# O(log n)
# Runtime 48ms
# Beats 30.21%
# Memory 19.25MB
# Beats 44.50%
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2
            print(f"low: {low}")
            print(f"high: {high}")
            print(f"mid: {mid}\n")
            if isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low


s = Solution()
print(s.firstBadVersion(10))
