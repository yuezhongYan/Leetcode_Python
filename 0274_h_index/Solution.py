from random import randrange


class Solution(object):
    def hIndex(self, citations):
        """Find h_index using quick sort and sequential search
        Given an array of citations (each citation is a non-negative integer) of a researcher, compute the
        researcher's h-index.
        A scientist has index h if h of his/her N papers have at least h citations each, and the other
        N - h papers have no more than h citations each.

        This algorithm has 2 steps to compute h-index:
        1. Sort citations array in reversed order.
        2. Traverse the sorted array. If the current citation is greater than the current index, h-index
        increments.

        The time complexity for reversed quick sort is O(n log n) in average case, O(n^2) in the worst
        case if the pivot in reversed quick sort is always picked at both ends. The time complexity for
        traversal is O(n). Thus, the total time complexity is O(n log n) + O(n) = O(n log n).

        :type citations: List[int]
        :rtype: int
        """
        size = len(citations)

        def reversed_quick_sort(citations, start, end):
            if start >= end:
                return

            pivot_index = randrange(end - start + 1) + start
            pivot = citations[pivot_index]

            # Swap citations[pivot_index] with citations[start]. Now the pivot is on the
            # left.
            citations[pivot_index], citations[start] = citations[start], citations[pivot_index]

            left = start + 1
            right = end

            # Partition
            while left <= right:
                while left <= right and citations[left] > pivot:
                    left += 1

                while left <= right and citations[right] <= pivot:
                    right -= 1

                if left < right:
                    # Swap citations[left] with citations[right].
                    citations[left], citations[right] = citations[right], citations[left]

                    left += 1
                    right -= 1

            # Swap citations[start] with citations[right]. Now the pivot is
            # citations[right].
            citations[start], citations[right] = citations[right], citations[start]

            reversed_quick_sort(citations, start, right - 1)
            reversed_quick_sort(citations, right + 1, end)

        reversed_quick_sort(citations, 0, size - 1)

        # Traverse the reversed-ordered citations. If the current citation is greater than
        # the current index, h index increments.
        h_index = 0
        for i in range(size):
            if citations[i] > i:
                h_index += 1

        return h_index


solution = Solution()
print(solution.hIndex(citations=[3, 0, 6, 1, 5]))
