from BinPy import *


def test_robertsons():

    assert BitTools.to_signed_int(
        Multipliers.robertsons_multiply(bin(-7), bin(5), 4)) == -35

    assert BitTools.to_signed_int(
        Multipliers.robertsons_multiply(bin(-7), bin(-5), 4)) == 35

    assert BitTools.to_signed_int(
        Multipliers.robertsons_multiply(
            '111111',
            '111111',
            7)) == 3969

    assert BitTools.to_signed_int(
        Multipliers.robertsons_multiply(
            '111111',
            '111111',
            5,
            signed=True)) == 1

    assert BitTools.to_signed_int(
        Multipliers.robertsons_multiply(
            '1111',
            '0111',
            5,
            signed=False)) == 105

    assert BitTools.to_signed_int(
        Multipliers.robertsons_multiply(
            '1111',
            '0111',
            5,
            signed=True)) == -7

    assert BitTools.to_signed_int(
        Multipliers.robertsons_multiply(
            '-1',
            '0111',
            5,
            signed=True)) == -7

    try:
        # If no of bits explicitly specified
        BitTools.to_signed_int(
            Multipliers.robertsons_multiply(
                '111111',
                '111111',
                5,
                signed=True))
        assert False
    except:
        pass


def test_booths():

    assert BitTools.to_signed_int(
        Multipliers.booths_multiply(bin(-7), bin(5), 4)) == -35

    assert BitTools.to_signed_int(
        Multipliers.booths_multiply(bin(-7), bin(-5), 4)) == 35

    assert BitTools.to_signed_int(
        Multipliers.booths_multiply(
            '111111',
            '111111',
            7)) == 3969

    assert BitTools.to_signed_int(
        Multipliers.booths_multiply(
            '111111',
            '111111',
            5,
            signed=True)) == 1

    assert BitTools.to_signed_int(
        Multipliers.booths_multiply(
            '1111',
            '0111',
            5,
            signed=False)) == 105

    assert BitTools.to_signed_int(
        Multipliers.booths_multiply(
            '1111',
            '0111',
            5,
            signed=True)) == -7

    assert BitTools.to_signed_int(
        Multipliers.booths_multiply(
            '-1',
            '0111',
            5,
            signed=True)) == -7

    try:
        # If no of bits explicitly specified
        BitTools.to_signed_int(
            Multipliers.booths_multiply(
                '111111',
                '111111',
                5,
                signed=True))
        assert False
    except:
        pass


def test_karatsuba():

    assert BitTools.to_signed_int(
        Multipliers.karatsuba_multiply(bin(-7), bin(5), signed=True)) == -35

    assert BitTools.to_signed_int(
        Multipliers.karatsuba_multiply(bin(-7), bin(-5), signed=True)) == 35

    assert BitTools.to_signed_int(
        Multipliers.karatsuba_multiply(
            '111111',
            '111111',
            7)) == 3969

    assert BitTools.to_signed_int(
        Multipliers.karatsuba_multiply(
            '111111',
            '111111',
            5,
            signed=True)) == 1

    assert BitTools.to_signed_int(
        Multipliers.karatsuba_multiply(
            '1111',
            '0111',
            5,
            signed=False)) == 105

    assert BitTools.to_signed_int(
        Multipliers.karatsuba_multiply(
            '1111',
            '0111',
            5,
            signed=True)) == -7

    assert BitTools.to_signed_int(
        Multipliers.karatsuba_multiply(
            '-1',
            '0111',
            5,
            signed=True)) == -7

    try:
        # If no of bits explicitly specified
        BitTools.to_signed_int(
            Multipliers.karatsuba_multiply(
                '111111',
                '111111',
                5,
                signed=True))
        assert False
    except:
        pass


def test_booths():

    assert BitTools.to_signed_int(
        Multipliers.booths_multiply(bin(-7), bin(5), 4)) == -35

    assert BitTools.to_signed_int(
        Multipliers.booths_multiply(bin(-7), bin(-5), 4)) == 35

    assert BitTools.to_signed_int(
        Multipliers.booths_multiply(
            '111111',
            '111111',
            7)) == 3969

    assert BitTools.to_signed_int(
        Multipliers.booths_multiply(
            '111111',
            '111111',
            5,
            signed=True)) == 1

    assert BitTools.to_signed_int(
        Multipliers.booths_multiply(
            '1111',
            '0111',
            5,
            signed=False)) == 105

    assert BitTools.to_signed_int(
        Multipliers.booths_multiply(
            '1111',
            '0111',
            5,
            signed=True)) == -7

    assert BitTools.to_signed_int(
        Multipliers.booths_multiply(
            '-1',
            '0111',
            5,
            signed=True)) == -7

    try:
        # If no of bits explicitly specified
        BitTools.to_signed_int(
            Multipliers.booths_multiply(
                '111111',
                '111111',
                5,
                signed=True))
        assert False
    except:
        pass
