from BinPy.bittools.bittools import *


def test_bittools():
    binary_string = "11011"

    # Giving an Unsigned binary string
    bit_array_object = BinPyBits(binary_string, 8, signed=False)

    assert isinstance(bit_array_object, BinPyBits)
    assert isinstance(bit_array_object, BinPyBits)
    assert bit_array_object.bin == "00011011"
    assert bit_array_object.int == 27

    # Giving a 2s complement input
    bit_array_signed = BinPyBits(binary_string, 8, signed=True)

    assert bit_array_signed.bin == "11111011"
    assert bit_array_signed.int == -5

    # Giving an unsigned input with signed parameter set to True
    binary_string = "011011"
    bit_array_signed = BinPyBits(binary_string, 8, signed=True)

    assert bit_array_signed.bin == "00011011"
    assert bit_array_signed.int == 27

    try:
        bit_array_signed = BinPyBits(binary_string, 5, signed=True)
        assert False
        # The signed representation of positive number should contain a 0 padded at the start.
        # For 5 bit numbers with length given as 5, this should throw an error
        # since 0 padding cannot be done

    except:
        assert True

    try:
        bit_array_signed = BinPyBits(binary_string, 5, signed=False)
        # This should however work
        assert True
    except:
        assert False

    # Giving a signed input with - sign ( Python signed binary )
    binary_string = bin(-5)

    bit_array_signed = BinPyBits(binary_string, 8, signed=True)
    # Passing signed will have no effect

    assert bit_array_signed.bin == "11111011"
    assert bit_array_signed.int == -5

    # Testing creation of BinPyBits with input binary string of 0 length
    assert BinPyBits('', 5).bin == "00000"

    # Testing creation of BinPyBits from numerals
    try:
        assert BinPyBits(5, length=5, signed=False).bin == "00101"
    except:
        assert False

    try:
        assert BinPyBits(-3, length=5, signed=True).bin == "11101"
    except:
        assert False

    # Testing creation of BinPyBits without explicit length parameter
    assert BinPyBits(64).bin == "1000000"
    assert BinPyBits(64).signed is False
    assert BinPyBits(-64).bin == "1000000"
    assert BinPyBits(-64).signed

    try:
        assert BinPyBits().bin == ""
    except:
        assert False

    assert BinPyBits(0).length == 1

    assert BinPyBits("0011", length=3).bin == "011"
    assert BinPyBits("0011").bin == "0011"


def test_convertors():
    assert to_unsigned_int("11111111") == 255
    assert to_signed_int("11111111") == -1
    assert to_signed_int("00000001") == 1
    assert to_unsigned_int("00000001") == 1
