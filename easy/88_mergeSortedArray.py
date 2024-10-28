from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp_array = []

        for i in range(m):
            if len(tmp_array) != 0 and len(nums2) != 0:
                if tmp_array[0] >= nums1[i] <= nums2[0]:
                    continue
                elif tmp_array[0] < nums2[0]:
                    tmp_array.append(nums1[i])
                    nums1[i] = tmp_array.pop(0)
                else:
                    tmp_array.append(nums1[i])
                    nums1[i] = nums2.pop(0)

            elif len(tmp_array) != 0 and len(nums2) == 0:
                if tmp_array[0] >= nums1[i]:
                    continue
                else:
                    tmp_array.append(nums1[i])
                    nums1[i] = tmp_array.pop(0)
            elif len(tmp_array) == 0 and len(nums2) != 0:
                if nums2[0] >= nums1[i]:
                    continue
                else:
                    tmp_array.append(nums1[i])
                    nums1[i] = nums2.pop(0)

        for i in range(m, m + n):
            if len(tmp_array) != 0 and len(nums2) != 0:
                if tmp_array[0] <= nums2[0]:
                    nums1[i] = tmp_array.pop(0)
                else:
                    nums1[i] = nums2.pop(0)
            elif len(tmp_array) != 0 and len(nums2) == 0:
                nums1[i] = tmp_array.pop(0)
            else:
                nums1[i] = nums2.pop(0)


        print(f'Tmp_array: {tmp_array}')
        print(f'nums1: {nums1}')
        print(f'nums2: {nums2}')


if __name__ == '__main__':
    s = Solution()
    # s.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
    s.merge(nums1=[0, 0, 3, 0, 0, 0, 0, 0, 0], m=3,
            nums2=[-1, 1, 1, 1, 2, 3], n=6)

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements
# that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
#
#
#
# Example 1:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3,
# nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:
#
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:
#
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1.
# The 0 is only there to ensure the merge result can fit in nums1.
#
#
# Constraints:
#
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109
#
#
# Follow up: Can you come up with an algorithm that runs in O(m + n) time?
