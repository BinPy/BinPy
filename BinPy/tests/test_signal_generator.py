import time
import math
from BinPy import *


def test_sin_signal():
    sig1 = SignalGenerator(typ=0, freq=10, ampl=1)
    time.sleep(0.5)  # To allow setup time.

    max = -1
    min = 2

    start_time = time.time()
    while (time.time() - start_time) < sig1.time_period:
        t = sig1.last_updated_time

        sig1_output = float(sig1.outputs[0]) - float(sig1.outputs[1])
        sig1_output = int(sig1_output * 1000) / float(1000)

        sin_t = 0.5 * math.sin(2 * math.pi * sig1._frequency * t) + 0.5
        sin_t = int(sin_t * 1000) / float(1000)

        assert (sig1_output == sin_t)

        time.sleep(sig1.sampling_time_interval)
        
    sig1.kill()

def test_square_signal():
    sig1 = SignalGenerator(typ=1, freq=10, ampl=2)
    sig1.set_offset(-1)
    time.sleep(0.5)  # To allow setup time.
    # To make range [ -1 to 1 ]

    max = -1
    min = 2

    start_time = time.time()
    while (time.time() - start_time) < sig1.time_period:
        t = sig1.last_updated_time

        sig1_output = float(sig1.outputs[0]) - float(sig1.outputs[1])
        sig1_output = int(sig1_output * 1000) / float(1000)

        sq_t = 1 if t < (sig1.time_period / float(2)) else -1
        sq_t = int(sq_t * 1000) / float(1000)

        assert (sig1_output == sq_t)

        time.sleep(sig1.sampling_time_interval)
        
    sig1.kill()


def test_ramp_signal():
    sig1 = SignalGenerator(typ=2, freq=10, ampl=2)
    sig1.set_offset(-1)
    time.sleep(0.5)  # To allow setup time.
    # To make range [ -1 to 1 ]

    max = -1
    min = 2

    start_time = time.time()
    while (time.time() - start_time) < sig1.time_period:
        t = sig1.last_updated_time

        sig1_output = float(sig1.outputs[0]) - float(sig1.outputs[1])
        sig1_output = int(sig1_output * 1000) / float(1000)

        r_t = 2 * ((t / sig1.time_period) - 0.5)
        r_t = int(r_t * 1000) / float(1000)

        assert (sig1_output == r_t)

        time.sleep(sig1.sampling_time_interval)
        
    sig1.kill()


def test_triangle_signal():
    sig1 = SignalGenerator(typ=3, freq=10, ampl=1)
    time.sleep(0.5)  # To allow setup time.

    max = -1
    min = 2

    start_time = time.time()
    while (time.time() - start_time) < sig1.time_period:
        t = sig1.last_updated_time

        sig1_output = float(sig1.outputs[0]) - float(sig1.outputs[1])
        sig1_output = int(sig1_output * 1000) / float(1000)

        tr_t = (
            2 *
            t /
            sig1.time_period) if (
            t < (
                sig1.time_period /
                float(2))) else (
                2 *
                (
                    sig1.time_period -
                    t) /
            sig1.time_period)
        tr_t = int(tr_t * 1000) / float(1000)

        assert (sig1_output == tr_t)

        time.sleep(sig1.sampling_time_interval)
        
    sig1.kill()


def test_ttl_signal():
    sig1 = SignalGenerator(typ=4, freq=10, ampl=2)
    time.sleep(0.5)  # To allow setup time.

    max = -1
    min = 2

    start_time = time.time()
    while (time.time() - start_time) < sig1.time_period:
        t = sig1.last_updated_time

        sig1_output = float(sig1.outputs[0]) - float(sig1.outputs[1])
        sig1_output = int(sig1_output * 1000) / float(1000)

        ttl_t = 5 if t < (sig1.time_period / float(2)) else 0
        ttl_t = int(ttl_t * 1000) / float(1000)

        assert (sig1_output == ttl_t)

        time.sleep(sig1.sampling_time_interval)
        
    sig1.kill()
