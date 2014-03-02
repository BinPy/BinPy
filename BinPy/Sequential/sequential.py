from BinPy import *
from BinPy.Gates import *
from BinPy.Gates import *


class FlipFlop:
    """
    Super Class for all FlipFlops
    """
    def __init__(self):
        pass
        
    def enable(self):
        self.enable.state = 1
        self.enable.trigger()
    
    def disable(self):
        self.enable.state = 0
        self.enable.trigger()
        
class SRLatch(FlipFlop):
    """
    Class to implement SRLatch
    S and R are the two primary inputs.
    They are enabled by the third input enable.

    Ouputs are a ( q ) and b ( ~q )
    
    To Use :
    Set the inputs of SRLatch and to trigger any change in input use trigger() method.
    
    """
    def __init__(self,S,R,enable,a = Connector(),b = Connector()):
        
        self.a = a
        self.b = b        
        
        #Initiated to support numerical inputs --> See trigger method's doc
        self.S = Connector()
        self.R = Connector()
        
        #Initiated to initiate the gates
        self.enabledS = Connector()
        self.enabledR = Connector()
        
        #Initiating the gates with inputs - Will be overwritten when the self.setInputs() is called 4 lines hence.
        #This is just to initiate the gates.
        
        self.en1 = AND(S,enable)
        self.en2 = AND(R,enable)
        
        self.g1 = NOR(self.enabledS,a)
        self.g2 = NOR(self.enabledR,b)
        
        self.setInputs(S = S, R = R, enable = enable)
        self.setOutputs(A = a, B = b)
        
    def setInputs(self,**inputs):
        """
        Sets the input connectors of SRLatch.
        Give input parameters as a dictionary
       
        Ex.: sr1.setInputs(S = S, R = R)
        Ex.2: sr2.setInputs(enable = foo)
        
        Where S, R, foo are all Connector class instances.
        
        This is done to support partial change in input [ only S or R etc ]
        """

        #To support both upper and lower case
        for key in inputs:
            if key.lower() == 's':
                #To support both numerical/boolean values or Connector instances
                if isinstance(inputs[key],Connector):
                    self.S = inputs[key]
                else:
                    self.S.state = int(inputs[key])
                    
            elif key.lower() == 'r':
                if isinstance(inputs[key],Connector):
                    self.R = inputs[key]
                else:
                    self.R.state = int(inputs[key])    
                    
            elif key.lower() == 'enable':
                if isinstance(inputs[key],Connector):
                    self.enable = inputs[key]
                else:
                    self.enable.state = int(inputs[key])
            else:
                print 'ERROR: Unknow parameter passed' + str(key)
                
        if not (bool(self.S) ^ bool(self.R)):
            print "ERROR: Invalid State - Resetting the Latch"
            self.S.state = 0
            self.R.state = 1
        
        
        self.en1.setInput(0,self.S)
        self.en1.setInput(1,self.enable)
        self.en1.setOutput(self.enabledS)
        
        self.en2.setInput(0,self.R)
        self.en2.setInput(1,self.enable)
        self.en2.setOutput(self.enabledR)
                
        self.g1.setInput(0,self.enabledS)
        self.g1.setInput(1,self.a)
        
        self.g2.setInput(0,self.enabledR)
        self.g2.setInput(1,self.b)
        self.trigger()
        
    def setOutputs(self,**outputs):
        
        for key in outputs:
            if not isinstance(outputs[key],Connector):
                raise Exception('ERROR: Output not a connector instance')
            if key.lower() == 'a':
                self.a = outputs[key]
            elif key.lower() == 'b':
                self.b = outputs[key]
            else:
                print 'ERROR: Unknow parameter passed' + str(key)
        
        self.g1.setOutput(self.b)
        self.g1.setInput(1,self.a)
        
        self.g2.setOutput(self.a)
        self.g2.setInput(1,self.b)
        
        self.trigger()
        
    def trigger(self,**inputs):
        """ 
        Call to SR Latch Instance will return its current state of outputs as a List of values [ q, qcomp ]
        
        Parameters can also be passed. Binary parameters will update the SRLatch
        Connector instances will connect them to the SRLatch
        
        Once SR is triggered with binary values the values of S and R are changed however since backward triggering is not present
        The circuit preceeding the SR Latch will not get affected by this change.
        
        """
        if len(inputs) != 0:
            self.setInputs(**inputs)
           
        if bool(self.S) and bool(self.R):
            print "ERROR: Invalid State - Resetting the Latch"
            self.S.state = 0
            self.R.state = 1
            
        self.S.trigger()
        self.R.trigger()
        self.enable.trigger()
        #This will trigger the gates which will trigger the a and b
    
        return [self.a(), self.b()]
    
    
    def reset(self):
        #Resets the latch
        self.S.state = 0
        self.R.state = 1
        
        self.trigger()
    
    def __call__(self):
        self.trigger()
        return [self.a(), self.b()]

