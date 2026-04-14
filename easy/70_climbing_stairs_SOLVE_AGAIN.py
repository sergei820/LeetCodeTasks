"""
70. Climbing Stairs (Easy)

class Solution:
    def climbStairs(self, n: int) -> int:

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3

Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45
"""

# Runtime 0ms
# Beats 100.00%
# Memory 19.31MB
# Beats 27.17%

class Solution:
    def climbStairs(self, n: int, cache = None) -> int:
        if cache is None:
            cache = {}

        if n in cache:
            return cache[n]

        if n == 1:
            return 1
        elif n == 2:
            return 2
        cache[n] = self.climbStairs(n - 1, cache) + self.climbStairs(n - 2, cache)
        return cache[n]
# input 4
# 2 + 2
# 2 + 1 + 1
# 1 + 2 + 1
# 1 + 1 + 2
# 1 + 1 + 1 + 1

s = Solution()
print(s.climbStairs(44))
