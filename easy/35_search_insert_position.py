"""
35. Search Insert Position (Easy)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
from typing import List

# Runtime 0ms
# Beats 100.00%
# Memory 20.04MB
# Beats 26.74%

# O(log n)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        count = 0

        while low <= high:
            count += 1
            mid = (low + high) // 2
            print(f"\ncount {count}:\n")
            print(f"high: {high}")
            print(f"low: {low}")
            print(f"mid: {mid}")

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low


s = Solution()
print(f"\nresult: {s.searchInsert(nums = [1,3,5,6], target = 5)}")  # 2
print(f"\nresult: {s.searchInsert(nums = [1,3,5,6], target = 2)}")  # 1
print(f"\nresult: {s.searchInsert(nums = [1,3,5,6], target = 7)}")  # 4
