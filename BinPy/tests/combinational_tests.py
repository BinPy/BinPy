from BinPy.combinational.combinational import *
from nose.tools import with_setup, nottest


def HalfAdder_test():
    ha = HalfAdder(0, 1)
    assert ha.output() == [0, 1]

    ha.set_input(0, 1)
    assert ha.output() == [1, 0]

    ha.set_inputs(0, 0)
    assert ha.output() == [0, 0]

    ha.set_inputs(1, 1)
    assert ha.output() == [1, 0]


def FullAdder_test():
    fa = FullAdder(0, 1, 0)
    assert fa.output() == [0, 1]

    fa.set_inputs(1, 1, 1)
    assert fa.output() == [1, 1]

    fa.set_input(1, 0)
    assert fa.output() == [1, 0]

    con1 = Connector()
    con2 = Connector()

    fa.set_output(1, con1)
    fa.set_output(0, con2)

    assert [con2.state, con1.state] == fa.output()

'''
def BCDAdder_test():
    ba = BCDAdder([0, 1, 1, 0], [0, 0, 1, 1], 0)
    assert ba.output() == [0, 1, 0, 0, 1]

    ba = BCDAdder([0, 1, 1, 0], [0, 0, 1, 1], 1)
    assert ba.output() == [0, 0, 1, 1, 1]
'''


def HalfSubtractor_test():
    hs = HalfSubtractor(0, 1)
    assert hs.output() == [1, 1]

    hs = HalfSubtractor(1, 1)
    assert hs.output() == [0, 0]


def FullSubtractor_test():
    fs = FullSubtractor(0, 1, 1)
    assert fs.output() == [1, 0]
    fs = FullSubtractor(1, 1, 0)
    assert fs.output() == [0, 0]
    fs = FullSubtractor(1, 1, 1)
    assert fs.output() == [1, 1]


def MUX_test():
    mux = MUX(0, 1)
    mux.select_lines(0)
    if mux.output() != 0:
        assert False
    mux.select_lines(1)
    if mux.output() != 1:
        assert False

    mux = MUX(0, 1, 0, 1)
    mux.select_lines(0, 0)
    if mux.output() != 0:
        assert False
    mux.select_lines(0, 1)
    if mux.output() != 1:
        assert False
    mux.select_lines(1, 0)
    if mux.output() != 0:
        assert False
    mux.select_lines(1, 1)
    if mux.output() != 1:
        assert False

    a = Connector()
    b = Connector()
    NOT(1).set_output(a)
    NOT(0).set_output(b)
    mux = MUX(0, 1, 0, 1)
    mux.select_lines(a, b)
    if mux.output() != 1:
        assert False
    mux.select_line(1, a)
    if mux.output() != 0:
        assert False
    mux.set_input(0, 1)
    if mux.output() != 1:
        assert False


def DEMUX_test():
    demux = DEMUX(0)
    demux.select_lines(0)
    q = [0, 0]
    if demux.output() != q:
        assert False
    demux.select_lines(1)
    if demux.output() != q:
        assert False
    demux = DEMUX(1)
    demux.select_lines(0)
    q = [1, 0]
    if demux.output() != q:
        assert False
    demux.select_lines(1)
    q = [0, 1]
    if demux.output() != q:
        assert False

    demux = DEMUX(0)
    demux.select_lines(0, 0)
    q = [0, 0, 0, 0]
    if demux.output() != q:
        assert False
    demux.select_lines(0, 1)
    if demux.output() != q:
        assert False
    demux = DEMUX(1)
    demux.select_lines(1, 0)
    q = [0, 0, 1, 0]
    if demux.output() != q:
        assert False
    demux.select_lines(1, 1)
    q = [0, 0, 0, 1]
    if demux.output() != q:
        assert False

    a = Connector()
    b = Connector()
    NOT(1).set_output(a)
    NOT(0).set_output(b)
    demux = DEMUX(0)
    demux.select_lines(a, 0)
    q = [0, 0, 0, 0]
    if demux.output() != q:
        assert False
    demux.set_inputs(b)
    demux.select_line(1, b)
    q = [0, 1, 0, 0]
    if demux.output() != q:
        assert False


def Decoder_test():
    try:
        decoder = Decoder()
        assert False
    except Exception:
        pass

    decoder = Decoder(0)
    try:
        decoder.set_inputs()
        assert False
    except Exception:
        pass

    decoder = Decoder(0)
    q = [1, 0]
    if decoder.output() != q:
        assert False
    decoder = Decoder(1)
    q = [0, 1]
    if decoder.output() != q:
        assert False

    decoder = Decoder(0, 0)
    q = [1, 0, 0, 0]
    if decoder.output() != q:
        assert False
    decoder = Decoder(0, 1)
    q = [0, 1, 0, 0]
    if decoder.output() != q:
        assert False
    decoder = Decoder(1, 0)
    q = [0, 0, 1, 0]
    if decoder.output() != q:
        assert False
    decoder = Decoder(1, 1)
    q = [0, 0, 0, 1]
    if decoder.output() != q:
        assert False

    a = Connector()
    b = Connector()
    NOT(1).set_output(a)
    NOT(0).set_output(b)
    decoder = Decoder(a, a)
    q = [1, 0, 0, 0]
    if decoder.output() != q:
        assert False
    decoder.set_input(1, b)
    q = [0, 1, 0, 0]
    if decoder.output() != q:
        assert False


def Encoder_test():
    encoder = Encoder(0, 1)
    q = [1]
    if encoder.output() != q:
        assert False
    encoder = Encoder(1, 0)
    q = [0]
    if encoder.output() != q:
        assert False

    encoder = Encoder(1, 0, 0, 0)
    q = [0, 0]
    if encoder.output() != q:
        assert False
    encoder = Encoder(0, 1, 0, 0)
    q = [0, 1]
    if encoder.output() != q:
        assert False
    encoder = Encoder(0, 0, 1, 0)
    q = [1, 0]
    if encoder.output() != q:
        assert False
    encoder = Encoder(0, 0, 0, 1)
    q = [1, 1]
    if encoder.output() != q:
        assert False

    a = Connector()
    b = Connector()
    NOT(1).set_output(a)
    NOT(0).set_output(b)
    encoder = Encoder(a, 0, 0, 1)
    q = [1, 1]
    if encoder.output() != q:
        assert False
    encoder.set_inputs(b, 0, 0, a)
    q = [0, 0]
    if encoder.output() != q:
        assert False
