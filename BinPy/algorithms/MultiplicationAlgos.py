"""
This module implements various types of multipliers using algorithms like Booth's and Robertson's
"""
from BinPy.bittools.bittools import *
import itertools


def booths_multiply(multiplicand, multiplier, bits=None, signed=False):
    """
    Multiply the multiplicand ( binary represented ) and multiplier ( binary represented )
    based on Booth's multiplication algorithm.
    If signed is set to true the input_data is assumed to be in a signed binary representation

    The result is a signed binary string representing the product.

    USAGE:

    # Unsigned multiplication
    >>>  booths_multiply('101', '111', 5, signed=False)
    '0000100011'

    # Passing 2s Complement Signed binary string
    >>> product = booths_multiply('0101','1001', 5, signed=True)
    >>> print ( product )
    '1111011101'
    >>> to_signed_int(product)
    -35

    # Passing - signed binary string
    >>> product = booths_multiply('101','-111', 5)
    >>> print ( product )
    '1111011101'
    >>> to_signed_int(product)
    -35

    """

    if bits is None:

        # DEV NOTE: Do not replace 0b in the inputs, the BinPyBits will
        # handle the same.

        if not signed:
            if "0b" not in multiplier:
                multiplier = multiplier.lstrip("0")

            if "0b" not in multiplicand:
                multiplicand = multiplicand.lstrip("0")

        bits = max(len(multiplier), len(multiplicand))

        if bits == len(multiplier) and "0b" in multiplier:
            bits -= 2

        elif bits == len(multiplicand) and "0b" in multiplicand:
            bits -= 2

        if bits == 0:
            bits = 1

    len_input = bits

    multiplicand = BinPyBits(multiplicand, bits, signed)
    multiplier = BinPyBits(multiplier, bits, signed)

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


def robertsons_multiply(multiplicand, multiplier, bits=None, signed=False):
    """
    Multiply the multiplicand ( binary represented ) and multiplier ( binary represented )
    based on Robertson's multiplication algorithm.
    If signed is set to true the input_data is assumed to be in a signed binary representation

    The result is a signed binary string representing the product.

    USAGE:

    # Unsigned multiplication
    >>>  robertsons_multiply('101', '111', 5, signed=False)
    '0000100011'

    # Passing 2s Complement Signed binary string
    >>> product =  robertsons_multiply('0101','1001', 5, signed=True)
    >>> print ( product )
    '1111011101'
    >>> to_signed_int(product)
    -35

    # Passing - signed binary string
    >>> product =  robertsons_multiply('101','-111', 5)
    >>> print ( product )
    '1111011101'
    >>> to_signed_int(product)
    -35

    """

    if bits is None:

        # DEV NOTE: Do not replace 0b in the inputs, the BinPyBits will
        # handle the same.

        if not signed:
            if "0b" not in multiplier:
                multiplier = multiplier.lstrip("0")

            if "0b" not in multiplicand:
                multiplicand = multiplicand.lstrip("0")

        bits = max(len(multiplier), len(multiplicand))

        if bits == len(multiplier) and "0b" in multiplier:
            bits -= 2

        elif bits == len(multiplicand) and "0b" in multiplicand:
            bits -= 2

        if bits == 0:
            bits = 1

    len_input = bits

    bits += 1

    multiplicand = BinPyBits(multiplicand, bits, signed)
    multiplier = BinPyBits(multiplier, bits, signed)

    product = BitArray(int=0, length=bits)
    product += multiplier

    multiplicand += BitArray(int=0, length=bits)

    # Create a Bit Vector with length 1 greater than the length of product array
    # To handle overflow due to addition or subtraction

    addition_result = BitArray(int=0, length=bits * 2 + 1)

    for i in range(bits - 1):

        if product.bin[-1] == "1":

            addition_result.int = product.int + multiplicand.int
            # Neglecting the carry and hence handling the overflow ( if it
            # occurs)
            product.bin = addition_result.bin[1:]

        product.int >>= 1

    if product.bin[-1] == "1":
        addition_result.int = product.int - multiplicand.int
        # Setting the last bit to 0 and ignoring the first bit
        product.bin = addition_result.bin[1:]

    # Do a final right shift
    product.int >>= 1

    len_result = 2 * len_input

    return BinPyBits(product.bin, len_result, signed).bin