class DFlipFlop(FlipFlop):
    """
    Class to implement DFlipFlop
    D is the primary input.
    It is enabled by the second input enable.

    Ouputs are a ( q ) and b ( ~q )
    
    To Use :
    Set the inputs of DFlipFlop and to trigger any change in input use trigger() method.
    Calling an instance of DFlipFlop returns a list of its state [ a, b]
    
    """
    def __init__(self,D,enable,a = Connector(),b = Connector()):
        
        self.g1 = AND(D,enable)
        self.g2 = NOT(a)
        
        self.setInputs(D = D, enable = enable)
        self.setOutputs(A = a, B = b)
        
    def setInputs(self,**inputs):
        """
        Sets the input connectors of DFlipFlop.
        Give input parameters as a dictionary
       
        Ex.: dff.setInputs(D = dconnector, enable = enable_connector)
        Ex.2: dff.setInputs(enable = foo)
        
        Usage of **inputs is to pass parameters as dict to to support partial change in input [ D or enable alone ]
        """
        
        #To support both upper and lower case
        for key in inputs:
            if key.lower() == 'd':
                #To support both numerical/boolean values or Connector instances
                if isinstance(inputs[key],Connector):
                    self.D = inputs[key]
                else:
                    self.D.state = int(inputs[key])
                    
            elif key.lower() == 'enable':
                if isinstance(inputs[key],Connector):
                    self.enable = inputs[key]
                else:
                    self.enable.state = int(inputs[key])    
            else:
                print 'ERROR: Unknow parameter passed' + str(key)
                
        
        
        self.g1.setInput(0,self.D)
        self.g1.setInput(1,self.enable)
        self.g1.setOutput(self.a)
        
        self.g2.setInput(0,self.a)
        self.g2.setOutput(self.b)
        
        self.trigger()
        
    def setOutputs(self,**outputs):
        
        for key in outputs:
            if not isinstance(outputs[key],Connector):
                raise Exception('ERROR: Output not a connector instance')
            if key.lower() == 'a':
                self.a = outputs[key]
            elif key.lower() == 'b':
                self.b = outputs[key]
            else:
                print 'ERROR: Unknow parameter passed' + str(key)
        
        self.g1.setOutput(self.a)
        
        self.g2.setInput(0,self.a)
        self.g2.setOutput(self.b)
                
        self.trigger()
        
    def trigger(self,**inputs):
        """ 
        Call to D FlipFlop Instance will return its current state of outputs as a List of values [ q, qcomp ]
        
        Parameters can also be passed to the trigger method. Binary parameters will update the D value
        Connector instances will connect them to the DFlipFlop
        
        """
        #This should take care of every thing.    
        
        if len(inputs) != 0:
            self.setInputs(inputs)

        self.D.trigger()        
        return [self.a(), self.b()]
        
    def reset(self):
        #Resets the latch
        self.D.state = 0
        self.D.trigger()
    
    def __call__(self):
        self.trigger()
        return [self.a(), self.b()]
    
