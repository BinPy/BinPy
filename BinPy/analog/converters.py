from BinPy import *
import math


class A2D(object):

    """
    This class is used to convert a single digital connector / bus with analog value
    to a 64 bit / 32 bit IEEE Floating point equivalent representation.
    The output can also be 4 / 8 / 16 bit based on requirement.

    TYPE OF ADC
    ===========

    Successive Approximation Type ADC. No clock is needed.
    Conversion happens with a minor delay.
    At the end of the conversion the valid bit is set.
    Refer: http://www.asdlib.org/onlineArticles/elabware/Scheeline_ADC/ADC_ADC_SucAprrox.html

    IEEE 754 STANDARD
    =================

    This module also allows conversion to IEEE 754 Single / Double Precision Format.
    The converted floating point value is a direct absolute representation of the  analog input.
    Refer: http://en.wikipedia.org/wiki/IEEE_floating_point

    ATTRIBUTES / PARAMETERS :
    ========================

    analog_input    - Analog type connector
    digital_outputs - Digital type connector outputs
    typ             - 1 : 4  bit output
                    - 2 : 8  bit output
                    - 3 : 16 bit output
                    - 4 : 32 bit output [ IEEE-754 Floating Point Format ]
                    - 5 : 64 bit output [ IEEE-754 Floation Point Format ]
    refp            - Positive reference.
    refn            - Negative reference.
    scale           - scale factor to be multiplied with the voltage before conversion.
    valid           - 1-Bit digital Bus Indicating the end of conversion.

    USAGE
    =====

    >>> input_analog   = Bus(Connector(voltage = 6.4))
    >>> input_analog.set_type(analog = True)
    >>> output_digital = Bus(16)
    >>> VREF           = Connector(voltage = 5.0)
    >>> GND            = Connector(voltage = 0)
    >>> a2d_16bit = A2D(input_analog, output_digital, 3, VREF, GND, scale = 0.5)
    >>> time.sleep(0.5) # To allow conversion to take place.
    >>> print output_digital.get_logic_all(as_list = False)

    0b1010001111010111

    >>> input_analog[0].set_voltage(4.2)
    >>> time.sleep(0.5) # To allow conversion to take place.
    >>> print output_digital.get_logic_all(as_list = False)

    0b0110101110000101

    >>> ieee_64bit = Bus(64)
    >>> a2d_IEEE64 = A2D(input_analog, ieee_64bit, 5)
    >>> time.sleep(0.5) # To allow conversion to take place.
    >>> print ieee_64bit.get_logic_all(as_list = False)

    0b0100000000010000110011001100110011001100110011001100110011001101

    http://babbage.cs.qc.cuny.edu/IEEE-754.old/Decimal.html

    """

    def __init__(
            self,
            analog_input,
            digital_output,
            typ,
            refp=None,
            refn=None,
            scale=1):

        # Input signal attenuation factor
        self.scale = float(scale)
        self.typ = typ

        self.valid = Bus(1)
        self._history = None
        self._enable_history = None

        self.inputs = Bus(1)
        self.inputs.set_type(analog=True)

        self.enable = Bus(1)
        self.enable[0].set_logic(1)

        self.ref = Bus(2)
        self.ref.set_type(analog=True)

        if typ not in range(1, 6):
            raise Exception("ERROR: Invalid output type")

        self.outputs = Bus(2 ** (typ + 1))

        if not isinstance(digital_output, Bus):
            raise Exception(
                "ERROR: Invalid ouput. Only Bus can serve as an output.")

        if typ not in [4, 5]:
            # Linking the reference inputs.
            if (type(refp) not in [Bus, Connector]) or (type(refn) not in [Bus, Connector]):
                raise Exception("ERROR: Invalid reference inputs")

            else:
                self.set_ref(refp, refn)

        self.set_inputs(analog_input)
        self.set_outputs(digital_output)

        # Update the values.
        self.trigger()

    @property
    def possible_states(self):
        return 2 ** (self.outputs.width)

    @property
    def resolution(self):
        if self.typ in [1, 2, 3]:
            vref = 0.0
            vref = float(self.ref[0]) - float(self.ref[1])
            return float(vref) / float(self.possible_states)

        elif self.typ == 4:
            return 1.0e-05

        else:
            return 1.0e-10  # approximate resolutions.

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
                    self.inputs)

            elif isinstance(analog_input, Connector) and (analog_input.analog):
                AutoUpdater.remove_link(
                    self.inputs)  # Remove old links to the inputs
                AutoUpdater.add_link(
                    [analog_input],
                    self.inputs)

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

            if isinstance(enable, Bus) or isinstance(enable, Connector):
                AutoUpdater.add_link(
                    enable,
                    self.enable)

            else:
                raise Exception(
                    "ERROR: Invalid input. Only Analog Connnector / Bus can be linked to input")

    def set_ref(self, refp, refn):
        """
        Sets the reference voltage levels. Accepts 1-Bit Bus / Connector.
        """

        with AutoUpdater._lock:
            AutoUpdater.remove_link(self.ref)
            AutoUpdater.add_link(
                refp,
                self.ref[0])
            AutoUpdater.add_link(
                refn,
                self.ref[1])

    def set_valid(self, val):
        self.valid[0].set_logic(bool(val))

    def trigger(self):

        with AutoUpdater._lock:
            cur_inputs = float(self.inputs[0])
            cur_ref = (float(self.ref[0]), float(self.ref[1]))
            cur_enable = bool(self.enable[0])

        if (cur_inputs - cur_ref[1] == self._history) and (cur_enable == self._enable_history):
            return
        # return if the input has not changed.

        if not cur_enable:
            self.set_valid(True)
            return

        self._history = (cur_inputs - cur_ref[1])
        self._enable_history = cur_enable

        ref = 0
        self.set_valid(False)
        ref = cur_ref[0] - cur_ref[1]

        outp = ''

        analog_val = (cur_inputs - cur_ref[1]) * float(self.scale)

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

            with AutoUpdater._lock:
                self.outputs.set_logic_all(outp)
                self.set_valid(True)

            return

        if analog_val == 0.0:
            with AutoUpdater._lock:
                self.outputs.set_logic_all('0' * self.outputs.width)
                self.set_valid(True)
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
        i = 0
        flag = 0
        ttl = excess

        while i <= len_mant + 1:
            trial = frac * 2.0
            trial_decimal = math.floor(trial)
            trial_fraction = trial - trial_decimal
            b += str(int(trial_decimal))
            frac = trial_fraction

            if (not flag) and (b[-1] == '1'):
                flag = 1

            i += flag

            # Maximum iterations is limited by the no of binary shifts.
            ttl -= 1

            if ttl < 0:  # Maximum possible no. of binary shifts
                break

        m = bin(int(math.floor(analog)))[2:] + '.' + ''.join(map(str, b))
        e = m.find('.') - m.find('1')
        e = bin(
            (e +
                excess) if e < 0 else (
                e -
                1 +
                excess))[
            2:].zfill(len_exp)

        ieee = '0b' + s[:1] + e[:len_exp] + \
            (m[m.find('1') + 1:]).replace('.', '')[:len_mant].ljust(len_mant, '0')

        with AutoUpdater._lock:
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


