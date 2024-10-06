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
            row = [1]  # First element is always 1
            if row_number > 1:
                # Generate the intermediate values
                previous_row = result[row_number - 2]
                for i in range(1, row_number - 1):
                    val_to_add = previous_row[i - 1] + previous_row[i]
                    row.append(val_to_add)
                row.append(1)  # Last element is always 1

            result.append(row)

        return result
