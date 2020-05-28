class Solution(object):
    def missingNumber(self, nums):
        """Find the missing number with set
        Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
        the one that is missing from the array.

        First, we insert nums into a hash set. Then, we use an identifier i that goes
        from 0 to n to check if i is in the hash set. The missing number must
        somewhere between (but not including) 0 and n. To find it, we ensure that the
        number we expect to be at each index is indeed there. As soon as we find an
        unexpected number, we can simply return the expected number. Time complexity
        is O(n), where insertion takes O(n) and for loop takes O(n) with contains()
        taking O(1) since it is a set. The sum of these operations is O(2n) => O(n).

        :type nums: List[int]
        :rtype: int
        """
        result_set = set()
        for i in nums:
            result_set.add(i)

        size = len(nums)
        missing_number = -1
        is_break = 0
        for i in range(size):
            if i not in result_set:
                missing_number = i
                is_break = 1
                break

        if is_break == 0:
            missing_number = size

        return missing_number
