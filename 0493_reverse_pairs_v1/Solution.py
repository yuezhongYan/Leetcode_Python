class Solution(object):
    def reversePairs(self, nums):
        """
        Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

        Divide the array into 2 sub-arrays until each sub-array is single element long and merging these
        sublists recursively that results in the final sorted array.

        Modify mergeSort that takes parameters an array and left and right indices:
             -If left >= right, elements can no longer be broken further and hence return 0.
             -Otherwise, set middle = left + ((right - left) >> 1).
             -Store important_reverse_pair_count by recursively calling mergeSort on range [left,middle] and
              [mid+1,end] and adding the results. This is the divide step on our routine, breaking it into
              the 2 ranges, and finding the results for each range separately.
             -Now, we have separately calculated the results for ranges [start, middle] and
              [middle + 1, end], but we still have to count the elements in [start, middle] that are
              greater than 2 * elements in [middle + 1, end]. Count all such elements and add the result to
              important_reverse_pair_count.
             -Finally, merge the array from left to right.

        Total time complexity is O(n log n), where it takes O(log n) to divide the array into 2
        sub-arrays and O(n) to count the the number of important reverse pairs and to merge the 2
        sub-arrays after sorting.

        :type nums: List[int]
        :rtype: List[int]
        """

        def merge_sort(nums, left, right):
            if left >= right:
                return 0

            middle = left + ((right - left) >> 1)

            # Current count of important reverse pairs.
            result = 0

            result += merge_sort(nums, left, middle)
            result += merge_sort(nums, middle + 1, right)

            def merge(nums, left, middle, right):
                # Index for left sub-array
                i = left

                # Index for right sub-array
                j = middle + 1

                # Store merged array.
                merged_array = []

                # Current count of important reverse pairs.
                important_reverse_pair_count = 0

                # Obtain the total count of important reverse pairs. If the element from the
                # left sub-array is less than the one from the right sub-array, then the
                # index for the left sub-array increments. Otherwise, the index for the
                # right sub-array increments. Convert the elements from int to long from
                # both sub-arrays to avoid overflow.
                while i < middle + 1 and j < right + 1:
                    if long(nums[i]) > 2 * long(nums[j]):
                        important_reverse_pair_count += middle - i + 1
                        j += 1
                    else:
                        i += 1

                nums[left: right + 1] = sorted(nums[left: right + 1])

                return important_reverse_pair_count

            result += merge(nums, left, middle, right)
            return result

        return merge_sort(nums, 0, len(nums) - 1)


solution = Solution()
print(solution.reversePairs(nums=[1, 3, 2, 3, 1]))
