from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        if len(nums1) > len(nums2):
            longer_list = nums1
            shorter_list = nums2
        else:
            shorter_list = nums1
            longer_list = nums2

        for num in shorter_list:
            if num in longer_list:
                result.append(longer_list.pop(longer_list.index(num)))

        return result


class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        if len(nums1) > len(nums2):
            for num in nums2:
                if num in nums1:
                    result.append(nums1.pop(nums1.index(num)))
        else:
            for num in nums1:
                if num in nums2:
                    result.append(nums2.pop(nums2.index(num)))

        return result


if __name__ == '__main__':
    s = Solution2()
    print(s.intersect([1, 2, 2, 1], [2, 2]))  # [2, 2]
    print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # [4, 9]

# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays
# and you may return the result in any order.
#
#
#
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
#
# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
#
# Follow up:
#
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk,
# and the memory is limited such that you cannot load all elements into the memory at once?
