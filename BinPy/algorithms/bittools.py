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

        input_data for signed numbers can be any one of the following :

        15 : 1111, signed = False
        15 : 01111, signed = True
        15 : 0b1111, signed = False
        15 : 0b01111, signed = True

        -7 : -0b111, signed = True
        -7 : -0b111, signed = False
        -7 : 1001, signed = True

        Prepending with 0b defaults the representation to unsigned, unless prepended by a -1

        i.e Do not give input_data as -7 : 0b1001, signed=True, it will be understood as +9

        """
        result = None

        if type(input_data) not in [str, int]:
            raise TypeError(
                "Input must be given as integer or binary strings or bitarray objects")

        # Convert to Bit Array Objects
        if isinstance(input_data, int):
            if signed:
                result = BitArray(int=input_data, length=bits)
                # Sign is taken care by the sign of input_data
            else:
                result = BitArray(uint=abs(input_data), length=bits)

        elif isinstance(input_data, str):
            # Sign is decided by the "signed" parameter or - in the input_data
            # string

            # Signed binary with 0b is understood by default
            # to be unsigned unless other wise prepended by -
            # DEV NOTE: This is so that input_data = bin(7), singed=True
            #           is not misinterpreted as -1
            #           But as a consequence -1 cannot be given as 0b111, signed = True
            #           It can be given as only as :
            #                                 -0b0001 or -0001
            #                                  1111, signed = True
            if "0b" in input_data:
                input_data = input_data.replace("0b", "")
                signed = False

            if len(input_data) == 0:
                return BitArray(int=0, length=bits)

            # First priority to - in the string "-0b111" ( -7 ) or a signed
            # binary number starting with 0
            if "-" in input_data or ((input_data[0] == "0") and signed):
                result = BitArray(int=int(input_data, 2), length=bits)

            # Next priority to 2s complement signed binary explicitly mentined
            # as signed and whose string does not contain 0b
            elif signed:
                input_data = input_data.replace("-", "")
                length = len(input_data)
                mask = int(("1" * length), 2)
                input_data = (int(input_data, 2) ^ mask) + 1
                result = BitArray(int=-input_data, length=bits)

            # Unsigned binary
            else:
                result = BitArray(uint=int(input_data, 2), length=bits)
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
