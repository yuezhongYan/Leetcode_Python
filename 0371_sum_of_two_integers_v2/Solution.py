class Solution(object):
    def getSum(self, a, b):
        """Calculate the sum of two integers a and b without "+" or "-" sign

        Use XOR to calculate sum without carry (i.e. a XOR b) as well as AND and << to
        calculate carry (i.e. (a AND b) << 1).  Use 32 bits because Leetcode performs 32
        bits. However, Python does not have restrictions on overflow. For example, 2^32
        in decimal is 0x100000000 in hex-decimal and
        1 1111 1111 1111 1111 1111 1111 1111 1111 in binary, but for other languages, it
        may cause an overflow. In Python, keep using modular operation to obtain the
        value of two integers in replace of those integers in the last round until
        carry = 0. Finally, we compare the sum with max integer for 32 bits. If it is
        less than this integer (i.e. not overflow), then return the sum. Otherwise,
        calculate negation of sum of ((a modulo min integer) XOR max integer).

        :type a: int
        :type b: int
        :rtype: int
        """
        # 2 ^ 32, use this number to do modulo operation to mimic to avoid overflow in
        # 32 bits. The reason why I do not pick 2 ^ 32 - 1 (0xFFFFFFFF in hex) is that
        # this number is not overflow yet in the range of [-(2 ^ 32), 2 ^ 32 - 1].
        MASK = 0x100000000

        while b != 0:
            addition_without_carry = a ^ b
            carry = (a & b) << 1

            # The reason to do modulo operation is to avoid overflow. Note that Python does
            # not have overflow so we have to mimic. Or the while loop has a dead cycle.
            a = addition_without_carry % MASK
            b = carry % MASK

        # Note that if we use the most significant bit for the sign of the number, then
        # we have 31 bits remaining. So we have the range of [-(2 ^ 31), 2 ^ 31 - 1],
        # which refers to [-0x80000000, 0x7FFFFFFF] in hex-decimal. A simple example is
        # that [-128, 127] = [-2 ^ 7, 2 ^ 7 - 1].
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1

        if a <= MAX_INT:
            return a
        else:
            # Represent a negative number for 32 bits when overflow. For example, if
            # a = 2 ^ 31 + 1 = 1000 0000 0000 0000 0000 0000 0000 0001 in binary with 32
            # bits, then a % MIN_INT = 1 = 0000 0000 0000 0000 0000 0000 0000 0001 in
            # binary with 32 bits.
            # (a % MIN_INT) ^ MAX_INT = 1 0000 0000 0000 0000 0000 0000 0000 0001 in binary
            # with 33 bits.
            # ~((a % MIN_INT) ^ MAX_INT) = 0 1111 1111 1111 1111 1111 1111 1111 1110 in
            # binary with 33 bits.
            return ~((a % MIN_INT) ^ MAX_INT)
