from __future__ import print_function
from BinPy import *


class FlipFlop:

    """
    Super Class for all FlipFlops
    """

    def __init__(self, enable, clk, a, b):
        self.a = a
        self.b = b
        self.clk = clk
        self.clkoldval = 1
        self.enable = enable

    def Enable(self):
        self.enable.state = 1

    def Disable(self):
        self.enable.state = 0

    def setff(self):
        # Sets the FlipFlop
        self.a.state = 1
        self.b.state = 0
        return [self.a(), self.b()]

    def resetff(self):
        # Resets the FlipFlop
        self.a.state = 0
        self.b.state = 1
        return [self.a(), self.b()]


class SRLatch(FlipFlop):

    """
    S and R are the two primary inputs.
    They are enabled by the third input enable.
    Clock is used to trigger the Latch.

    Outputs are a ( q ) and b ( ~q )

    To Use :
    Set the inputs of SRLatch and to trigger any change in input use\
    trigger() method.
    """

    def __init__(
            self,
            S,
            R,
            enable,
            clk,
            preset=Connector(1),
            clear=Connector(1),
            a=Connector(0),
            b=Connector(1)):

        FlipFlop.__init__(self, enable, clk, a, b)

        # Initiated to support numerical inputs --> See trigger method's doc
        self.S = Connector(0)
        self.R = Connector(1)

        self.preset = Connector(1)
        self.clear = Connector(1)
        # Initiated to initiate the gates
        self.enabledS = Connector(0)
        self.enabledR = Connector(1)

        # Initiating the gates with inputs - Will be overwritten when the
        # self.setInputs() is called 4 lines hence.

        # This is just to initiate the gates.
        self.en1 = AND(S, enable)
        self.en2 = AND(R, enable)

        self.g1 = NOR(self.enabledS, a)
        self.g2 = NOR(self.enabledR, b)

        self.setInputs(S=S, R=R, enable=enable, preset=preset, clear=clear)
        self.setOutputs(A=a, B=b)

    def setInputs(self, **inputs):
        """
        Sets the input connectors of SRLatch.
        Give input parameters as a dictionary

        Ex.: sr1.setInputs(S = S, R = R)
        Ex.2: sr2.setInputs(enable = en1)

        [ where S, R, foo are all Connector class instances. ]

        This is done to support partial change in input [ only S or R etc ]

        Note:
        1) When inputs are given as type-int - The S and R states alone are
        changed. The connections remain intact.
        2) Setting the inputs does not trigger the Latch.
        Use trigger separately to trigger any change.
        """

        # To support both upper and lower case
        for key in inputs:
            if key.lower() == 's':
                # To support both numerical values or Connector instances
                if isinstance(inputs[key], Connector):
                    self.S = inputs[key]
                else:
                    self.S.state = int(inputs[key])

            elif key.lower() == 'r':
                if isinstance(inputs[key], Connector):
                    self.R = inputs[key]
                else:
                    self.R.state = int(inputs[key])

            elif key.lower() == 'enable':
                if isinstance(inputs[key], Connector):
                    self.enable = inputs[key]
                else:
                    self.enable.state = int(inputs[key])

            elif key.lower() == 'clk':
                if isinstance(inputs[key], Connector):
                    self.clk = inputs[key]
                else:
                    self.clk.state = int(inputs[key])
            elif key.lower() == "preset":
                if isinstance(inputs[key], Connector):
                    self.preset = inputs[key]
                else:
                    self.preset.state = int(inputs[key])
            elif key.lower() == "clear":
                if isinstance(inputs[key], Connector):
                    self.clear = inputs[key]
                else:
                    self.clear.state = int(inputs[key])

            else:
                print("ERROR: Unknow parameter passed" + str(key))

        if not (bool(self.S) ^ bool(self.R)):
            print("ERROR: Invalid State - Resetting the Latch")
            self.S.state = 0
            self.R.state = 1
        if not (self.preset or self.clear):
            print("ERROR: Invalid State - Resetting the Latch")
            self.preset.state = 1
            self.clear.state = 1

        self.en1.setInput(0, self.S)
        self.en1.setInput(1, self.enable)
        self.en1.setOutput(self.enabledS)

        self.en2.setInput(0, self.R)
        self.en2.setInput(1, self.enable)
        self.en2.setOutput(self.enabledR)

        self.g1.setInput(0, self.enabledS)
        self.g1.setInput(1, self.a)

        self.g2.setInput(0, self.enabledR)
        self.g2.setInput(1, self.b)

    def setOutputs(self, **outputs):

        for key in outputs:
            if not isinstance(outputs[key], Connector):
                raise Exception("ERROR: Output not a connector instance")
            if key.lower() == 'a':
                self.a = outputs[key]
            elif key.lower() == 'b':
                self.b = outputs[key]
            else:
                print("ERROR: Unknow parameter passed" + str(key))

        self.g1.setOutput(self.b)
        self.g1.setInput(1, self.a)

        self.g2.setOutput(self.a)
        self.g2.setInput(1, self.b)

    def trigger(self):
        if self.clear.state == 1 and self.preset.state == 0:
            return self.setff()
        elif self.preset.state == 1 and self.clear.state == 0:
            return self.resetff()
        elif not(self.clear.state or self.preset.state):
            print("Error: Invalid State - Resetting the Latch")
            self.clear.state = 1
            self.preset.state = 1
        else:
            if self.clkoldval == 1 and self.clk.state == 0:
                if bool(self.S) and bool(self.R):
                    print("ERROR: Invalid State - Resetting the Latch")
                    self.S.state = 0
                    self.R.state = 1

                self.enable.trigger()
                # This will trigger the gates which will trigger the a and b

        self.clkoldval = self.clk.state
        # stores the current clock state

        return [self.a(), self.b()]

    def __call__(self):
        return self.trigger()

    def state(self):
        """Returns the current state of the SRLatch"""
        return [self.a(), self.b()]


