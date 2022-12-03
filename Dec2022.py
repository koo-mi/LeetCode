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
    """
    Question 121 - Best Time to Buy and Sell Stock
    2022-12-03
    """
    def maxProfit1(self, prices: list[int]) -> int:
        # First approach but time limit exceeded
        output = 0
        for index, value in enumerate(prices):
            for i in range(index+1, len(prices)):
                if prices[i] - value > output:
                    output = prices[i] - value
        return output

    def maxProfit2(self, prices: list[int]) -> int:
        # Second approach but time limit exceeded
        output = 0
        d_prices = prices.copy()
        for i in range(len(prices)-1):
            d_prices.pop(0)
            val = max(d_prices) - prices[i]
            if val > output:
                output = val
        return output

    def maxProfit3(self, prices: list[int]) -> int:
        # Third approach
        left, right = 0, 1  # Buy, Sell
        output = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                val = prices[right]-prices[left]
                if output < val:
                    output = val
            else:
                left = right
            right += 1
        return output

