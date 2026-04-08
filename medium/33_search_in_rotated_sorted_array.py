"""
33. Search in Rotated Sorted Array (Medium)

class Solution:
    def search(self, nums: List[int], target: int) -> int:

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
from typing import List

# O(log n)
# Runtime 0ms
# Beats 100.00%
# Memory 19.38MB
# Beats 85.00%

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        # count = 0

        while low <= high:
            # count += 1
            # if count > 5:
            #     break
            mid = (low + high) // 2
            # print(f"low: {low}")
            # print(f"high: {high}")
            # print(f"mid: {mid}\n")
            if nums[mid] == target:
                return mid
            # is left half sorted?
            # [4,5,6,7,0,1,2]
            elif nums[low] <= nums[mid]:
                # print("Left side is sorted")
                # print(f"{nums[low]} <= {target} < {nums[mid]}")
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] <= nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1



s = Solution()
print(s.search(nums = [4,5,6,7,0,1,2], target = 0))  # 4
print(s.search(nums = [4,5,6,7,0,1,2], target = 3))  # -1
print(s.search(nums = [1], target = 0))  # -1
print(s.search(nums = [4,5,6,7,0,1,2], target = 1))  # 5
print(s.search(nums = [2,1], target = 1))  # 1
print(s.search(nums = [1,3], target = 3))  # 1
print(s.search(nums = [5,1,3], target = 5))  # 0