class DFlipFlop(FlipFlop):

    """
    DATA Flip Flop ( Negative edge triggered )

    D is the primary input.
    enable activates the Flip Flop.
    ( Negative edge triggered )
    Clock triggers the output

    Outputs are a ( q ) and b ( ~q )

    """

    def __init__(
            self,
            D,
            enable,
            clk,
            preset=Connector(1),
            clear=Connector(1),
            a=Connector(0),
            b=Connector(0)):

        FlipFlop.__init__(self, enable, clk, a, b)
        # Initiated to support numerical inputs --> See trigger method's doc
        self.D = Connector(0)
        self.g1 = AND(self.D, self.enable)
        self.g2 = NOT(self.a)
        self.preset = Connector(1)
        self.clear = Connector(1)

        self.setInputs(D=D, enable=enable, preset=preset, clear=clear)
        self.setOutputs(A=a, B=b)

    def setInputs(self, **inputs):
        """
        Sets the input connectors of DFlipFlop.
        Give input parameters as a dictionary

        Ex.: dff.setInputs(D = dconnector, enable = enable_connector)
        Ex.2: dff.setInputs(enable = foo)

        Usage of **inputs is to pass parameters as dict to to support \
        partial change in input [ D or enable alone ]

        Note:
        1) When inputs are given as type-int - The D state alone is
        changed. The connections remain intact.
        2) Setting the inputs does not trigger the Latch.
        Use trigger separately to trigger any change.
        """

        # To support both upper and lower case
        for key in inputs:
            if key.lower() == "d":
                # To support both numerical/boolean values or Connector
                # instances
                if isinstance(inputs[key], Connector):
                    self.D = inputs[key]
                else:
                    self.D.state = int(inputs[key])
            elif key.lower() == "enable":
                if isinstance(inputs[key], Connector):
                    self.enable = inputs[key]
                else:
                    self.enable.state = int(inputs[key])
            elif key.lower() == "clk":
                if isinstance(inputs[key], Connector):
                    self.clk = inputs[key]
                else:
                    self.clk.state = int(inputs[key])
            elif key.lower() == "preset":
                if isinstance(inputs[key], Connector):
                    self.preset = inputs[key]
                else:
                    self.preset.state = int(inputs[key])
            elif key.lower() == "clear":
                if isinstance(inputs[key], Connector):
                    self.clear = inputs[key]
                else:
                    self.clear.state = int(inputs[key])
            else:
                print("ERROR: Unknow parameter passed" + str(key))

        if not(self.preset.state or self.clear.state):
            print("ERROR : Invalid State - Resetting the Latch")
            self.preset.state = 1
            self.clear.state = 1

        self.g1.setInput(0, self.D)
        self.g1.setInput(1, self.enable)
        self.g1.setOutput(self.a)

        self.g2.setInput(self.a)
        self.g2.setOutput(self.b)

    def setOutputs(self, **outputs):

        for key in outputs:
            if not isinstance(outputs[key], Connector):
                raise Exception("ERROR: Output not a connector instance")
            if key.lower() == "a":
                self.a = outputs[key]
            elif key.lower() == "b":
                self.b = outputs[key]
            else:
                print("ERROR: Unknow parameter passed" + str(key))

        self.g1.setOutput(self.a)

        self.g2.setInput(self.a)
        self.g2.setOutput(self.b)

    def trigger(self):
        if self.clear.state == 1 and self.preset.state == 0:
            return self.setff()
        elif self.preset.state == 1 and self.clear.state == 0:
            return self.resetff()
        elif not(self.clear.state or self.preset.state):
            print("Error: Invalid State - Resetting the Latch")
            self.clear.state = 1
            self.preset.state = 1
        else:
            if self.clkoldval == 1 and self.clk.state == 0:
                self.D.trigger()
        self.clkoldval = self.clk.state
        return [self.a(), self.b()]

    def __call__(self, **inputs):
        """Call to the FlipFlop instance will invoke the trigger method"""
        return self.trigger(**inputs)

    def state(self):
        """Returns the current state of the DFlipflop"""
        return [self.a(), self.b()]


