"""
169. Majority Element (Easy)

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List


# Runtime 15ms
# Beats 19.31%
# Memory 21.10MB
# Beats 63.66%

# O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}
        for el in nums:
            if el not in elements:
                elements[el] = 1
            else:
                elements[el] += 1
            if elements[el] > (len(nums) / 2):
                return el


s = Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))

