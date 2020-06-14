class Solution(object):
    def maximumGap(self, nums):
        """Find the maximum gap in sorted nums
        Use least-significant digit radix sort to sort the array. Then find the maximum
        gap. Time complexity is O(n * k), where k is the number of digits that the
        maximum number has, which is a constant.

        :type nums: List[int]
        :rtype: int
        """
        max_gap = 0
        size = len(nums)
        if size < 2:
            return max_gap

        def least_significant_radix_sort(array, size):
            max_number = max(array)

            # 10 digits
            RADIX = 10

            bucket = [[] for i in range(RADIX)]
            divisor = 1

            while max_number / divisor > 0:

                # Append specified elements in array to designated location of bucket
                for element in array:
                    digit = (element / divisor) % 10
                    bucket[digit].append(element)

                # Array to store elements in bucket
                array_to_store_elements_in_bucket = []

                # Store elements in bucket to array_to_store_elements_in_bucket
                for element in bucket:
                    array_to_store_elements_in_bucket.extend(element)

                # Copy back to array from array_to_store_elements_in_bucket
                for element in range(size):
                    array[element] = array_to_store_elements_in_bucket[element]

                # Clear current bucket by creating a new one
                bucket = [[] for i in range(RADIX)]

                divisor *= 10

            return

        least_significant_radix_sort(nums, size)

        max_gap = nums[1] - nums[0]
        for i in range(2, size):
            max_gap = max(max_gap, nums[i] - nums[i - 1])

        return max_gap


solution = Solution()
nums = [9, 6, 3, 1]

result = solution.maximumGap(nums)
print(result)
