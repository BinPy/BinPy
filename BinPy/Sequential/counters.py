from BinPy import *
from sequential import *

class Counter(object):
    """
    Base class for all counters
    """
    def __init__(self,bits):
        
        self.bits = bits
        self.out = [0]*self.bits
        self.outold = self.out[:]
        self.ff = []
        self.enable = 1
        
    def __call__(self):
        #Returns the output array
        #To print with MSB at the Left Most position
        return self.out[::-1]
    
    def enable(self):
        #Enables counting on trigger
        self.enable = 1
    
    def disable(self):
        #Disables counter
        self.enable = 0
    
    def reset(self):
        #Resets the counter to 0
        self.out = [0]*self.bits
        self.enable = 1
    
class BinaryCounter(Counter):
    """
    A 2 Bit Binary Counter
    """
    def __init__(self):
        
        Counter.__init__(self,2)
        #Calling the super class constructor
                
        self.ff = [TFlipFlop(), TFlipFlop()]
                
        #<self.bit> nos of TFlipFlop instances are appended in the ff array
        
    def trigger(self,t):
        #Trigger acts as the clock pulse for incrementing the counter
        tmp = [ self.ff[0](t,self.enable)[0]  ,  self.ff[1](self.out[0],self.enable)[0] ]
        #The trigger of the second FlipFlop is controlled by the output of the previous stage
        
        self.out = tmp[:]
        #MSB is at the Right Most position
        
        #To print with MSB at the Left Most position
        return self.out[::-1]
    
class NBitRippleCounter(Counter):
    """
    An N-Bit Ripple Counter
    """
    def __init__(self,bits):
        
        Counter.__init__(self,bits)
        #Calling the super class constructor
        
        for i in xrange(bits):
            self.ff.append(TFlipFlop())
        
    def trigger(self,t):
        if self.enable:
            tmp = []
            tmp.append( self.ff[0](1,t)[0] )
            for i in xrange(1,self.bits):
                tog = 1 if ( (self.out[i-1] == 1) and (tmp[i-1] == 0) ) else 0
                #Next ff is toggled when there is a falling edge at the previous ff's output)
                tmp.append( self.ff[i](1,tog)[0])            
            
            self.out = tmp[:]
            #MSB is at Right most position
            
        #To print with MSB at the Left Most position
        return self.out[::-1]