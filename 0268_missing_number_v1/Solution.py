class Solution(object):
    def missingNumber(self, nums):
        """Find the missing number with sorting
        Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
        the one that is missing from the array.

        First, we sort nums. Then, we ensure that 0 is at the beginning and that n is
        at the end. The missing number must somewhere between (but not including) 0
        and n. To find it, we ensure that the number we expect to be at each index is
        indeed there. As soon as we find an unexpected number, we can simply return
        the expected number. Time complexity is O(n log n), where sort() takes
        O(n log n) and for loop takes O(n).

        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        size = len(nums)
        missing_number = -1
        is_break = 0

        # If we find the unexpected number, then the index is the missing number.
        for i in range(0, size):
            if nums[i] != i:
                missing_number = i
                is_break = 1
                break

        # Handle the sorted array with missing number being 0 or n.
        if is_break is 0:
            missing_number = size

        return missing_number
