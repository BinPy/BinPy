from __future__ import print_function
from BinPy import *


class FlipFlop:

    """
    Super Class for all FlipFlops
    """

    def __init__(self, enable, clk, a, b, set, reset):
        self.a = a
        self.b = b
        self.clk = clk
        self.clkoldval = 1
        self.enable = enable
        self.set = set
        self.reset = reset

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

class FlipFlop1:

    """
    Super Class for Earle FlipFlops
    """

    def __init__(self, enable_L, enable_H, clk, a, set, reset):
        self.a = a
        self.clk = clk
        self.clkoldval = 1
        self.enable_H = enable_H
        self.enable_L = enable_L
        self.set = set
        self.reset = reset

    def Enable(self):
        self.enable_H.state = 1
        self.enable_L.state = 0

    def Disable(self):
        self.enable_H.state = 0
        self.enable_L.state = 1

    def setff(self):
        # Sets the FlipFlop
        self.a.state = 1
        return [self.a()]

    def resetff(self):
        # Resets the FlipFlop
        self.a.state = 0
        return [self.a()]


class SRLatch(FlipFlop):

    """
    S and R are the two primary inputs.
    They are enabled by the third input enable.
    Clock is used to trigger the Latch.

    Ouputs are a ( q ) and b ( ~q )

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
            a=Connector(0),
            b=Connector(1),
            set=Connector(0),
            reset=Connector(0)):

        FlipFlop.__init__(self, enable, clk, a, b, set, reset)

        # Initiated to support numerical inputs --> See trigger method's doc
        self.S = Connector(0)
        self.R = Connector(1)

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

        self.setInputs(S=S, R=R, enable=enable)
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
            elif key.lower() == "set":
                if isinstance(inputs[key], Connector):
                    self.set = inputs[key]
                else:
                    self.set.state = int(inputs[key])
                self.trigger()
            elif key.lower() == "reset":
                if isinstance(inputs[key], Connector):
                    self.reset = inputs[key]
                else:
                    self.reset.state = int(inputs[key])
                self.trigger()

            else:
                print("ERROR: Unknow parameter passed" + str(key))

        if not (bool(self.S) ^ bool(self.R)):
            print("ERROR: Invalid State - Resetting the Latch")
            self.S.state = 0
            self.R.state = 1

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

        if self.set.state == 1:
            return self.setff()

        elif self.reset.state == 1:
            return self.resetff()

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

class EarleLatch(FlipFlop1):

    """
    D is primary input.
    Earle latch uses complementary enable inputs: enable active low (E_L) and enable active high (E_H)
    Clock is used to trigger the Latch.

    Ouputs are a ( q ) 

    To Use :
    Set the inputs of EarleLatch and to trigger any change in input use\
    trigger() method.
    """

    def __init__(
            self,
            D,
            enable_L,
            enable_H,
            clk,
            a=Connector(0),
            set=Connector(0),
            reset=Connector(0)):

        FlipFlop.__init__(self, enable_L, enable_H, clk, a, set, reset)

        # Initiated to support numerical inputs --> See trigger method's doc
        self.D = Connector(0)
        

        # Initiated to initiate the gates
        self.enabledD1 = Connector(1)
        self.enabledD2 = Connector(1)
        self.enabledD3 = Connector(1)

        # Initiating the gates with inputs - Will be overwritten when the
        # self.setInputs() is called 4 lines hence.

        # This is just to initiate the gates.
        self.g1 = NAND(D, enable_H)
        self.g2 = NAND(D, a)
        self.g3 = NAND(a, enable_L)
        self.g4 = NAND(self.enabledD1, self.enabledD2, self.enabledD3)
        

        self.setInputs(D=D, enable_L=enable_L, enable_H=enable_H)
        self.setOutputs(A=a)

    def setInputs(self, **inputs):
        """
        Sets the input connectors of EarleLatch.
        Give input parameters as a dictionary

        Ex.: sr1.setInputs(D=D)
        
        Note:
        1) When inputs are given as type-int - The D states alone are
        changed. The connections remain intact.
        2) Setting the inputs does not trigger the Latch.
        Use trigger separately to trigger any change.
        """

        # To support both upper and lower case
        for key in inputs:
            if key.lower() == 'd':
                # To support both numerical values or Connector instances
                if isinstance(inputs[key], Connector):
                    self.D = inputs[key]
                else:
                    self.D.state = int(inputs[key])

           
            elif key.lower() == 'enable_l':
                if isinstance(inputs[key], Connector):
                    self.enable = inputs[key]
                else:
                    self.enable.state = int(inputs[key])
            elif key.lower() == 'enable_h':
                if isinstance(inputs[key], Connector):
                    self.enable = inputs[key]
                else:
                    self.enable.state = int(inputs[key])

            elif key.lower() == 'clk':
                if isinstance(inputs[key], Connector):
                    self.clk = inputs[key]
                else:
                    self.clk.state = int(inputs[key])
            elif key.lower() == "set":
                if isinstance(inputs[key], Connector):
                    self.set = inputs[key]
                else:
                    self.set.state = int(inputs[key])
                self.trigger()
            elif key.lower() == "reset":
                if isinstance(inputs[key], Connector):
                    self.reset = inputs[key]
                else:
                    self.reset.state = int(inputs[key])
                self.trigger()

            else:
                print("ERROR: Unknow parameter passed" + str(key))

        if not (bool(self.D) ):
            print("ERROR: Invalid State - Resetting the Latch")
            self.D.state = 0
           

        self.g1.setInput(0, self.D)
        self.g1.setInput(1, self.enable_H)
        self.g1.setOutput(self.enabledD1)
        
        self.g2.setInput(0, self.D)
        self.g2.setInput(1, self.a)

        self.g3.setInput(0, self.enable_L)
        self.g3.setInput(1, self.a)

        

    def setOutputs(self, **outputs):

        for key in outputs:
            if not isinstance(outputs[key], Connector):
                raise Exception("ERROR: Output not a connector instance")
            if key.lower() == 'a':
                self.a = outputs[key]
            
            else:
                print("ERROR: Unknown parameter passed" + str(key))

        
        self.g2.setInput(1, self.a)
        self.g2.setOutput(self.enabledD2)

        self.g3.setInput(1, self.a)
        self.g3.setOutput(self.enabledD3)
       
        self.g4.setInput(1,self.enabledD1)
        self.g4.setInput(1,self.enabledD2)
        self.g4.setInput(1,self.enabledD3)

        self.g4.setOutput(self.a)
        

    def trigger(self):

        if self.set.state == 1:
            return self.setff()

        elif self.reset.state == 1:
            return self.resetff()

        if self.clkoldval == 1 and self.clk.state == 0:
            if bool(self.D) :
                print("ERROR: Invalid State - Resetting the Latch")
                self.D.state = 0
                

            self.enable.trigger()
            # This will trigger the gates which will trigger the a 

        self.clkoldval = self.clk.state
        # stores the current clock state

        return [self.a()]

    def __call__(self):
        return self.trigger()

    def state(self):
        """Returns the current state of the EarleLatch"""
        return [self.a()]


class DFlipFlop(FlipFlop):

    """
    DATA Flip Flop ( Negative edge triggered )

    D is the primary input.
    enable activates the Flip Flop.
    ( Negative edge triggered )
    Clock triggers the output

    Ouputs are a ( q ) and b ( ~q )

    """

    def __init__(
            self,
            D,
            enable,
            clk,
            a=Connector(0),
            b=Connector(1),
            set=Connector(0),
            reset=Connector(0)):

        FlipFlop.__init__(self, enable, clk, a, b, set, reset)
        # Initiated to support numerical inputs --> See trigger method's doc
        self.D = D
        self.g1 = AND(self.D, self.enable)
        self.g2 = NOT(self.a)

        self.setInputs(D=D, enable=enable)
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
        1) When inputs are given as type-int - The S and R states alone are
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
            elif key.lower() == "set":
                if isinstance(inputs[key], Connector):
                    self.set = inputs[key]
                else:
                    self.set.state = int(inputs[key])
                self.trigger()
            elif key.lower() == "reset":
                if isinstance(inputs[key], Connector):
                    self.reset = inputs[key]
                else:
                    self.reset.state = int(inputs[key])
                self.trigger()
            else:
                print("ERROR: Unknow parameter passed" + str(key))

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

        if self.set.state == 1:
            return self.setff()

        elif self.reset.state == 1:
            return self.resetff()

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

    Ouputs are a ( q ) and b ( ~q )

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
            a=Connector(0),
            b=Connector(1),
            set=Connector(0),
            reset=Connector(0)):

        FlipFlop.__init__(self, enable, clk, a, b, set, reset)

        self.J = J
        self.K = K

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
        1) When inputs are given as type-int - The S and R states alone are
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
            elif key.lower() == "set":
                if isinstance(inputs[key], Connector):
                    self.set = inputs[key]
                else:
                    self.set.state = int(inputs[key])
                self.trigger()
            elif key.lower() == "reset":
                if isinstance(inputs[key], Connector):
                    self.reset = inputs[key]
                else:
                    self.reset.state = int(inputs[key])
                self.trigger()
            else:
                print("ERROR: Unknow parameter passed" + str(key))

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

        if self.set.state == 1:
            return self.setff()

        elif self.reset.state == 1:
            return self.resetff()

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


class TFlipFlop(FlipFlop):

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
            a=Connector(),
            b=Connector(),
            set=Connector(0),
            reset=Connector(0)):

        FlipFlop.__init__(self, enable, clk, a, b, set, reset)

        self.T = T
        self.T.tap(self, "input")
        self.enable.tap(self, "input")
        self.clk.tap(self, "input")

    def setInputs(self, **inputs):
        for key in inputs:
            if key.lower() == "t":
                # To support both numerical/boolean values or Connector
                # instances
                if isinstance(inputs[key], Connector):
                    self.T = inputs[key]
                else:
                    self.T.state = int(inputs[key])
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
            elif key.lower() == "set":
                if isinstance(inputs[key], Connector):
                    self.set = inputs[key]
                else:
                    self.set.state = int(inputs[key])
                self.trigger()
            elif key.lower() == "reset":
                if isinstance(inputs[key], Connector):
                    self.reset = inputs[key]
                else:
                    self.reset.state = int(inputs[key])
                self.trigger()
            else:
                print("ERROR: Unknow parameter passed" + str(key))

        self.T.tap(self, "input")
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

        if self.set.state == 1:
            return self.setff()

        elif self.reset.state == 1:
            return self.resetff()

        if self.clkoldval == 1 and self.clk.state == 0:
            if bool(self.T):
                self.a.state = 0 if bool(self.a) else 1
            self.b.state = 0 if bool(self.a) else 1

            self.a.trigger()
            self.b.trigger()

        self.clkoldval = self.clk.state

    def state(self):
        return [self.a(), self.b()]

    def __call__(self):
        self.trigger()
        return [self.a(), self.b()]