class D2A(object):

    """
    Digital To Analog Converter Block.
    This Block is used to Convert 4 / 8 / 16 Bit wide digital representation to
    its analog equivalent.
    Conversion delay is very minimal.

    IEEE 754 STANDARDS CONVERSION
    =============================

    It also has provision to convert from 32 Bit ( Single Precision ) or
    64 Bit ( Double Precision ) IEEE 754 Format to its analog Equivalent.

    ATTRIBUTES:
    ==========

    digital_inputs - Analog type connector
    typ            - 1 : 4  bit input
                   - 2 : 8  bit input
                   - 3 : 16 bit input
                   - 4 : 32 bit input [ IEEE-754 Floating Point Format ]
                   - 5 : 64 bit input [ IEEE-754 Floation Point Format ]
    refp           - Positive reference.
    refn           - Negative reference.
    gnd            - Module reference.
    scale          - scale factor to be multiplied with the voltage before conversion.

    USAGE:
    =====

    >>> output_analog   = Bus(Connector(voltage = 6.4))
    >>> output_analog.set_type(analog = True)
    >>> input_digital = Bus(16)
    >>> input_digital.set_logic_all('0110101110000101')
    >>> VREF           = Connector(voltage = 5.0)
    >>> GND            = Connector(voltage = 0)
    >>> d2a_16bit = D2A(input_digital, output_analog, 3, VREF, GND, scale = 2)
    >>> time.sleep(0.1) # To allow conversion to take place.
    >>> print output_analog[0].get_voltage()

    4.19998168945

    >>> ieee_64bit = Bus(64)
    >>> ieee_64bit.set_logic_all('0b0100000000011001100110011001100110011001100110011001100110011010')
    >>> ieee_packed = Bus(1)
    >>> ieee_packed.set_type(analog = True)
    >>> d2a_ieee64 = D2A(ieee_64bit, ieee_packed, 5)
    >>> time.sleep(0.1)
    >>> print  ieee_packed[0].get_voltage()

    http://babbage.cs.qc.cuny.edu/IEEE-754.old/Decimal.html

    """

    def __init__(
            self,
            digital_inputs,
            analog_output,
            typ,
            refp=None,
            refn=None,
            scale=1):

        if typ not in range(1, 6):
            raise Exception("ERROR: Invalid output type")

        # Input signal attenuation factor
        self.scale = float(scale)

        self.typ = typ
        self.valid = Bus(Connector(1))
        self._history = None
        self._enable_history = None

        self.outputs = Bus(1)
        self.outputs.set_type(analog=True)

        self.enable = Bus(1)
        self.enable[0].set_logic(1)

        self.ref = Bus(2)  # ref+, ref-
        self.ref.set_type(analog=True)

        self.inputs = Bus(2 ** (typ + 1))
        self.inputs.set_type(analog=False)

        if not isinstance(digital_inputs, Bus):
            raise Exception(
                "ERROR: Invalid input. Only Bus can serve as an input.")

        if typ not in [4, 5]:
            # Linking the reference inputs.
            if (type(refp) not in [Bus, Connector]) or (type(refn) not in [Bus, Connector]):
                raise Exception("ERROR: Invalid reference inputs")

            else:
                self.set_ref(refp, refn)

        self.set_inputs(digital_inputs)
        self.set_outputs(analog_output)

        # Update the values.
        self.trigger()

    @property
    def possible_states(self):
        return 2 ** (self.inputs.width)

    @property
    def resolution(self):
        if self.typ in [1, 2, 3]:
            vref = 0.0
            vref = float(self.ref[0]) - float(self.ref[1])
            return float(vref) / float(self.possible_states)

        elif self.typ == 4:
            return 1.0e-05

        else:
            return 1.0e-10  # approximate resolutions.

    def set_inputs(self, digital_inputs):
        """
        To 'link' the Digital Bus with the module's inputs.
        """
        with AutoUpdater._lock:

            if isinstance(digital_inputs, Bus) and (not digital_inputs.analog) and (digital_inputs.width == 2 ** (self.typ + 1)):
                AutoUpdater.remove_link(
                    self.inputs)  # Remove old links to the inputs
                AutoUpdater.add_link(
                    digital_inputs,
                    self.inputs)

            else:
                raise Exception(
                    "ERROR: Invalid input. Only Digital Bus can be linked to input")

    def set_outputs(self, analog_output):
        """
        To link the output of the D2A instance with the external output
        """
        with AutoUpdater._lock:
            if isinstance(analog_output, Bus) and (analog_output.analog):
                AutoUpdater.remove_link(
                    self.outputs)  # Remove old links from the output
                AutoUpdater.add_link(
                    self.outputs,
                    analog_output,
                    bind_to=D2A.trigger,
                    params=[self])

            elif isinstance(analog_output, Connector) and (analog_output.analog):
                AutoUpdater.remove_link(
                    self.outputs)  # Remove old links from the outputs
                AutoUpdater.add_link(
                    self.outputs,
                    [analog_output],
                    bind_to=D2A.trigger,
                    params=[self])

                raise Exception(
                    "ERROR: Invalid output. Output must only be a analog Bus / Connector instance")

    def set_enable(self, enable):
        """
        Link the external enable bus / connector to the A2D instance.
        """
        with AutoUpdater._lock:
            AutoUpdater.remove_link(enable)

            if isinstance(enable, Bus):
                AutoUpdater.add_link(
                    enable,
                    self.enable)

            elif isinstance(enable, Connector):
                AutoUpdater.add_link(
                    [enable],
                    self.enable)
            else:
                raise Exception(
                    "ERROR: Invalid input. Only Analog Connnector / Bus can be linked to input")

    def set_ref(self, refp, refn):
        """
        Sets the reference voltage levels
        """
        with AutoUpdater._lock:
            AutoUpdater.remove_link(self.ref)
            AutoUpdater.add_link(
                refp,
                self.ref[0])
            AutoUpdater.add_link(
                refn,
                self.ref[1])

    def set_valid(self, val):
        self.valid[0].set_logic(bool(val))

    def trigger(self):
        with AutoUpdater._lock:
            cur_inputs = self.inputs.get_logic_all()
            cur_inputsb = self.inputs.get_logic_all(as_list=False)
            cur_enable = bool(self.enable[0])
            cur_ref = (float(self.ref[0]), float(self.ref[1]))
            cur_resl = self.resolution

        if (cur_inputs == self._history):
            return
        # return if the input has not changed.

        if not cur_enable:
            # The output is valid for the given inputs ( enable set to false )
            self.set_valid(True)
            return

        self._history = cur_inputs
        self._enable_history = cur_enable

        self.set_valid(False)

        ref = cur_ref[0] - cur_ref[1]
        dig = cur_inputsb

        if self.typ in range(1, 4):

            analog = float(int(dig, 2)) * float(cur_resl)
            result = (analog + float(cur_ref[1])) * float(self.scale)
            with AutoUpdater._lock:
                self.outputs[0].set_voltage(result)

            self.set_valid(True)
            return

        dig = dig[2:]

        if self.typ == 4:

            len_mant = 23
            len_exp = 8
            excess = 127

        elif self.typ == 5:

            len_mant = 52
            len_exp = 11
            excess = 1023

        s = 1 if dig[0] == '0' else -1
        exp = 2 ** (int(dig[1:(len_exp + 1)], 2) - excess)
        man = (float(1) / ((2 ** len_mant) - 1)) * \
            float(int(dig[len_exp + 1:], 2))

        analog = s * exp * (man + 1)

        result = (analog + float(cur_ref[1])) * float(self.scale)

        with AutoUpdater._lock:
            self.outputs[0].set_voltage(result)

        self.set_valid(True)

    def __del__(self):
        try:
            BinPyIndexer.unindex(self)
            AutoUpdater.remove_link(self.inputs)
            AutoUpdater.remove_link(self.outputs)
            AutoUpdater.remove_link(self.enable)

        except (AttributeError, KeyError, ValueError, TypeError) as e:
            pass
