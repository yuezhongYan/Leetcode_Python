class Solution(object):
    def intersection(self, nums1, nums2):
        """Find intersection of two arrays using set()
        Given two arrays, compute their intersection by following steps:
        1. Remove duplicates for given arrays.
        2. Compute their intersection.

        Total time complexity is O(min(n, m)), where n, m are the lengths of two given arrays.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list((set(nums1)).intersection(set(nums2)))


solution = Solution()
print(solution.intersection(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4]))
