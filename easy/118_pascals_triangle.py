import math


class Solution(object):
    def generate(self, num_rows):
        """
        :type num_rows: int
        :rtype: List[List[int]]
        """
        result = []
        if num_rows <= 0:
            raise ValueError("Choose a positive value")

        for row_number in range(1, num_rows + 1):
            row = [1]
            if row_number > 2:
                row.append(row_number - 1)

            if row_number > 4:
                # calculate values
                prevoius_row = result[row_number - 2]
                ceil_rounded_middle = int(math.ceil(row_number / 2))
                for i in range(2, ceil_rounded_middle):
                    val_to_add = prevoius_row[i - 1] + prevoius_row[i]
                    row.append(val_to_add)

            # mirroring
            if row_number > 1:
                if row_number % 2 == 0:
                    row.extend(row[::-1])
                else:
                    index_until_copy = int(math.floor(row_number/2))
                    first_half = row[:index_until_copy:]
                    row.extend(first_half[::-1])

            result.append(row)
        return result


# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
#        [1] - row 1
#       [1,1] - row 2
#      [1,2,1] - row 3
#    [1,3,3,1] - row 4
#    [1,4,6,4,1] - row 5
#  [1,5,10,10,5,1]
# [1,6,15,20,15,6,1]

# Example 2:
# Input: numRows = 1
# Output: [[1]]


if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))
