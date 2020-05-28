class Solution(object):
    def missingNumber(self, nums):
        """Find the missing number with XOR bit operation
        Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
        the one that is missing from the array.

        Because we know that nums contains n numbers and that it is missing exactly
        one number on the range [0..n-1], we know that n definitely replaces the
        missing number in nums. Therefore, if we initialize an integer to n and XOR it
        with every index and value, we will be left with the missing number.
        Mathematically, it is n = n ^ (nums[i] ^ i), where i is the counter for nums.

        e.g., nums = {3, 0, 1}, then missing number is 2, which is n ^ (nums[i] ^ i)
        with n = 3 initially.

        Time complexity is O(n) in the worst case because it takes O(1) for each
        iteration.

        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        missing_number = len(nums)
        for i in range(size):
            missing_number ^= (i ^ nums[i])

        return missing_number