class JKFlipFlop(FlipFlop):

    """
    J K Flip Flop - Negative edge triggered

    J and K are the two primary inputs.
    They are enabled by the third input enable.
    Clock triggers the Flip flop.

    Outputs are a ( q ) and b ( ~q )

    To Use :
    Set the inputs of JKFlipFlop and to trigger any change in input \
    use trigger() method.
    call to the JKFlipFlop instance also triggers it and returns the \
    current state as a list
    """

    def __init__(
            self,
            J,
            K,
            enable,
            clk,
            preset=Connector(1),
            clear=Connector(1),
            a=Connector(0),
            b=Connector(1)):

        FlipFlop.__init__(self, enable, clk, a, b)

        self.J = Connector(0)
        self.K = Connector(0)
        self.preset = Connector(1)
        self.clear = Connector(1)
        self.setInputs(J=J, K=K, enable=enable, preset=preset, clear=clear)
        self.setOutputs(A=a, B=b)

        self.J.tap(self, "input")
        self.K.tap(self, "input")
        self.enable.tap(self, "input")
        self.clk.tap(self, "input")

        self.a.tap(self, "output")
        self.b.tap(self, "output")

    def setInputs(self, **inputs):
        """
        Sets the input connectors of Jk Flip flop.
        Give input parameters as a dictionary

        Ex.: jk1.setInputs(J = J, K = K)
        Ex.2: jk2.setInputs(enable = foo)

        Where J, K, foo are all Connector class instances.

        This is done to support partial change in input [ only J or K etc ]

        Note:
        1) When inputs are given as type-int - The J and K states alone are
        changed. The connections remain intact.
        2) Setting the inputs does not trigger the Latch.
        Use trigger separately to trigger any change.
        """

        for key in inputs:
            # To support both upper and lower case
            if key.lower() == "j":
                # To support both numerical/boolean values or Connector
                # instances
                if isinstance(inputs[key], Connector):
                    self.J = inputs[key]
                else:
                    self.J.state = int(inputs[key])

            elif key.lower() == "k":
                if isinstance(inputs[key], Connector):
                    self.K = inputs[key]
                else:
                    self.K.state = int(inputs[key])

            elif key.lower() == "enable":
                if isinstance(inputs[key], Connector):
                    self.enable = inputs[key]
                else:
                    self.enable.state = int(inputs[key])
            elif key.lower() == "clk":
                if isinstance(inputs[key], Connector):
                    self.clk = inputs[key]
                else:
                    self.clk.state = int(inputs[key])
            elif key.lower() == "preset":
                if isinstance(inputs[key], Connector):
                    self.preset = inputs[key]
                else:
                    self.preset.state = int(inputs[key])
            elif key.lower() == "clear":
                if isinstance(inputs[key], Connector):
                    self.clear = inputs[key]
                else:
                    self.clear.state = int(inputs[key])
            else:
                print("ERROR: Unknow parameter passed" + str(key))

        if not(self.preset.state or self.clear.state):
            print("ERROR : Invalid State - Resetting the Latch")
            self.preset.state = 1
            self.clear.state = 1

        self.J.tap(self, "input")
        self.K.tap(self, "input")
        self.enable.tap(self, "input")
        self.clk.tap(self, "input")

    def setOutputs(self, **outputs):

        for key in outputs:
            if not isinstance(outputs[key], Connector):
                raise Exception("ERROR: Output not a connector instance")
            if key.lower() == "a":
                self.a = outputs[key]
            elif key.lower() == "b":
                self.b = outputs[key]
            else:
                print("ERROR: Unknow parameter passed" + str(key))

        self.a.tap(self, "output")
        self.b.tap(self, "output")

    def trigger(self):
        """
        Trigger will update the output when any of the inputs change.
        """
        if self.clear.state == 1 and self.preset.state == 0:
            return self.setff()
        elif self.preset.state == 1 and self.clear.state == 0:
            return self.resetff()
        elif not(self.clear.state or self.preset.state):
            print("Error: Invalid State - Resetting the Latch")
            self.clear.state = 1
            self.preset.state = 1
        else:
            # Using behavioural Modelling
            if self.clkoldval == 1 and self.clk.state == 0:

                if bool(self.enable):
                    if bool(self.J) and bool(self.K):
                        self.a.state = 0 if bool(self.a) else 1

                    elif not bool(self.J) and bool(self.K):
                        self.a.state = 0

                    elif bool(self.J) and not bool(self.K):
                        self.a.state = 1

                self.b.state = 0 if self.a.state else 1

                self.a.trigger()
                self.b.trigger()
        self.clkoldval = self.clk.state
        return [self.a(), self.b()]

    def __call__(self):
        return self.trigger()

    def state(self):
        return [self.a(), self.b()]


class TFlipFlop(JKFlipFlop):

    """
    Toggle Flip Flop. Negative edge triggered.

    Inputs are T and enable.
    Clock triggers the circuit

    Outputs are:
    a = ( q )
    b = ( q~ )
    """

    def __init__(
            self,
            T,
            enable,
            clk,
            preset=Connector(1),
            clear=Connector(1),
            a=Connector(),
            b=Connector()):

        JKFlipFlop.__init__(self, T, T, enable, clk, preset, clear, a, b)

    def setOutputs(self, **outputs):
        JKFlipFlop.setOutputs(self, **outputs)

    def trigger(self):
        JKFlipFlop.trigger(self)
        # Triggering of the outputs is done by the JKFlipFlop Module.

    def state(self):
        return [self.a(), self.b()]

    def __call__(self):
        self.trigger()
        return [self.a(), self.b()]
