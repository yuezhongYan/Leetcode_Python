from Solution import Solution


def main():
    """runs solution method

    """
    solution = Solution()
    nums = [3, 4, 5, 1, 2]
    print(solution.findMin(nums))


class SolutionTest(object):
    """Test solution

    """
    if __name__ == '__main__':
        main()