def karatsuba_multiply(multiplier, multiplicand, bits=None, signed=False):
    """
    Multiply the multiplicand ( binary represented ) and multiplier ( binary represented )
    based on Karatsuba fast multiplication algorithm.
    If the signed is True, the input_data is assumed to be in a signed binary representation.

    The result is a signed binary string representing the product.

    USAGE:

    # Both Positive inputs
    >>>  karatsuba_multiply('0101', '0111')
    '0000100011'

    # Passing 2s Complement Signed binary string as one input
    >>> product =  karatsuba_multiply('0101','1001')
    >>> print ( product )
    '1111011101'
    >>> to_signed_int(product)
    -35

    # Passing - signed binary string
    >>> product =  karatsuba_multiply('101','-111')
    >>> print ( product )
    '1111011101'
    >>> to_signed_int(product)
    -35

    """

    if bits is None:

        # DEV NOTE: Do not replace 0b in the inputs, the BinPyBits will
        # handle the same.

        if not signed:
            if "0b" not in multiplier:
                multiplier = multiplier.lstrip("0")

            if "0b" not in multiplicand:
                multiplicand = multiplicand.lstrip("0")

        bits = max(len(multiplier), len(multiplicand))

        if bits == len(multiplier) and "0b" in multiplier:
            bits -= 2

        elif bits == len(multiplicand) and "0b" in multiplicand:
            bits -= 2

        if bits == 0:
            bits = 1

    multiplicand = BinPyBits(multiplicand, bits, signed)
    multiplier = BinPyBits(multiplier, bits, signed)

    sign_bit = None

    if (signed):
        # The following set of operations will run only during the first
        # pass, if the signed is set to True

        # Calculating the sign of the product
        if ((multiplicand.bin[0] == "1") ^ (multiplier.bin[0] == "1")):
            sign_bit = 1
        else:
            sign_bit = 0

        # Strip off the sign bit and convert to a BitArray with unsigned
        # binary string.
        multiplicand = BinPyBits(
            abs(multiplicand.int), bits, signed=False)
        multiplier = BinPyBits(
            abs(multiplier.int), bits, signed=False)

    # Base case of 0 bit multiplication. If length is 0 product is 0.
    if len(multiplier.bin) == 0 or len(multiplicand.bin) == 0:
        return "0"

    # Base case of 1 bit multiplication
    if len(multiplier) == 1:
        return "1" if (
            multiplier.bin == "1" and multiplicand.bin == "1") else "0"

    m = int(bits / 2)

    # x = x1*(2**m) + x0
    # y = y1*(2**m) + y0

    x1 = multiplicand.bin[:m]
    x0 = multiplicand.bin[m:]

    y1 = multiplier.bin[:m]
    y0 = multiplier.bin[m:]

    # Upper half of the bits
    z2 = karatsuba_multiply(x1, y1)
    # Lower half of the bits
    z0 = karatsuba_multiply(x0, y0)

    # ( x1 + x0 )( y1 + y0 )
    sum_term1 = int(x1, 2) + int(x0, 2)
    sum_term1 = bin(sum_term1).replace("0b", "").lstrip("0")

    sum_term2 = int(y1, 2) + int(y0, 2)
    sum_term2 = bin(sum_term2).replace("0b", "").lstrip("0")

    z1 = karatsuba_multiply(sum_term1, sum_term2)
    z1 = bin(int(z1, 2) - int(z2, 2) - int(z0, 2))

    # The "0" padding at the right is binary equivalent of left shift or
    # muliply with 2**bits
    abs_result = int((z2 + "0" * (2 * (bits - m))),
                     2) + int((z1 + "0" * (bits - m)),
                              2) + int(z0,
                                       2)

    # len_result = 2*length of multiplicand / multiplier
    len_result = 2 * bits

    # Converting to binary of 2ce the bit length of inputs
    abs_result = BinPyBits(abs_result, len_result, signed=False)

    if sign_bit == 1:
        abs_result.int *= -1

    return abs_result.bin


