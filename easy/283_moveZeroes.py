from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0

        for i in reversed(range(len(nums))):
            if nums[i] == 0:
                nums.pop(i)
                counter += 1

        nums.extend([0] * counter)


if __name__ == '__main__':
    s = Solution()
    my_list = [0, 1, 0, 3, 12]
    s.moveZeroes(my_list)
    print(my_list)

# Given an integer array nums,
# move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]
#
# Constraints:
# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
