class Solution(object):
    def countBits(self, num):
        """Count the number of 1's for every integer i in [0, num]
        Given a non-negative integer num, count the number of 1's for every integer i in
        [0, num]. Return them as an array. Time complexity is O(n), where while loop
        takes O(n) and count_number_of_ones() takes O(1).

        :type num: int
        :rtype: List[int]
        """

        def count_number_of_ones(self, number):
            """Count the number of 1's for a given number
            This method is the same as Problem 191 with Hamming Weight.
            Refer: https://en.wikipedia.org/wiki/Hamming_weight

            :param self: Solution class
            :param number: given number
            :return: the number of 1's for the given number
            """
            m_1 = 0x55555555  # binary: 01010101010101010101010101010101
            m_2 = 0x33333333  # binary: 00110011001100110011001100110011
            m_4 = 0x0F0F0F0F  # binary: 00001111000011110000111100001111
            m_8 = 0x00FF00FF  # binary: 00000000111111110000000011111111
            m_16 = 0x0000FFFF  # binary: 00000000000000001111111111111111

            number = (number & m_1) + ((number >> 1) & m_1)
            number = (number & m_2) + ((number >> 2) & m_2)
            number = (number & m_4) + ((number >> 4) & m_4)
            number = (number & m_8) + ((number >> 8) & m_8)
            number = (number & m_16) + ((number >> 16) & m_16)

            return number

        result = []

        i = 0
        while i <= num:
            number_of_ones = count_number_of_ones(self, i)
            result.append(number_of_ones)
            i += 1

        return result
