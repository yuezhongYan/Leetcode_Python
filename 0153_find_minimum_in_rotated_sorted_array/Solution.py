class Solution(object):
    def findMin(self, nums):
        """Find minimum value of a rotated sorted list

        Retrieve the minimum value of a rotated sorted list using modified binary
        search. If the size of the list is 1 or if the first element is less than
        the last(i.e. sorted list without being rotated), the minimum value is 1.
        Compare the middle element with the last. If the middle element is greater than
        the last, then the turning point is at the right of the middle element.
        Otherwise, it is at the left of that. If the middle element is greater than its
        next one, then the minimum value is the next element. If the middle element is
        less than its previous one, then the minimum value is the middle element.

        :arg self: class Solution itself
             nums: given list consisting of ints

        :returns minimum_value: the minimum value of given list

        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums) - 1
        minimum_value = -1

        # If the list has just 1 element or if the last element is greater than the
        # first(i.e. no rotation), hence the smallest element is the first element,
        # A[0]. e.g, 1 < 2 < 3 < 4 < 5. Already sorted array.
        if len(nums) == 1 or nums[i] < nums[j]:
            return nums[i]

        # Binary search
        while i < j:
            middle = (i + j) >> 1

            # If the middle element is greater than the last, this means the least value is
            # on the right of the middle element.
            if nums[middle] > nums[j]:
                i = middle + 1

            # If the middle element is smaller than the last, this means the least value is
            # on the left of the middle element.
            else:
                j = middle - 1

            # If the middle element is greater than its next element, then the next element
            # is the smallest.
            if nums[middle] > nums[middle + 1]:
                minimum_value = nums[middle + 1]
                break

            # If the middle element is smaller than its previous element, then the middle
            # element is the smallest.
            if nums[middle] < nums[middle - 1]:
                minimum_value = nums[middle]
                break

        return minimum_value
