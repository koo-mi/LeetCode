import re

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
        # Third approach - Successful
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

    """
    Question 125 - Valid Palindrome
    2022-02-04
    """
    def isPalindrome(self, s: str) -> bool:
        # Approach 1 - comparing each letter - Successful
        # leave only number / letters and make it lower case
        s1 = re.sub(r"[^0-9A-Za-z]", '', s).lower()

        # if the length is 0 or 1, return True
        if len(s1) == 0 or len(s1) == 1:
            return True
        # if the length is greater than 1, find the halfway point
        elif len(s1) % 2 == 0:
            half = len(s1) // 2
        else:
            half = len(s1) // 2 + 1

        # check if the forward and backward are the same
        for i in range(1, half+1):
            if s1[i-1] != s1[-i]:
                return False
        return True

    def isPalindrome2(self, s: str) -> bool:
        # taking different approach using slicing - Successful
        s1 = re.sub(r"[^0-9A-Za-z]", '', s).lower()

        if len(s1) == 0 or len(s1) == 1:
            return True
        elif len(s1) % 2 == 0:
            half = len(s1) // 2
        else:
            half = len(s1) // 2 + 1

        if s1[:half] == s1[::-1][:half]:
            return True
        else:
            return False

    """
    Question 136 - Single Number
    2022-12-05
    """
    def singleNumber(self, nums: list[int]) -> int:
        # Approach 1 using sets
        nums_c = nums.copy()
        origin = set(nums)

        for items in origin:
            nums_c.remove(items)

        output = list(origin.symmetric_difference(nums_c))[0]

        return output

    def singleNumber2(self, nums: list[int]) -> int:
        # Approach 2 by removing each element from the list
        if len(nums) % 2 == 0:
            rep = len(nums) // 2
        else:
            rep = len(nums) // 2 + 1

        for i in range(rep):
            output = nums[0]
            try:
                nums.remove(output)
                nums.remove(output)
            except:
                return output