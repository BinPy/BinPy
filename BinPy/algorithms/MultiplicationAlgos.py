"""
This module implements various types of multipliers using algorithms like Booth's and Robertson's
"""

from bitstring import *
from BinPy.algorithms.bittools import *
import sys
import random
import itertools


class BoothsMultiplier(object):

    """
    This class implements various types of mulipliers using different algorithms used in study, analysis
    or practical implementation of Computer archetectures.
    """

    @staticmethod
    def booths_multiply(multiplicand, multiplier, bits, signed=False):
        """
        Multiply the multiplicand ( binary represented ) and multiplier ( binary represented )
        based on Booth's multiplication algorithm.
        If signed is set to true the input_data is assumed to be in a signed binary representation

        The result is a signed binary string representing the product.

        USAGE:

        # Unsigned multiplication
        >>> Multipliers.booths_multiply('101', '111', 5, signed=False)
        '0000100011'

        # Passing 2s Complement Signed binary string
        >>> product = Multiplier.booths_multiply('0101','1001', 5, signed=True)
        >>> print ( product )
        '1111011101'
        >>> BitTools.to_signed_int(product)
        -35

        # Passing - signed binary string
        >>> product = Multiplier.booths_multiply('101','-111', 5)
        >>> print ( product )
        '1111011101'
        >>> BitTools.to_signed_int(product)
        -35

        """

        multiplicand = BitTools.to_BitArray(multiplicand, bits, signed)
        multiplier = BitTools.to_BitArray(multiplier, bits, signed)

        product = BitArray(int=0, length=bits)
        product += multiplier
        prev_bit = "0"
        multiplicand += BitArray(int=0, length=bits)

        for i in range(bits):
            check = product.bin[-1] + prev_bit
            if check == "01":
                product.int += multiplicand.int

            if check == "10":
                product.int -= multiplicand.int

            prev_bit = product.bin[-1]
            product.int >>= 1

        return product.bin
