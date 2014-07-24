from BinPy import *


def test_bittools():
    binary_string = "11011"

    # Giving an Unsigned binary string
    bit_array_object = BitTools.to_BitArray(binary_string, 8, signed=False)

    assert isinstance(bit_array_object, BitArray)
    assert bit_array_object.bin == "00011011"
    assert bit_array_object.int == 27

    # Giving a 2s complement input
    bit_array_signed = BitTools.to_BitArray(binary_string, 8, signed=True)

    assert bit_array_signed.bin == "11111011"
    assert bit_array_signed.int == -5

    # Giving an unsigned input with signed parameter set to True
    binary_string = "011011"
    bit_array_signed = BitTools.to_BitArray(binary_string, 8, signed=True)

    assert bit_array_signed.bin == "00011011"
    assert bit_array_signed.int == 27

    try:
        bit_array_signed = BitTools.to_BitArray(binary_string, 5, signed=True)
        assert False
        # The signed representation of positive number should contain a 0 padded at the start.
        # For 5 bit numbers with length given as 5, this should throw an error
        # since 0 padding cannot be done

    except:
        assert True

    # Giving a signed input with - sign ( Python signed binary )
    binary_string = bin(-5)

    bit_array_signed = BitTools.to_BitArray(binary_string, 8)
    # Passing signed will have no effect

    assert bit_array_signed.bin == "11111011"
    assert bit_array_signed.int == -5

    # Testing creation of BitArray with input binary string of 0 length
    assert repr(BitTools.to_BitArray('', 5)) == "BitArray('0b00000')"


def test_convertors():
    assert BitTools.to_unsigned_int("11111111") == 255
    assert BitTools.to_signed_int("11111111") == -1
    assert BitTools.to_signed_int("00000001") == 1
    assert BitTools.to_unsigned_int("00000001") == 1
