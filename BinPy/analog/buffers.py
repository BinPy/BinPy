from BinPy import *


class AnalogBuffer(object):

    """
    Analog Buffer Block
    ===================

    Create an Analog Buffer Bank which buffers the input analog value to the output.
    Enabled input enables the buffer.

    All inputs / outputs / enable are Bus types.

    METHODS
    =======

    set_enable(enable_Bus_1_bit)      : link the enable_Bus_1_bit with the Buffer's enable.

    set_inputs(Bus)                   : link the 'Bus' with the Buffer's inputs.
    set_outputs(Bus)                  : link the 'Bus' with the Buffer's outputs.
    set_inouts(In_Bus, Out_Bus)       : Set the inputs and outputs ( used when the buffer bank width has to be varied )
    set_attenuation(float)            : set the voltage attenuation in decibels.
                                        Voltage attenuation determines the value by which input is attenuated by the buffer block.
    trigger()                         : update the outputs Bus with the value of inputs.

    PROPERTIES
    ==========

    attenuation                       : get the voltage attenuation value ( in db )
    enabled                           : return true if the enable input is high.
    disabled                          : return true if the enable input is low.

    USAGE
    =====

    >>> a = Bus(4)
    >>> a.set_voltage_all(3.5, 4.6, 2.6, 1.1)
    >>> b = Bus(4)
    >>> e = Bus(1)
    >>> e.set_logic(1) # Set enable high

    >>> buf1 = AnalogBuffer(a, b, e, 0.8)

    >>> b.get_voltage_all()
    [ 3.1920379377456842,  4.195249861037184,  2.3712281823253654,  1.0032119232915009 ]

    >>> b.get_logic_all()
    [1, 1, 0, 0]

    >>> b.set_attenuation(0) # Change the attenuation value

    >>> b.get_voltage_all()
    [3.5, 4.6, 2.6, 1.1]

    >>> b.get_logic_all()
    [1, 1, 1, 0]


    NOTE
    ====

    The input width is taken as the width of the Buffer Bank.
    When inputs are changed accordingly the width varies.
    Consequently  the output width needs to match the input width.

    Hence inputs / outputs need to be updated in parallel.

    """

    def __init__(self, inputs, outputs, enable, attenuation=0.0):
        with AutoUpdater._lock:
            self.inputs = Bus(inputs.width)
            self.outputs = Bus(inputs.width)
            self._enable = Bus(1)

            self.set_attenuation(attenuation)
            self.set_inouts(inputs, outputs)
            self.set_enable(enable)

    def trigger(self):
        with AutoUpdater._lock:
            inp_voltages = self.inputs.get_voltage_all()
            inp_voltages_atten = [
                float(float(v) * (10 ** (-self._attenuation / 20))) for v in self.inputs]
            if self._enable[0].get_logic() == 1:
                self.outputs.set_voltage_all(inp_voltages_atten)

    def set_attenuation(self, attenuation):
        """
        Set the voltage attenuation value in db for the buffer bank.
        Negative value indicates gain.
        """
        with AutoUpdater._lock:
            if type(attenuation) not in [float, int]:
                raise Exception(
                    "ERROR: Attenuation can be a float value only.")
            self._attenuation = float(attenuation)
            self.trigger()

    @property
    def attenuation(self):
        """
        Get the voltage attenuation value in db for the buffer bank.
        Negative value indicates gain.
        """
        return float(self._attenuation)

    def set_inputs(self, inputs):
        """
        Set the inputs to be linked with the inputs of the buffer bank module
        """
        if (inputs.width != self.inputs.width):
            raise Exception("ERROR: Input / Output width mismatch.")

        with AutoUpdater._lock:
            AutoUpdater.remove_link(self.inputs)
            AutoUpdater.add_link(
                inputs,
                self.inputs,
                bind_to=AnalogBuffer.trigger,
                params=[self])

            self.trigger()

    def set_outputs(self, outputs):
        """
        Set the outputs to be linked with the outputs of the buffer bank module
        """
        if (outputs.width != self.outputs.width):
            raise Exception("ERROR: Input / Output width mismatch.")

        with AutoUpdater._lock:
            AutoUpdater.remove_link(self.outputs)
            AutoUpdater.add_link(
                self.outputs,
                outputs,
                bind_to=AnalogBuffer.trigger,
                params=[self])

            self.trigger()

    def set_inouts(self, inputs, outputs):
        """
        Set the inputs and ouputs to be linked with the inputs and the outputs of the buffer bank module
        """
        with AutoUpdater._lock:
            if (inputs.width != outputs.width):
                raise Exception("ERROR: Input / Output width mismatch.")

            AutoUpdater.remove_link(self.inputs)
            AutoUpdater.add_link(
                inputs,
                self.inputs,
                bind_to=AnalogBuffer.trigger,
                params=[self])

            AutoUpdater.remove_link(self.outputs)
            AutoUpdater.add_link(
                self.outputs,
                outputs,
                bind_to=AnalogBuffer.trigger,
                params=[self])

            self.trigger()

    def set_enable(self, enable):
        """
        Set the enable input to be linked with the enable input of the buffer bank module
        """
        with AutoUpdater._lock:
            if isinstance(enable, Bus):
                AutoUpdater.remove_link(self._enable)
                AutoUpdater.add_link(
                    enable,
                    self._enable,
                    bind_to=AnalogBuffer.trigger,
                    params=[self])
            elif isinstance(enable, Connector):
                AutoUpdater.remove_link(self._enable)
                AutoUpdater.add_link(
                    [enable],
                    self._enable,
                    bind_to=AnalogBuffer.trigger,
                    params=[self])
            else:
                raise Exception(
                    "ERROR: Invalid Enable input. Enable must be a 1-bit Bus or a Connector.")

    @property
    def enabled(self):
        """
        Return true if the buffer block is enabled
        """
        return (self._enable[0].get_logic() == 1)

    @property
    def disabled(self):
        """
        Return true if the buffer block is disabled
        """
        return not self.is_enabled()
