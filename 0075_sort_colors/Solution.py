from random import randint


def quick_sort(nums, start, end):
    """Implement quick sort

    :param nums: given array
    :param start: start index of given array
    :param end: end index of given array
    :return: nothing returned, modify nums in-place instead
    """
    if start >= end:
        return

    pivot_index = randint(0, end - start) + start
    pivot = nums[pivot_index]

    left = start + 1
    right = end

    # Swap 0th element with pivot. Now the pivot is nums[start].
    nums[start], nums[pivot_index] = nums[pivot_index], nums[start]

    # Partition
    while left <= right:
        # Find the first element that is greater than the pivot.
        while left <= right and nums[left] <= pivot:
            left += 1

        # Find the last element that is smaller than or equal to the pivot.
        while left <= right and nums[right] > pivot:
            right -= 1

        if left < right:
            # Swap nums[left] and nums[right]
            nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right -= 1

    # Swap nums[right] with 0th element. Now pivot is nums[right].
    nums[start], nums[right] = nums[right], nums[start]

    quick_sort(nums, start, right - 1)
    quick_sort(nums, right + 1, end)


class Solution(object):
    def sortColors(self, nums):
        """Sort colors represented with integers through quick sorting algorithm
        Time complexity of quick sort is O(n log n) in average and O(n^2) is the worst
        case.

        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        quick_sort(nums, 0, len(nums) - 1)
