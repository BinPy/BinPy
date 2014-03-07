from BinPy import *
from sequential import *

class Counter(object):
    """
    Base class for all counters
    """
    def __init__(self,bits):
        
        self.bits = bits
        self.out = []
        for i in range(self.bits):
            self.out.append(Connector())
        self.outold = self.out[:]
        self.ff = []
        self.enable = Connector(1)
        self.t = Connector(1)
        
    def setInput(self,t=None,enable = None):
        if t is not None:
            if isinstance(t,Connector):
                self.t = t
            else:
                self.t.state = int(t)
        if enable is not None:
            if isinstance(enable,Connector):
                self.enable = enable
            else:
                self.enable.state = int(enable)
        
    def __call__(self):
        self.trigger()
    
    def Enable(self):
        #Enables counting on trigger
        self.enable.state = 1
    
    def Disable(self):
        #Disables counter
        self.enable.state = 0
    
    def reset(self):
        #Resets the counter to 0
        for i in range(self.bits):
            self.out[i].state = 0
        self.enable.state = 1
        
    def state(self):
        #MSB is at the Right Most position
        #To print with MSB at the Left Most position
        
        return [self.out[i].state for i in range(self.bits-1,-1,-1)]
    
class BinaryCounter(Counter):
    """
    A 2 Bit Binary Counter
    """
    def __init__(self):
        Counter.__init__(self,2)
        #Calling the super class constructor
        
        self.ff = [TFlipFlop(t,self.enable,self.out[0]), TFlipFlop(self.out[0],self.enable,self.out[1])]
        #<self.bit> nos of TFlipFlop instances are appended in the ff array
        #The trigger of the second FlipFlop is controlled by the output of the previous stage
    def trigger(self):
        #Trigger acts as the clock pulse for incrementing the counter
        if self.enable:
            self.ff[0].trigger()
    
class NBitRippleCounter(Counter):
    """
    An N-Bit Ripple Counter
    """
    def __init__(self,bits):
        Counter.__init__(self,bits)
        #Calling the super class constructor
        
        self.ff.append(TFlipFlop(t,self.enable,self.out[0]))
        for i in range(1,self.bits):
            self.ff.append(TFlipFlop(out[i-1],self.enable,self.out[i]))
        
    def trigger(self,t):
        if self.enable:
            self.ff[0].trigger()
