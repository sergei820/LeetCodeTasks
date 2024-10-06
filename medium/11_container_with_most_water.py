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
        h1 = Pointer(0, height[0])
        h2 = Pointer(len(height) - 1, height[len(height) - 1])
        # сделал шаг с одного конце, если выше, то охранить пару: индекс, высота
        # из высот с двух концов взять меньшую,
        # умножить на расстояние между ними
        for i in range(len(height) // 2):
            index_from_end = len(height) - i - 1
            if height[i] > h1.value + 1:
                h1.index = i
                h1.value = height[i]

                # взять меньшее
                if h1.value < h2.value:
                    smaller_height = h1.value
                else:
                    smaller_height = h2.value

                # рассчитать расстояние, умножить на меньшую высоту, сравнить площадь с предыдущей
                distance = len(height) - h1.index - h2.index
                if max_area < smaller_height * distance:
                    max_area = smaller_height * distance

            if height[index_from_end] < h2.value + 1:
                h2.index = index_from_end
                h2.value = height[index_from_end]
                # взять меньшее
                if h1.value < h2.value:
                    smaller_height = h1.value
                else:
                    smaller_height = h2.value

                # рассчитать расстояние, умножить на меньшую высоту, сравнить площадь с предыдущей
                distance = len(height) - h1.index - h2.index
                if max_area < smaller_height * distance:
                    max_area = smaller_height * distance

        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
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