def toom3_multiply(multiplier, multiplicand, bits=None, signed=False):
    """
    Multiply the multiplicand ( binary represented ) and multiplier ( binary represented )
    based on Toom Cook's multiplication algorithm - ( Toom-3; Km = Kn = 3 ).
    If the signed is True, the input_data is assumed to be in a signed binary representation.

    The result is a signed binary string representing the product.

    USAGE:

    # Both Positive inputs
    >>>  toom3_multiply('0101', '0111')
    '0000100011'

    # Passing 2s Complement Signed binary string as one input
    >>> product =  toom3_multiply('0101','1001')
    >>> print ( product )
    '1111011101'
    >>> to_signed_int(product)
    -35

    # Passing - signed binary string
    >>> product =  toom3_multiply('101','-111')
    >>> print ( product )
    '1111011101'
    >>> to_signed_int(product)
    -35

    """

    # print multiplicand, multiplier

    if bits is None:

        # DEV NOTE: Do not replace 0b in the inputs, the BinPyBits will
        # handle the same.

        if not signed:
            if "0b" not in multiplier:
                multiplier = multiplier.lstrip("0")

            if "0b" not in multiplicand:
                multiplicand = multiplicand.lstrip("0")

        bits = max(len(multiplier), len(multiplicand))

        if bits == len(multiplier) and "0b" in multiplier:
            bits -= 2

        elif bits == len(multiplicand) and "0b" in multiplicand:
            bits -= 2

        if bits == 0:
            bits = 1

    len_input = bits

    while bits % 3 != 0:
        bits += 1

    multiplicand = BinPyBits(multiplicand, bits, signed)
    multiplier = BinPyBits(multiplier, bits, signed)

    sign_bit = None

    if (signed):
        # The following set of operations will run only during the first
        # pass, if the signed is set to True

        # Calculating the sign of the product
        if ((multiplicand.bin[0] == "1") ^ (multiplier.bin[0] == "1")):
            sign_bit = 1
        else:
            sign_bit = 0

        # Strip off the sign bit and convert to a BitArray with unsigned
        # binary string.
        multiplicand = BinPyBits(
            abs(multiplicand.int), bits, signed=False)
        multiplier = BinPyBits(
            abs(multiplier.int), bits, signed=False)

    # Base case of 0 bit multiplication. If length is 0 product is 0.
    if len(
            multiplier.bin.lstrip("0")) == 0 or len(
            multiplicand.bin.lstrip("0")) == 0:
        return "0"

    # Base case of 1 bit multiplication
    if len(multiplier.bin.lstrip("0")) == 1:
        return "1" if (
            multiplier.bin[-1] == "1" and multiplicand.bin[-1] == "1") else "0"

    m = int(bits / 3)

    B = 2 ** m

    # x = x2*(B**2) + x1*(B) + x0 <= p(x = B)
    # y = y2*(B**2) + y1*(B) + y0 <= q(x = B)

    x2 = BinPyBits(multiplicand.bin[:m])
    x1 = BinPyBits(multiplicand.bin[m:2 * m])
    x0 = BinPyBits(multiplicand.bin[2 * m:])

    y2 = BinPyBits(multiplier.bin[:m])
    y1 = BinPyBits(multiplier.bin[m:2 * m])
    y0 = BinPyBits(multiplier.bin[2 * m:])

    # Multipoint coefficient evaluation using Marco Bodrato's sequence

    # p is the multipoint dict of cartesian pairs for the multiplicand polynomial
    # q is the multipoint dict of cartesian pairs for the multiplier polynomial

    p = {}
    q = {}

    p_o = BinPyBits(x0.uint + x2.uint)

    p[0] = x0
    p[1] = BinPyBits(p_o.uint + x1.uint)
    p[-1] = BinPyBits(p_o.uint - x1.uint)  # Can be negative
    p[-2] = BinPyBits(2 * (p[-1].uint + x2.uint) - x0.uint)  # Can be negative
    p['inf'] = x2

    q_o = BinPyBits(x0.uint + x2.uint)

    q[0] = x0
    q[1] = BinPyBits(q_o.uint + x1.uint)
    q[-1] = BinPyBits(q_o.uint - x1.uint)  # Can be negative
    q[-2] = BinPyBits(2 * (q[-1].uint + x2.uint) - x0.uint)  # Can be negative
    q['inf'] = x2

    # Calculating pointwise multiplication - Recursively calling toom3 for
    # smaller part multiplications

    r = {}

    # print p, q

    r[0] = BinPyBits(toom3_multiply(p[0].bin, q[0].bin))
    r[1] = BinPyBits(toom3_multiply(p[1].bin, q[1].bin))
    r[-1] = BinPyBits(toom3_multiply(p[-1].bin, q[-1].bin))
    r[-2] = BinPyBits(toom3_multiply(p[-2].bin, q[-2].bin))
    r['inf'] = BinPyBits(toom3_multiply(p['inf'].bin, q['inf'].bin))

    # Interpolating the points to the product polynomial
    # Using Marco Bodrato's sequence
    # Integer ( may be negative too ) result of the point multiplication is
    # used to interpolate

    r0 = r[0].int
    r4 = r['inf'].int
    r3 = (r[-2].int - r[1].int) / 3
    r1 = (r[1].int - r[-1].int) / 2
    r2 = r[-1].int - r[0].int
    r3 = (r2 - r3) / 2 + 2 * r['inf']
    r2 = r2 + r1 - r4
    r1 = r1 - r3

    product = r4 * (4 * B) + r3 * (3 * B) + r2 * (2 * B) + r1 * (B) + r0

    product = BinPyBits(product, 2 * len_input)

    if sign_bit == 1:
        product.int *= -1

    return product.bin
