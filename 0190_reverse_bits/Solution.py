class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        """Reverse bits
        Returns the value obtained by reversing the order of the bits in the two's
        complement binary representation of the specified int value.

        Right-shift input value with m bits and do AND operation, then use the same
        input value, do AND operation, and do left-shift operation. Finally, apply OR
        operation to obtain the result and assign this result to the input value.

        Do the above step using m = 1, 2, 4, 8, 16.
        For AND operation, use
        m_1 = 01010101010101010101010101010101b
        m_2 = 00110011001100110011001100110011b
        m_4 = 00001111000011110000111100001111b
        m_8 = 00000000111111110000000011111111b
        m_16 = 00000000000000001111111111111111b
        to split bits into group of m.

        e.g., n = 43261596 = 00000010100101000001111010011100b
        n = ((n >> 1) & M1) | ((n & M1) << 1): = 00000001011010000010110101101100b

        Time complexity is O(1) in the worst case because it has total of 25 bit
        operations no matter how large the input value is.

        :param n: int
        :return: int
        """
        m_1 = 0x55555555  # binary: 01010101010101010101010101010101
        m_2 = 0x33333333  # binary: 00110011001100110011001100110011
        m_4 = 0x0F0F0F0F  # binary: 00001111000011110000111100001111
        m_8 = 0x00FF00FF  # binary: 00000000111111110000000011111111
        m_16 = 0x0000FFFF  # binary: 00000000000000001111111111111111

        # reverse evens and odds.
        n = ((n >> 1) & m_1) | ((n & m_1) << 1)

        # reverse consecutive pairs.
        n = ((n >> 2) & m_2) | ((n & m_2) << 2)

        # reverse 4-bit long pairs
        n = ((n >> 4) & m_4) | ((n & m_4) << 4)

        # reverse 8-bit long pairs
        n = ((n >> 8) & m_8) | ((n & m_8) << 8)

        # reverse 16-bit long pairs
        n = ((n >> 16) & m_16) | ((n & m_16) << 16)

        return n
