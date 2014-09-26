from BinPy import *


def test_robertsons():

    # assert to_signed_int(
    # robertsons_multiply(bin(-7), bin(5), 4, signed=True)) == -35

    # assert to_signed_int(
    # robertsons_multiply(bin(-7), bin(-5), 4, signed=True)) == 35

    assert to_signed_int(
        robertsons_multiply(
            '111111',
            '111111',
            7)) == 3969

    assert to_signed_int(
        robertsons_multiply(
            '111111',
            '111111',
            5,
            signed=True)) == 1

    assert to_signed_int(
        robertsons_multiply(
            '1111',
            '0111',
            5,
            signed=False)) == 105

    assert to_signed_int(
        robertsons_multiply(
            '1111',
            '0111',
            5,
            signed=True)) == -7

    assert to_signed_int(
        robertsons_multiply(
            '-1',
            '0111',
            5,
            signed=True)) == -7

    try:
        # If no of bits explicitly specified
        to_signed_int(
            robertsons_multiply(
                '111111',
                '111111',
                5,
                signed=True))
        assert False
    except:
        pass


def test_booths():

    # assert to_signed_int(
    # booths_multiply(bin(-7), bin(5), 4)) == -35

    # assert to_signed_int(
    # booths_multiply(bin(-7), bin(-5), 4)) == 35

    assert to_signed_int(
        booths_multiply(
            '111111',
            '111111',
            7)) == 3969

    assert to_signed_int(
        booths_multiply(
            '111111',
            '111111',
            5,
            signed=True)) == 1

    assert to_signed_int(
        booths_multiply(
            '1111',
            '0111',
            5,
            signed=False)) == 105

    assert to_signed_int(
        booths_multiply(
            '1111',
            '0111',
            5,
            signed=True)) == -7

    assert to_signed_int(
        booths_multiply(
            '-1',
            '0111',
            5,
            signed=True)) == -7

    try:
        # If no of bits explicitly specified
        to_signed_int(
            booths_multiply(
                '111111',
                '111111',
                5,
                signed=True))
        assert False
    except:
        pass


def test_karatsuba():

    # assert to_signed_int(
    # karatsuba_multiply(bin(-7), bin(5), signed=True)) == -35

    # assert to_signed_int(
    # karatsuba_multiply(bin(-7), bin(-5), signed=True)) == 35

    assert to_signed_int(
        karatsuba_multiply(
            '111111',
            '111111',
            7)) == 3969

    assert to_signed_int(
        karatsuba_multiply(
            '111111',
            '111111',
            5,
            signed=True)) == 1

    assert to_signed_int(
        karatsuba_multiply(
            '1111',
            '0111',
            5,
            signed=False)) == 105

    assert to_signed_int(
        karatsuba_multiply(
            '1111',
            '0111',
            5,
            signed=True)) == -7

    assert to_signed_int(
        karatsuba_multiply(
            '-1',
            '0111',
            5,
            signed=True)) == -7

    try:
        # If no of bits explicitly specified
        to_signed_int(
            karatsuba_multiply(
                '111111',
                '111111',
                5,
                signed=True))
        assert False
    except:
        pass


def test_booths():

    # assert to_signed_int(
    # booths_multiply(bin(-7), bin(5), 4)) == -35

    # assert to_signed_int(
    # booths_multiply(bin(-7), bin(-5), 4)) == 35

    assert to_signed_int(
        booths_multiply(
            '111111',
            '111111',
            7)) == 3969

    assert to_signed_int(
        booths_multiply(
            '111111',
            '111111',
            5,
            signed=True)) == 1

    assert to_signed_int(
        booths_multiply(
            '1111',
            '0111',
            5,
            signed=False)) == 105

    assert to_signed_int(
        booths_multiply(
            '1111',
            '0111',
            5,
            signed=True)) == -7

    assert to_signed_int(
        booths_multiply(
            '-1',
            '0111',
            5,
            signed=True)) == -7

    try:
        # If no of bits explicitly specified
        to_signed_int(
            booths_multiply(
                '111111',
                '111111',
                5,
                signed=True))
        assert False
    except:
        pass
