import time
import math
from BinPy import *


def test_sin_signal():
    sig1 = SignalGenerator(typ=0, freq=1000, ampl=1)
    time.sleep(0.5)  # To allow setup time.

    max = -1
    min = 2

    start_time = time.time()
    while (time.time() - start_time) < sig1.time_period:
        # sample when the run method is in sleep
        while sig1.updating:
            pass

        t = sig1.last_updated_time
        sig1_output = sig1.outputs[0].voltage - sig1.outputs[1].voltage
        sin_t = 0.5 * math.sin(2 * 3.145926 * sig1._frequency * t) + 0.5

        if (round(sig1_output, 2) != round(sin_t, 2)):
            sig1.kill()
            assert False

        time.sleep(sig1.sampling_time_interval)

    sig1.kill()


def test_square_signal():
    sig1 = SignalGenerator(typ=1, freq=1000, ampl=2)
    sig1.set_offset(-1)
    time.sleep(0.5)
    # To allow setup time.
    # To make range [ -1 to 1 ]

    max = -1
    min = 2

    start_time = time.time()
    while (time.time() - start_time) < sig1.time_period:
        # sample when the run method is in sleep
        while sig1.updating:
            pass

        t = sig1.last_updated_time
        sig1_output = sig1.outputs[0].voltage - sig1.outputs[1].voltage
        sq_t = 1 if t < (sig1.time_period / float(2)) else -1

        if (round(sig1_output, 2) != round(sq_t, 2)):
            sig1.kill()
            assert False

        time.sleep(sig1.sampling_time_interval)

    sig1.kill()


def test_ramp_signal():
    sig1 = SignalGenerator(typ=2, freq=1000, ampl=2)
    sig1.set_offset(-1)
    time.sleep(0.5)  # To allow setup time.
    # To make range [ -1 to 1 ]

    max = -1
    min = 2

    start_time = time.time()
    while (time.time() - start_time) < sig1.time_period:
        # sample when the run method is in sleep
        while sig1.updating:
            pass

        t = sig1.last_updated_time
        sig1_output = sig1.outputs[0].voltage - sig1.outputs[1].voltage
        r_t = 2 * ((t / sig1.time_period) - 0.5)

        if (round(sig1_output, 2) != round(r_t, 2)):
            sig1.kill()
            assert False

        time.sleep(sig1.sampling_time_interval)

    sig1.kill()


def test_triangle_signal():
    sig1 = SignalGenerator(typ=3, freq=1000, ampl=1)
    time.sleep(0.5)  # To allow setup time.

    max = -1
    min = 2

    start_time = time.time()
    while (time.time() - start_time) < sig1.time_period:
        # sample when the run method is in sleep
        while sig1.updating:
            pass

        t = sig1.last_updated_time
        sig1_output = sig1.outputs[0].voltage - sig1.outputs[1].voltage

        if (t < (sig1.time_period / 2.0)):
            tr_t = (2 * t / sig1.time_period)
        else:
            tr_t = (2 * (sig1.time_period - t) / sig1.time_period)

        if (round(sig1_output, 2) != round(tr_t, 2)):
            sig1.kill()
            assert False

        time.sleep(sig1.sampling_time_interval)

    sig1.kill()


def test_ttl_signal():
    sig1 = SignalGenerator(typ=4, freq=1000, ampl=2)
    time.sleep(0.5)  # To allow setup time.

    max = -1
    min = 2

    start_time = time.time()
    while (time.time() - start_time) < sig1.time_period:
        # sample when the run method is in sleep
        while sig1.updating:
            pass

        t = sig1.last_updated_time
        sig1_output = sig1.outputs[0].voltage - sig1.outputs[1].voltage
        ttl_t = 5 if t < (sig1.time_period / 2.0) else 0

        if (round(sig1_output, 2) != round(ttl_t, 2)):
            sig1.kill()
            assert False

        time.sleep(sig1.sampling_time_interval)

    sig1.kill()
