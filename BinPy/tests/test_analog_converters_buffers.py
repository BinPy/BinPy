
from BinPy import *
import time


# Testing 4 Bit, 8 Bit, 16 Bit - A2D-AnalogBuffer-D2A Block

def test_A2D_AnalogBuffer_D2A():
    for typ in range(1, 6):

        # Input to A2D
        analog_ip = Bus(1)
        analog_ip.analog = True
        analog_ip[0].set_voltage(0)

        # Output from D2A
        analog_op = Bus(1)
        analog_op.analog = True
        analog_op[0].set_voltage(0)

        # Intermediate Bus Connecting the A2D and the D2A. Buffer Input
        digital_ip = Bus(2 ** (typ + 1))

        # Intermediate Bus Connecting the A2D and the D2A. Buffer Output
        digital_op = Bus(2 ** (typ + 1))

        # The reference voltages - Testing Different Types of input
        REFP = Bus(Connector(voltage=2.5))  # Acts as +REF
        REFN = Connector(voltage=-2.5)       # Acts as -REF

        # Initialization of A2D.
        test_a2d = A2D(analog_ip, digital_ip, typ, REFP, REFN, scale=1)

        en = Connector(1)

        # Analog Buffer Block
        AnalogBuffer(digital_ip, digital_op, en, attenuation=0.1)
        # An analog Buffer Block with 0.1 db attenuation

        # Initialization of D2A.
        test_d2a = D2A(digital_op, analog_op, typ, REFP, REFN, scale=1)
        test_vector = [0.54321, -0.54321, 0, 1.23456, 5.78882, -5.78882, 2, -2]
        result_vect = [0.54321, -0.54321, 0, 1.23456, 2.50000, -2.5, 2, -2]
        # Both +5.7 and -5.7 Saturates the A2D converter.
        # The output must be Positive and negative maxima and minima

        for i in range(len(test_vector)):
            analog_ip[0].set_voltage(test_vector[i])

            # linker delay
            time.sleep(1)

            # Timing the A2D Action:
            start = time.time()
            valid = False

            while not valid:
                valid = bool(test_a2d.valid[0])
                now = time.time() - start
                # If conversion takes more than 1 second Assert False
                if now > 1:
                    assert False

            # Timing the Buffering action: - Timed test of linker module and
            # the AnalogBuffer Module
            start = time.time()
            while digital_ip.get_logic_all(as_list=False) != digital_op.get_logic_all(as_list=False):
                now = time.time() - start
                # If Buffering takes more than 1 second Assert False
                if now > 1:
                    assert False

            # Timing the D2A Action:
            start = time.time()
            valid = False

            while not valid:
                valid = bool(test_d2a.valid[0])
                now = time.time() - start
                # If conversion takes more than 1 second Assert False
                if now > 1:
                    assert False

            # Testing if the attenuation level of analog Buffer Block is
            # within the limits.
            assert digital_ip.get_logic_all(
                as_list=False) == digital_op.get_logic_all(
                as_list=False)
            if typ in [1, 2, 3]:
                # Testing the a2d functionality in typ 1, 2, 3
                # To allow for error margin of abs(resolution of the dac /
                # adc)
                assert abs(
                    float(
                        analog_op[0]) -
                    result_vect[i]) <= abs(test_a2d.resolution)
            else:
                # Testing the packing unpacking of bits in IEEE 754 mode.
                # The IEEE 754 Mode converter does not saturate.
                # It converts the input difference voltage ( VIN, VREF- )
                # to a 32 / 64 bit float.
                assert abs(
                    float(
                        analog_op[0]) -
                    float(
                        analog_ip[0])) <= abs(test_a2d.resolution)

            # Overall this module tests :
            # AnalogBuffer input / output / attenuation set functionality
            # A2D input / output / scale / ref set functionality
            # Both Connector and Bus Support in input / output / ref setting
            # A2D Action, A2D speed, D2A Action D2A Speed
            # IEEE 754 Single Precision / Double Precision Packing and Unpacking
            # linker module's functionality.
            # Buffering Speed
