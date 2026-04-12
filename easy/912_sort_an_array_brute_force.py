"""
912. Sort an Array (Medium)

THIS IS A BRUTE FORCE SOLUTION PRACTICE

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3),
while the positions of other numbers are changed (for example, 1 and 5).

Example 2:
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.


Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""
from typing import List


def find_smallest_value_index(nums: List[int]) -> int:
    smallest = nums[0]
    smallest_index = 0

    for i in range(1, len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
            smallest_index = i

    # print(smallest)
    return smallest_index


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sorted_array = []
        print(len(nums))

        for _ in range(len(nums)):
            sorted_array.append(nums.pop(find_smallest_value_index(nums)))

        return sorted_array



s = Solution()
print(s.sortArray([5,2,3,1]))
print(s.sortArray([5,1,1,2,0,0]))