class JKFlipFlop(FlipFlop):
    """
    Class to implement JKFlipFlop
    J and K are the two primary inputs.
    They are enabled by the third input enable.

    Ouputs are a ( q ) and b ( ~q )
    
    To Use :
    Set the inputs of JKFlipFlop and to trigger any change in input use trigger() method.
    call to the JKFlipFlop instance also triggers it and returns the current state as a list
    
    """
    def __init__(self,J,K,enable,a = Connector(),b = Connector()):
        
        #Initiated to support numerical inputs --> See trigger method's doc
        self.a = a
        self.b = b  

        self.J = Connector()
        self.K = Connector()
        
        self.wire1 = Connector(0)
        self.wire2 = Connector(0)
        
        #Initiated to initiate the gates
        self.enabledJ = Connector()
        self.enabledK = Connector()
        
        #Initiating the gates with inputs - Will be overwritten when the self.setInputs() is called 4 lines below.
        #This is just to initiate the gates.
        #I.E   J, K, enable are Dummy variables w.r.t the below 2 lines.
        self.en1 = AND(J,enable,b)
        self.en2 = AND(K,enable,a)
        
        self.g1 = NOR(self.enabledJ,a)
        self.g2 = NOR(self.enabledK,b)
        
        self.setInputs(J = J, K = K, enable = enable)
        self.setOutputs(A = a, B = b)
        
    def setInputs(self,**inputs):
        """
        Sets the input connectors of SRLatch.
        Give input parameters as a dictionary
       
        Ex.: jk1.setInputs(J = J, K = K)
        Ex.2: jk2.setInputs(enable = foo)
        
        Where J, K, foo are all Connector class instances.
        
        This is done to support partial change in input [ only J or K etc ]
        """

        #To support both upper and lower case
        
        for key in inputs:
            if key.lower() == 'j':
                #To support both numerical/boolean values or Connector instances
                if isinstance(inputs[key],Connector):
                    self.J = inputs[key]
                else:
                    self.J.state = int(inputs[key])
                    
            elif key.lower() == 'k':
                if isinstance(inputs[key],Connector):
                    self.K = inputs[key]
                else:
                    self.K.state = int(inputs[key])    
                    
            elif key.lower() == 'enable':
                if isinstance(inputs[key],Connector):
                    self.enable = inputs[key]
                else:
                    self.enable.state = int(inputs[key])
            else:
                print 'ERROR: Unknow parameter passed' + str(key)
                
        self.en1.setInput(0,self.wire1)
        
        self.en1.setInput(1,self.J)
        self.en1.setInput(2,self.enable)
        self.en1.setOutput(self.enabledJ)
        
        self.en2.setInput(0,self.wire2)
        
        self.en2.setInput(1,self.K)
        self.en2.setInput(2,self.enable)
        self.en2.setOutput(self.enabledK)
                
        self.g1.setInput(0,self.enabledJ)
        self.g1.setInput(1,self.a)
        
        self.g2.setInput(0,self.enabledK)
        self.g2.setInput(1,self.b)
        
        self.trigger()
        
    def setOutputs(self,**outputs):
        
        for key in outputs:
            if not isinstance(outputs[key],Connector):
                raise Exception('ERROR: Output not a connector instance')
            if key.lower() == 'a':
                self.a = outputs[key]
            elif key.lower() == 'b':
                self.b = outputs[key]
            else:
                print 'ERROR: Unknow parameter passed' + str(key)
        
        self.g1.setOutput(self.b)
        self.g1.setInput(1,self.a)
        
        self.g2.setOutput(self.a)
        self.g2.setInput(1,self.b)
        
        self.trigger()
                
    def trigger(self,**inputs):
        """ 
        Call to JK Latch Instance will return its current state of outputs as a List of values [ q, qcomp ]
        
        Parameters can also be passed. Binary parameters will update the J and K states. Connections will remain intact.
        Connector instances will connect them to the JKFlipFlop
        
        Once JK is triggered with binary values the values of J and S are changed, however since backward triggering is not present
        The circuit preceeding the JKFlipFlop will not get affected by this change.
        
        """
        if len(inputs) != 0:
            self.setInputs(**inputs)

        #This will trigger all the gates once
        self.enable.trigger()
            
        #This will set the wire1 and wire2 to outputs of NOR gates 1 and 2       
        self.wire1.state = self.g1.result
        self.wire2.state = self.g2.result
        
        #This will trigger it again to obtain the final answer
        self.enable.trigger()
        
        #This seems to be the only workaround to  avoid infinite recursions and still get correct output.
    
        return [self.a(), self.b()]
        
    
    def reset(self):
        #Resets the latch
        self.J.state = 0
        self.K.state = 1
        
        self.trigger()
    
    def __call__(self):
        self.trigger()
        return [self.a(), self.b()]

class TFlipFlop:
    """
    Implemented using JKFlipFlop
    J = K = T
    """
    def __init__(self,T,enable,a = Connector(),b = Connector()):
        
        #Initiated to support numerical inputs --> See trigger method's doc
        self.T = T
        self.enable = enable

        self.a = a
        self.b = b

        self.jkff = JKFlipFlop(self.T,self.T,self.enable,self.a,self.b)
        
    def setInputs(self,**inputs):
        for key in inputs:
            if key.lower() == 't':
                #To support both numerical/boolean values or Connector instances
                if isinstance(inputs[key],Connector):
                    self.T = inputs[key]
                else:
                    self.T.state = int(inputs[key])
            elif key.lower() == 'enable':
                if isinstance(inputs[key],Connector):
                    self.enable = inputs[key]
                else:
                    self.enable.state = int(inputs[key])
            else:
                print 'ERROR: Unknow parameter passed' + str(key)
                
        self.jkff.setInputs(J = self.T,K = self.T,enable = self.enable)
        self.trigger()
        
    def setOutputs(self,**outputs):
        
        for key in outputs:
            if not isinstance(outputs[key],Connector):
                raise Exception('ERROR: Output not a connector instance')
            if key.lower() == 'a':
                self.a = outputs[key]
            elif key.lower() == 'b':
                self.b = outputs[key]
            else:
                print 'ERROR: Unknow parameter passed' + str(key)

        self.jkff.setOutputs(self.a,self.b)
        self.trigger()
        
    def trigger(self,**inputs):

        if len(inputs) != 0:
            self.setInputs(**inputs)
        
        self.jkff.trigger()
        
        return [self.a(), self.b()]
    
    def reset(self):
        #Resets the latch
        self.T.state = 0        
        self.trigger()
        
    def __call__(self):
        self.trigger()
        return [self.a(), self.b()]