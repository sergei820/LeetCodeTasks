from typing import List

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
# of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.

class Pointer:
    def __init__(self, index, value):
        self.index = index
        self.value = value

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = Pointer(0, height[0])
        right = Pointer(len(height) - 1, height[len(height) - 1])

        while left.index < right.index:
            current_area = min(left.value, right.value) * (right.index - left.index)
            if current_area > max_area:
                max_area = current_area

            if height[left.index] > height[right.index]:
                right.index -= 1
                right.value = height[right.index]
            else:
                left.index += 1
                left.value = height[left.index]

        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(s.maxArea([2, 1]))
    print(s.maxArea([1, 2, 4, 3]))  # 4
#
# Example 1:
#
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case,
# the max area of water (blue section) the container can contain is 49.
# Example 2:
#
# Input: height = [1,1]
# Output: 1
