"""
The BitTools module consists of static methods to assist operations on binary string.
The bitstring package is used extensively to make the conversions efficient.
"""
from bitstring import *


class BitTools(object):

    # DEV NOTE : BitArray is the class name so pep8 naming ( bit_array ) is
    # not used

    @staticmethod
    def to_BitArray(input_data, bits, signed=False):
        """
        Returns a bit array object, from the input_data.
        Validation and exception handling is taken care of by this method, to assist in DRY coding principle
        """
        result = None

        if type(input_data) not in [str, int, BitArray]:
            raise TypeError(
                "Input must be given as integer or binary strings or bitarray objects")

        # Convert to Bit Array Objects
        if isinstance(input_data, int):
            result = BitArray(int=input_data, length=bits)
            # Sign is taken care by the sign of input_data

        elif isinstance(input_data, str):
            # Sign is decided by the "signed" parameter or - in the input_data
            # string

            input_data = input_data.replace("0b", "")

            if len(input_data) == 0:
                return BitArray(int=0, length=bits)

            # First priority to - in the string "-0b111" ( -7 )
            if "-" in input_data or ((input_data[0] == "1") and not signed) or (input_data[0] == "0"):
                result = BitArray(int=int(input_data, 2), length=bits)

            # Next priority to 2s complement signed binary explicitly mentined
            # as signed
            else:
                input_data = input_data.replace("-", "")
                length = len(input_data)
                mask = int(("1" * length), 2)
                input_data = (int(input_data, 2) ^ mask) + 1
                result = BitArray(int=-input_data, length=bits)

        else:
            raise TypeError(
                "Input  must be given as binary strings or integers.")

        return result

    @staticmethod
    def to_signed_int(signed_binary):
        """
        Converts 2s Complement Signed binary representation to signed integer

        USAGE

        >>> BitTools.to_signed_int("11111000")
        -8

        >>> BitTools.to_signed_int("01111111")
        127

        >>> BitTools.to_signed_int("11111111")
        -1
        """
        return BitArray(bin=signed_binary.replace("0b", "")).int

    # DEV NOTE: The following method not quite useful. Given just to give a sense of completion
    # to the purpose of this class and to give a method similar to
    # to_signed_int(binary_str)

    @staticmethod
    def to_unsigned_int(signed_binary):
        """
        Converts Unsigned binary representation to unsigned integer

        USAGE

        >>> BitTools.to_unsigned_int("11111000")
        248

        >>> BitTools.to_unsigned_int("01111111")
        127

        >>> BitTools.to_unsigned_int("11111111")
        255
        """
        return int(signed_binary, 2)
