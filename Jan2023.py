class Solution:
    """
    Question 217 - Contains Duplicate
    2022-01-11
    """
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set(nums)
        if len(s) == len(nums):
            return False
        else:
            return True

    def containsDuplicate2(self, nums: list[int]) -> bool:
        s = {}
        for i in nums:
            if i in s:
                return True
            else:
                s[i] = 1
        return False

    def containsDuplicate3(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
