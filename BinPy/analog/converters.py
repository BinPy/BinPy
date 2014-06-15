from BinPy import *
import math


class A2D(object):

    """
    This class is used to get a single connector bus with analog value to a 64 bit / 32 bit IEEE Floating point
    equivalent representation.
    The output can also be 4 / 8 / 16 bit based on requirement.

    TYPE OF ADC
    ===========

    Successive Approximation Type ADC. No sampling needs to be done.
    Conversion happens with a minor delay.
    Refer: http://www.asdlib.org/onlineArticles/elabware/Scheeline_ADC/ADC_ADC_SucAprrox.html

    IEEE 754 STANDARD
    =================

    This module also allows conversion to IEEE 754 Single / Double Precision Format.
    The converted floating point value is a direct absolute representation of the  analog input.
    Refer: http://en.wikipedia.org/wiki/IEEE_floating_point

    ATTRIBUTES:
    ==========

    analog_input - Analog type connector

    typ          - 1 : 4  bit output
                 - 2 : 8  bit output
                 - 3 : 16 bit output
                 - 4 : 32 bit output [ IEEE-754 Floating Point Format ]
                 - 5 : 64 bit output [ IEEE-754 Floation Point Format ]

    refp         - Positive reference.
    refn         - Negative reference.
    gnd          - Module reference.

    scale        - scale factor to be multiplied with the voltage before conversion.

    valid        - Indicative of end of conversion.


    """

    def __init__(
            self,
            analog_input,
            digital_output,
            typ,
            gnd,
            refp=None,
            refn=None,
            scale=1):

        # Input signal attenuation factor
        self.scale = float(scale)
        self.typ = typ
        self.valid = False
        self._history = None

        self.inputs = Bus(1)
        self.inputs.set_type(analog=True)

        self.enable = Bus(1)
        self.enable[0].set_logic(1)

        self.ref = Bus(2)
        self.ref.set_type(analog=True)

        self.gnd = Bus(1)
        self.gnd.set_type(analog=True)

        if typ not in range(1, 6):
            raise Exception("ERROR: Invalid output type")

        self.outputs = Bus(2 ** (typ + 1))

        if not isinstance(digital_output, Bus):
            raise Exception(
                "ERROR: Invalid ouput. Only Bus can serve as an output.")

        if typ not in [4, 5]:
            # Linking the reference inputs.
            if (type(refp) not in [Bus, Connector] or type(refn) not in [Bus, Connector]):
                raise Exception("ERROR: Invalid reference inputs")

            else:
                self.set_ref(refp, refn)

        if not (type(gnd) in [Bus, Connector]) and (gnd.analog):
            raise Exception(
                "ERROR: The gnd must be an analog Connector or Bus.")

        self.set_inputs(analog_input)
        self.set_outputs(digital_output)
        self.set_gnd(gnd)

        # Update the values.
        self.trigger()

    def set_inputs(self, analog_input):
        """
        To 'link' the analog connector with the module's inputs.
        """
        with AutoUpdater._lock:

            if isinstance(analog_input, Bus) and analog_input.analog and (analog_input.width == 1):
                AutoUpdater.remove_link(
                    self.inputs)  # Remove old links to the inputs
                AutoUpdater.add_link(
                    analog_input,
                    self.inputs,
                    bind_to=A2D.trigger,
                    params=[self])

            elif isinstance(analog_input, Connector) and (analog_input.analog):
                AutoUpdater.remove_link(
                    self.inputs)  # Remove old links to the inputs
                AutoUpdater.add_link(
                    [analog_input],
                    self.inputs,
                    bind_to=A2D.trigger,
                    params=[self])

            else:
                raise Exception(
                    "ERROR: Invalid input. Only Analog Connnector / Bus can be linked to input")

    def set_outputs(self, outputs):
        """
        To link the output of the A2D instance with the external outputs
        """
        with AutoUpdater._lock:
            if not isinstance(outputs, Bus):
                raise Exception(
                    "ERROR: Invalid output. Output must only be a Bus instance")

            AutoUpdater.remove_link(
                self.outputs)  # Remove old links from the output
            AutoUpdater.add_link(
                self.outputs,
                outputs,
                bind_to=A2D.trigger,
                params=[self])

    def set_enable(self, enable):
        """
        Link the external enable bus / connector to the A2D instance.
        """
        with AutoUpdater._lock:
            AutoUpdater.remove_link(enable)

            if isinstance(enable, Bus):
                AutoUpdater.add_link(
                    enable,
                    self.enable,
                    bind_to=A2D.trigger,
                    params=[self])

            elif isinstance(enable, Connector):
                AutoUpdater.add_link(
                    [enable],
                    self.enable,
                    bind_to=A2D.trigger,
                    params=[self])

            else:
                raise Exception(
                    "ERROR: Invalid input. Only Analog Connnector / Bus can be linked to input")

    def set_gnd(self, gnd):
        """
        Links the gnd reference Connector / Bus
        """

        with AutoUpdater._lock:
            AutoUpdater.remove_link(self.gnd)
            AutoUpdater.add_link(
                [gnd],
                self.gnd,
                bind_to=A2D.trigger,
                params=[self])

    def set_ref(self, refp, refn):
        """
        Sets the reference voltage levels
        """

        with AutoUpdater._lock:
            AutoUpdater.remove_link(self.ref)
            AutoUpdater.add_link(
                [refp, refn], self.ref, bind_to=A2D.trigger, params=[self])

    def set_valid(self, val):
        self.valid = bool(val)

    def trigger(self):
        with AutoUpdater._lock:
            if (float(self.inputs[0]) - float(self.gnd[0])) == self._history:
                return
            # return if the input has not changed.

            self.set_valid(False)

            if not bool(self.enable[0]):
                self.set_valid(True)
                return

            ref = float(self.ref[0]) - float(self.ref[1])

            outp = ''

            self._history = (float(self.inputs[0]) - float(self.gnd[0]))

            analog_val = (
                float(self.inputs[0]) - float(self.gnd[0])) * self.scale

            cumulative_op = 0.0

            if self.typ in range(1, 4):
                # Successively approximate and set the bits accordingly.
                for i in range(self.outputs.width):
                    ref_i = float(ref) / float(2 ** (i + 1))
                    if (float(cumulative_op) + ref_i) < analog_val:
                        cumulative_op += float(ref_i)
                        outp += '1'
                    else:
                        outp += '0'

                self.outputs.set_logic_all(outp)
                return

            if analog_val == 0.0:
                self.outputs.set_logic_all('0' * self.outputs.width)
                return

            if self.typ == 4:

                len_mant = 23
                len_exp = 8
                excess = 127

            elif self.typ == 5:

                len_mant = 52
                len_exp = 11
                excess = 1023

            s = '0' if analog_val >= 0 else '1'
            analog = abs(analog_val)
            frac = analog - math.floor(analog)
            b = ''

            stop = False

            i = 0
            flag = 0

            while i <= len_mant:
                trial = frac * 2.0
                trial_decimal = math.floor(trial)
                trial_fraction = trial - trial_decimal
                b += str(int(trial_decimal))
                frac = trial_fraction

                if (not flag) and (b[-1] == '1'):
                    flag = 1

                i += flag

            m = bin(int(math.floor(analog)))[2:] + '.' + ''.join(map(str, b))
            e = m.find('.') - m.find('1')
            e = bin(
                (e +
                 excess) if e < 0 else (
                    e -
                    1 +
                    excess))[
                2:].zfill(len_exp)

            ieee = '0b' + \
                s[:1] + e[:len_exp] + (m[m.find('1') + 1:]).replace('.', '')[:len_mant].ljust(len_mant, '0')

            self.outputs.set_logic_all(ieee)
            self.set_valid(True)

    def __del__(self):
        try:
            BinPyIndexer.unindex(self)
            AutoUpdater.remove_link(self.inputs)
            AutoUpdater.remove_link(self.outputs)
            AutoUpdater.remove_link(self.enable)

        except (AttributeError, KeyError, ValueError, TypeError) as e:
            pass
