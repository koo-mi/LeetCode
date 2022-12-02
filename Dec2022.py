"""
Question 118 - Pascal's Triangle
2022-12-02
"""

class Solution:
    def generate(self, numRows: int):
        # Result for the first two rows
        if numRows == 1:
            li = [[1]]
            return li
        else:
            li = [[1], [1, 1]]
            if numRows == 2:
                return li
                # Adding elements
        for i in range(2, numRows):
            li2 = []

            # first number is always 1
            li2.insert(0, 1)

            # Add the middle numbers by the order
            for j in range(2, i + 1):
                num = li[i - 1][j - 2] + li[i - 1][j - 1]
                li2.append(num)

            # Last number is always 1
            li2.append(1)
            li.append(li2)
        return li

