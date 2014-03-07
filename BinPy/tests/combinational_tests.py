from BinPy.Combinational.combinational import *
from nose.tools import with_setup, nottest


def MUX_test():
    mux = MUX(0, 1)
    mux.selectLines(0)
    if mux.output() != 0:
        assert False
    mux.selectLines(1)
    if mux.output() != 1:
        assert False

    mux = MUX(0, 1, 0, 1)
    mux.selectLines(0, 0)
    if mux.output() != 0:
        assert False
    mux.selectLines(0, 1)
    if mux.output() != 1:
        assert False
    mux.selectLines(1, 0)
    if mux.output() != 0:
        assert False
    mux.selectLines(1, 1)
    if mux.output() != 1:
        assert False

    a = Connector()
    b = Connector()
    NOT(1).setOutput(a)
    NOT(0).setOutput(b)
    mux = MUX(0, 1, 0, 1)
    mux.selectLines(a, b)
    if mux.output() != 1:
        assert False
    mux.selectLine(1, a)
    if mux.output() != 0:
        assert False
    mux.setInput(0, 1)
    if mux.output() != 1:
        assert False


def DEMUX_test():
    demux = DEMUX(0)
    demux.selectLines(0)
    q = [0, 0]
    if demux.output() != q:
        assert False
    demux.selectLines(1)
    if demux.output() != q:
        assert False
    demux = DEMUX(1)
    demux.selectLines(0)
    q = [1, 0]
    if demux.output() != q:
        assert False
    demux.selectLines(1)
    q = [0, 1]
    if demux.output() != q:
        assert False

    demux = DEMUX(0)
    demux.selectLines(0, 0)
    q = [0, 0, 0, 0]
    if demux.output() != q:
        assert False
    demux.selectLines(0, 1)
    if demux.output() != q:
        assert False
    demux = DEMUX(1)
    demux.selectLines(1, 0)
    q = [0, 0, 1, 0]
    if demux.output() != q:
        assert False
    demux.selectLines(1, 1)
    q = [0, 0, 0, 1]
    if demux.output() != q:
        assert False

    a = Connector()
    b = Connector()
    NOT(1).setOutput(a)
    NOT(0).setOutput(b)
    demux = DEMUX(0)
    demux.selectLines(a, 0)
    q = [0, 0, 0, 0]
    if demux.output() != q:
        assert False
    demux.setInputs(b)
    demux.selectLine(1, b)
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
        decoder.setInputs()
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
    NOT(1).setOutput(a)
    NOT(0).setOutput(b)
    decoder = Decoder(a, a)
    q = [1, 0, 0, 0]
    if decoder.output() != q:
        assert False
    decoder.setInput(1, b)
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
    NOT(1).setOutput(a)
    NOT(0).setOutput(b)
    encoder = Encoder(a, 0, 0, 1)
    q = [1, 1]
    if encoder.output() != q:
        assert False
    encoder.setInputs(b, 0, 0, a)
    q = [0, 0]
    if encoder.output() != q:
        assert False
