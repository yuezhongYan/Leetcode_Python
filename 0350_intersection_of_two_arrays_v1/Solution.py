from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        """Given two arrays, compute their intersection
        Given two arrays, write a function to compute their intersection. Each element in the result should
        appear as many times as it shows in both arrays.

        This algorithm applies collections.Counter() and has following steps:
        1. Store key-value pairs where key is the element from the given array and value is the frequency
        of each element. Do this step for both given arrays.
        2. Create a list to store the intersection of both given arrays.
        3. For each key in key-value pairs for the first given array. Check if the key is contained in the
        second. If yes, extract the smaller frequency(value) between the two frequencies as well as the key.
        Store the key into the list for x times, where x = the smaller number of frequencies.

        Time complexity for this algorithm is O(nk), where n is the size of the first given array and k is
        the size of iterables to extend.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Store the key-value pairs where key is the element from nums1 and value is the
        # frequency of each element
        nums1_counter = Counter(nums1)

        # Store the key-value pairs where key is the element from nums2 and value is the
        # frequency of each element
        nums2_counter = Counter(nums2)

        intersection = []

        for key in nums1_counter:
            if key in nums2_counter:
                # Combine another iterable [key] in intersection list. Min() extracts the
                # smaller number of frequencies for the key. Finally add the key to
                # intersection list for (smaller-number-of-frequencies) times.
                intersection.extend([key] * min(nums1_counter[key], nums2_counter[key]))

        return intersection


solution = Solution()
print(solution.intersect(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
