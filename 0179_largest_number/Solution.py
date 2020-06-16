class Solution(object):
    def largestNumber(self, nums):
        """Arrange non negative integers such that they form the largest number
        Given a list of non negative integers, arrange them such that they form the largest number with
        merge sort.

        e.g., Input: [3,30,34,5,9]
              Output: "9534330"

        Time complexity is O(n log n) because merge sort takes O(n log n) in the worst case.

        :type nums: List[int]
        :rtype: str
        """
        # Handle the case where all numbers are 0's. Here, the output is 0.
        if all(value == 0 for value in nums):
            return "%s" % 0

        def merge_sort(nums, left, right):
            """Implement merge sort

            :param nums: given non negative integers
            :param left: left pointer of the given non negative integers
            :param right: right pointer of the given non negative integers
            :return:
            """
            if len(nums) < 2:
                return

            # Create left sub-array.
            left_sub_array_size = len(nums) >> 1
            left_sub_array = []
            for i in range(0, left_sub_array_size):
                left_sub_array.append(nums[i])

            # Create right sub-array
            right_sub_array_size = len(nums) - left_sub_array_size
            right_sub_array = []
            for i in range(0, right_sub_array_size):
                right_sub_array.append(nums[i + left_sub_array_size])

            middle = left + (right - left) >> 1
            merge_sort(left_sub_array, left, middle)
            merge_sort(right_sub_array, middle + 1, right)

            def merge(left_sub_array, left_sub_array_size, right_sub_array,
                      right_sub_array_size, result):
                """Implement modified merge

                :param left_sub_array: left sub-array
                :param left_sub_array_size: left sub-array size
                :param right_sub_array: right sub-array
                :param right_sub_array_size: right sub-array size
                :param result: result array containing the elements from left sub-array and right sub-array sorted
                :return:
                """
                # index for left sub-array
                i = 0

                # index for right sub-array
                j = 0

                # index for result array
                k = 0

                def compare(number_from_left, number_from_right):
                    """Compare combinations of the number from left sub-array with the one from right
                    If the combination of the number from left sub-array and the one from right is greater than the
                    combination of the number from right sub-array and the one from left, return true. Otherwise return
                    false.

                    :param number_from_left: number from left sub-array
                    :param number_from_right: number from right sub-array
                    :return: true if the left-right combination is greater than the right-left one, false otherwise
                    """
                    as_string_left_number = "%s" % number_from_left
                    as_string_right_number = "%s" % number_from_right

                    left_right_combination = "%s%s" % (as_string_left_number, as_string_right_number)
                    right_left_combination = "%s%s" % (as_string_right_number, as_string_left_number)

                    return long(left_right_combination) > long(right_left_combination)

                while i < left_sub_array_size and j < right_sub_array_size:
                    # Implement modified merging process with compare method that obtains the larger combination.
                    # e.g., Input: [3, 30], then there are two combinations, 330 and 303. To obtain 330, 3 comes into
                    # result array first then 30.
                    if compare(left_sub_array[i], right_sub_array[j]):
                        # Move the elements of left sub-array at the end of result
                        result[k] = left_sub_array[i]
                        i += 1
                    else:
                        # Move the elements of right sub-array at the end of result
                        result[k] = right_sub_array[j]
                        j += 1
                    k += 1

                # Move the remaining elements of left sub-array to result
                while i < left_sub_array_size:
                    result[k] = left_sub_array[i]
                    i += 1
                    k += 1

                # Move the remaining elements of right sub-array to result
                while j < right_sub_array_size:
                    result[k] = right_sub_array[j]
                    j += 1
                    k += 1

            merge(left_sub_array, left_sub_array_size, right_sub_array,
                  right_sub_array_size, nums)

        merge_sort(nums, 0, len(nums) - 1)

        return ''.join(map(str, nums))


solution = Solution()
nums = [3, 30, 34, 5, 9]
print(solution.largestNumber(nums))
