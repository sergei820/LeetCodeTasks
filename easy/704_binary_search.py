from typing import List

"""# 704. Binary Search
# Easy

# Task from scratch (for future practice)

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:

# Given an array of integers nums which is sorted in ascending order, and an integer target,
# write a function to search target in nums. If target exists, then return its index.
# Otherwise, return -1.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#
# Constraints:
#
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order."""


############################## SOLUTIONS ##############################

# Solution 1
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if target not in nums:
#             return -1
#         else:
#             return nums.index(target)

# Solution 2

    # O(log n)

    # Runtime 0ms
    # Beats 100.00%
    # Memory 20.53MB
    # Beats 53.73%

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        counter = 0

        while low <= high:
            counter += 1
            mid = (low + high) // 2

            print(f"low: {low}")
            print(f"high: {high}")
            print(f"mid: {mid}")

            if nums[mid] == target:
                print(f"target index is: {mid}!")
                print(f"found in {counter} steps")
                return mid
            elif nums[mid] < target:
                low = mid + 1  # mid is checked, should be excluded, that's why +1
            else:
                high = mid - 1

            print(f"counter: {counter}")
            print("\n")

        print("Value doesn't present in the list")
        return -1


s = Solution()
print(s.search(nums = [-1,0,3,5,9,12], target = 9))
print(s.search(nums = [-1,0,3,5,9,12], target = 2))
